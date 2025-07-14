import os
import json
import google.generativeai as genai
from typing import Optional, List, Dict, Any
import requests
from bs4 import BeautifulSoup
from config import GEMINI_API_KEY
import markdown

# Configure Gemini API
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=GEMINI_API_KEY)

# Simple in-memory conversation storage
conversation_memory = {}

# Initialize LangChain components
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain.memory import ConversationBufferWindowMemory
    from langchain.schema import HumanMessage, AIMessage
    
    # Initialize LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GEMINI_API_KEY,
        temperature=0.7
    )
    
    print("✓ LangChain components initialized successfully")
    LANGCHAIN_AVAILABLE = True
    
except Exception as e:
    print(f"⚠️ LangChain initialization failed: {e}")
    print("Falling back to direct Gemini API with manual memory")
    llm = None
    LANGCHAIN_AVAILABLE = False

def get_conversation_memory(project_id: str) -> List[Dict]:
    """Get conversation history for a project"""
    if project_id not in conversation_memory:
        conversation_memory[project_id] = []
    return conversation_memory[project_id]

def add_to_conversation_memory(project_id: str, user_message: str, ai_response: str):
    """Add message pair to conversation memory"""
    if project_id not in conversation_memory:
        conversation_memory[project_id] = []
    
    conversation_memory[project_id].append({
        'user': user_message,
        'ai': ai_response,
        'timestamp': datetime.now().isoformat()
    })
    
    # Keep only last 10 exchanges to prevent memory overflow
    if len(conversation_memory[project_id]) > 10:
        conversation_memory[project_id] = conversation_memory[project_id][-10:]

def chat_with_gemini_direct(message: str, project_context: Optional[Dict] = None, project_id: str = None) -> str:
    """
    Enhanced chat with memory and context - keeping original function name for compatibility
    """
    if LANGCHAIN_AVAILABLE and llm:
        return chat_with_langchain_memory(message, project_context, project_id)
    else:
        return chat_with_manual_memory(message, project_context, project_id)

def chat_with_langchain_memory(message: str, project_context: Optional[Dict] = None, project_id: str = None) -> str:
    """
    Chat using LangChain with proper memory management
    """
    try:
        # Create memory for this project
        memory = ConversationBufferWindowMemory(
            k=10,  # Keep last 10 exchanges
            return_messages=True
        )
        
        # Load previous conversation into memory
        if project_id:
            history = get_conversation_memory(project_id)
            for exchange in history:
                memory.chat_memory.add_user_message(exchange['user'])
                memory.chat_memory.add_ai_message(exchange['ai'])
        
        # Build context-aware prompt
        system_context = build_system_context(project_context, project_id)
        
        # Get memory variables
        memory_vars = memory.load_memory_variables({})
        chat_history = memory_vars.get('history', [])
        
        # Create comprehensive prompt
        full_prompt = f"""{system_context}

CONVERSATION HISTORY:
{format_chat_history(chat_history)}

CURRENT USER MESSAGE: {message}

Please respond helpfully based on the project context and conversation history:"""

        # Get response from LangChain
        response = llm.invoke([HumanMessage(content=full_prompt)])
        ai_response = response.content
        
        # Save to memory
        if project_id:
            add_to_conversation_memory(project_id, message, ai_response)
        
        return ai_response
        
    except Exception as e:
        print(f"LangChain chat error: {e}")
        return chat_with_manual_memory(message, project_context, project_id)

def chat_with_manual_memory(message: str, project_context: Optional[Dict] = None, project_id: str = None) -> str:
    """
    Direct Gemini chat with manual memory management
    """
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Build context
        system_context = build_system_context(project_context, project_id)
        
        # Get conversation history
        history_text = ""
        if project_id:
            history = get_conversation_memory(project_id)
            if history:
                history_text = "\nPREVIOUS CONVERSATION:\n"
                for exchange in history[-5:]:  # Last 5 exchanges
                    history_text += f"User: {exchange['user']}\nAI: {exchange['ai'][:200]}...\n\n"
        
        # Create full prompt
        full_prompt = f"""{system_context}

{history_text}

CURRENT USER MESSAGE: {message}

Based on our conversation history and the project context, please provide a helpful, specific response:"""

        response = model.generate_content(full_prompt)
        ai_response = response.text if response and response.text else "I'm having trouble generating a response. Please try again."
        
        # Save to memory
        if project_id:
            add_to_conversation_memory(project_id, message, ai_response)
        
        return ai_response
        
    except Exception as e:
        print(f"Gemini API error: {e}")
        return "I'm having trouble connecting to the AI service. Please check your connection and try again."

def build_system_context(project_context: Optional[Dict] = None, project_id: str = None) -> str:
    """Build comprehensive system context"""
    
    context_parts = ["""You are an expert AI assistant for grantY, specializing in grant writing, business proposals, and document creation. You have memory of our conversation and can reference previous topics.

CORE CAPABILITIES:
• Grant writing and funding strategies
• Business proposal development
• Document structure and formatting
• Finding funding opportunities
• Professional writing assistance
• Project planning and organization

MEMORY INSTRUCTIONS:
• Remember what we've discussed before
• Reference previous questions and topics
• Build on our conversation history
• Provide continuity in advice"""]

    if project_context:
        context_parts.append(f"""
CURRENT PROJECT CONTEXT:
• Title: {project_context.get('title', 'Unknown Project')}
• Type: {project_context.get('project_type', 'Unknown').replace('_', ' ').title()}
• Status: {'Has generated content' if project_context.get('generated_content') else 'Content not yet generated'}
• Sections: {len(project_context.get('sections', []))} sections available
• Progress: {len([v for v in project_context.get('answers', {}).values() if str(v).strip()])} questions answered""")

        # Add content preview if available
        if project_context.get('generated_content'):
            content_preview = project_context['generated_content'][:300]
            context_parts.append(f"""
CURRENT CONTENT PREVIEW:
{content_preview}...""")
        
        # Add section information
        sections = project_context.get('sections', [])
        if sections:
            section_info = []
            for section in sections[:3]:
                section_info.append(f"• {section.get('title', 'Unknown Section')}")
            context_parts.append(f"""
DOCUMENT SECTIONS:
{chr(10).join(section_info)}
{"• ... and more sections" if len(sections) > 3 else ""}""")

    return '\n'.join(context_parts)

def format_chat_history(history) -> str:
    """Format chat history for prompt"""
    if not history:
        return "No previous conversation."
    
    formatted = []
    for msg in history[-6:]:  # Last 6 messages
        if hasattr(msg, 'content'):
            role = "User" if msg.__class__.__name__ == "HumanMessage" else "AI"
            content = msg.content[:150] + "..." if len(msg.content) > 150 else msg.content
            formatted.append(f"{role}: {content}")
    
    return '\n'.join(formatted)

# Import datetime for memory timestamps
from datetime import datetime

def restructure_content_with_ai(content: str, instructions: str) -> str:
    """
    Restructure content based on user instructions
    """
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = f"""
You are a professional editor. Restructure the following content based on these instructions:

Instructions: {instructions}

Original Content:
{content}

Requirements:
1. Maintain all important information
2. Improve structure and flow
3. Use proper HTML formatting
4. Ensure professional tone
5. Make it more compelling and clear

Return the restructured content in clean HTML format.
"""
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        print(f"Error restructuring content: {e}")
        return content

def extract_sections_with_sample_answers(content: str) -> List[Dict]:
    """
    Extract sections and questions from uploaded template content
    """
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = f"""
Analyze this document and extract sections with questions and sample answers.

Document Content:
{content[:4000]}...

Create a JSON structure with sections, each containing:
- id: unique identifier (kebab-case)
- title: section name
- description: what this section covers
- questions: array of questions with:
  - id: unique identifier (kebab-case) 
  - text: the question
  - type: "text" or "textarea"
  - sample_answer: realistic example answer

Return ONLY valid JSON starting with [ and ending with ].
"""
        
        response = model.generate_content(prompt)
        
        # Clean and parse response
        text = response.text.strip()
        if text.startswith('```json'):
            text = text[7:]
        if text.endswith('```'):
            text = text[:-3]
        text = text.strip()
        
        sections = json.loads(text)
        
        # Validate structure
        if isinstance(sections, list) and sections:
            return validate_sections(sections)
        else:
            return get_default_sections()
            
    except Exception as e:
        print(f"Error extracting sections: {e}")
        return get_default_sections()

def validate_sections(sections: List[Dict]) -> List[Dict]:
    """
    Validate and clean extracted sections
    """
    valid_sections = []
    
    for i, section in enumerate(sections):
        if not isinstance(section, dict):
            continue
            
        valid_section = {
            'id': section.get('id', f'section-{i+1}'),
            'title': section.get('title', f'Section {i+1}'),
            'description': section.get('description', ''),
            'questions': []
        }
        
        questions = section.get('questions', [])
        if isinstance(questions, list):
            for j, question in enumerate(questions):
                if isinstance(question, dict):
                    valid_question = {
                        'id': question.get('id', f'q{i+1}-{j+1}'),
                        'text': question.get('text', f'Question {j+1}'),
                        'type': question.get('type', 'textarea'),
                        'sample_answer': question.get('sample_answer', 'Please provide your response.')
                    }
                    valid_section['questions'].append(valid_question)
        
        if valid_section['questions']:
            valid_sections.append(valid_section)
    
    return valid_sections if valid_sections else get_default_sections()

def get_default_sections() -> List[Dict]:
    """
    Default sections when extraction fails
    """
    return [
        {
            'id': 'project-overview',
            'title': 'Project Overview',
            'description': 'Basic information about your project',
            'questions': [
                {
                    'id': 'project-title',
                    'text': 'What is the title of your project?',
                    'type': 'text',
                    'sample_answer': 'Innovative Community Development Initiative'
                },
                {
                    'id': 'project-description',
                    'text': 'Provide a brief description of your project.',
                    'type': 'textarea',
                    'sample_answer': 'This project aims to address critical community needs through innovative solutions and strategic partnerships.'
                }
            ]
        },
        {
            'id': 'objectives',
            'title': 'Project Objectives',
            'description': 'Main goals and objectives',
            'questions': [
                {
                    'id': 'main-objectives',
                    'text': 'What are the main objectives of this project?',
                    'type': 'textarea',
                    'sample_answer': 'Our objectives are to: 1) Address key challenges, 2) Create sustainable impact, 3) Build partnerships, 4) Deliver measurable results.'
                }
            ]
        }
    ]

def generate_grant_content(draft: Dict, template: Dict) -> str:
    """
    Generate complete document content using AI
    """
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Prepare sections content
        sections_text = ""
        answers = draft.get('answers', {})
        
        for section in draft.get('sections', []):
            sections_text += f"\n\n## {section['title']}\n"
            sections_text += f"Purpose: {section['description']}\n"
            
            for question in section.get('questions', []):
                answer = answers.get(question['id'], '').strip()
                if answer:
                    sections_text += f"Q: {question['text']}\nA: {answer}\n"
        
        if not sections_text.strip():
            return generate_basic_content(draft, template)
        
        prompt = f"""
Create a professional document based on this information:

Title: {draft['title']}
Type: {template['name']}

Content:
{sections_text}

Requirements:
1. Create a comprehensive, well-structured document
2. Use proper HTML formatting (<h1>, <h2>, <p>, <ul>, <li>)
3. Expand answers into professional narrative
4. Maintain logical flow between sections
5. Include specific details and examples
6. Use persuasive, professional language
7. Make it publication-ready

Generate the complete document in HTML format:
"""
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        print(f"Error generating content: {e}")
        return generate_basic_content(draft, template)

def generate_basic_content(draft: Dict, template: Dict) -> str:
    """
    Generate basic content structure
    """
    title = draft.get('title', 'Untitled Project')
    template_name = template.get('name', 'Template')
    
    content = f"""
<div style="max-width: 800px; margin: 0 auto; padding: 20px; font-family: Arial, sans-serif;">
    <h1 style="color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px;">
        {title}
    </h1>
    
    <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
        <h2 style="color: #2980b9; margin-top: 0;">Document Overview</h2>
        <p>This document was created using the <strong>{template_name}</strong> template.</p>
    </div>
    
    <div style="background: #fff3cd; border: 1px solid #ffeaa7; padding: 15px; border-radius: 6px;">
        <p style="margin: 0; color: #856404;">
            <strong>Note:</strong> Complete the questions in the editor to generate comprehensive content.
        </p>
    </div>
</div>
"""
    return content

def find_funding_opportunities(query: str) -> List[Dict]:
    """
    Find funding opportunities using AI with specific focus on the query
    """
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = f"""
Based on the query "{query}", suggest relevant funding opportunities that would be realistic and helpful.

Analyze the query to understand the project type and suggest appropriate funding sources such as:
- Government grants (federal, state, local)
- Private foundations
- Corporate grants and CSR programs
- Industry-specific funding
- Research grants
- Innovation and startup funding
- Social impact funding

Create realistic funding opportunities that would match this specific query.

Return a JSON array with 4-6 opportunities, each having:
- title: opportunity name
- description: brief description (2-3 sentences)
- link: realistic URL or organization name
- deadline: application deadline
- amount: funding amount range
- remarks: additional notes about eligibility

Return only valid JSON.
"""
        
        response = model.generate_content(prompt)
        
        # Parse response
        text = response.text.strip()
        if text.startswith('```json'):
            text = text[7:]
        if text.endswith('```'):
            text = text[:-3]
        
        opportunities = json.loads(text)
        return opportunities if isinstance(opportunities, list) else []
        
    except Exception as e:
        print(f"Error finding opportunities: {e}")
        return []

def get_opportunities(content: str) -> List[Dict]:
    """
    Extract opportunities from document content
    """
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = f"""
Analyze this content and suggest relevant funding opportunities:

Content:
{content[:2000]}...

Based on this content, suggest realistic funding opportunities that would be relevant.

Return a JSON array of opportunities with:
- title: opportunity name
- description: description
- link: URL (can be example if needed)
- deadline: realistic deadline
- amount: funding amount
- remarks: additional notes

Return only valid JSON.
"""
        
        response = model.generate_content(prompt)
        
        # Parse response
        text = response.text.strip()
        if text.startswith('```json'):
            text = text[7:]
        if text.endswith('```'):
            text = text[:-3]
        
        opportunities = json.loads(text)
        return opportunities if isinstance(opportunities, list) else []
        
    except Exception as e:
        print(f"Error extracting opportunities: {e}")
        return []

# Test function
def test_gemini_connection() -> bool:
    """
    Test if Gemini API is working
    """
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content("Hello, this is a test.")
        return bool(response and response.text)
    except Exception as e:
        print(f"Gemini test failed: {e}")
        return False

# Clear conversation memory function for debugging
def clear_conversation_memory(project_id: str = None):
    """Clear conversation memory for a project or all projects"""
    if project_id:
        conversation_memory.pop(project_id, None)
    else:
        conversation_memory.clear()

print("✓ Enhanced Gemini Utils loaded with memory support")
if LANGCHAIN_AVAILABLE:
    print("✓ LangChain available with memory management")
else:
    print("ℹ️ Using direct Gemini API with manual memory")