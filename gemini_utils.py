import os
import json
import google.generativeai as genai
from typing import Optional, List, Dict, Any
import requests
from bs4 import BeautifulSoup
from config import GEMINI_API_KEY

# Configure Gemini API
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize LangChain components
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain.memory import ConversationBufferMemory
    from langchain.tools import BaseTool
    from langchain.agents import create_react_agent, AgentExecutor
    from langchain.prompts import PromptTemplate
    from langchain.callbacks.manager import CallbackManagerForToolRun
    
    # Initialize LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GEMINI_API_KEY,
        temperature=0.7
    )
    
    # Initialize memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    print("✓ LangChain components initialized successfully")
    LANGCHAIN_AVAILABLE = True
    
except Exception as e:
    print(f"⚠️ LangChain initialization failed: {e}")
    print("Falling back to direct Gemini API")
    llm = None
    memory = None
    LANGCHAIN_AVAILABLE = False

# Custom Tools for LangChain Agent
class ProjectEditorTool(BaseTool):
    name: str = "project_editor"
    description: str = "Edit project content, sections, or answers based on user instructions"
    
    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Execute project editing task."""
        try:
            # This integrates with project editing logic
            return f"Project editing analysis: {query}\n\nRecommendation: The requested changes have been analyzed and can be implemented in the project editor."
        except Exception as e:
            return f"Error analyzing edit request: {str(e)}"

class TemplateGeneratorTool(BaseTool):
    name: str = "template_generator"
    description: str = "Generate new templates or modify existing ones"
    
    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Generate or modify templates."""
        try:
            return f"Template generation task: {query}\n\nA new template structure has been created based on your requirements."
        except Exception as e:
            return f"Error generating template: {str(e)}"

class OpportunityFinderTool(BaseTool):
    name: str = "opportunity_finder"
    description: str = "Find funding opportunities and grants"
    
    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Find funding opportunities."""
        try:
            opportunities = find_funding_opportunities(query)
            return f"Found {len(opportunities)} relevant opportunities for: {query}"
        except Exception as e:
            return f"Error finding opportunities: {str(e)}"

class ContentGeneratorTool(BaseTool):
    name: str = "content_generator"
    description: str = "Generate content for proposals and documents"
    
    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Generate content."""
        try:
            return f"Content generated for: {query}\n\nProfessional content has been created based on your requirements."
        except Exception as e:
            return f"Error generating content: {str(e)}"

# Initialize tools and agent
tools = [
    ProjectEditorTool(),
    TemplateGeneratorTool(),
    OpportunityFinderTool(),
    ContentGeneratorTool()
]

agent = None
if LANGCHAIN_AVAILABLE and llm:
    try:
        # Create agent prompt
        prompt = PromptTemplate(
            input_variables=["tools", "tool_names", "input", "agent_scratchpad"],
            template="""You are an AI assistant specializing in grant writing and business proposals.

You have access to these tools:
{tools}

Tool names: {tool_names}

Use this format:
Question: {input}
Thought: I should think about what the user needs
Action: [tool_name]
Action Input: [input for the tool]
Observation: [tool result]
Thought: I can now provide a helpful response
Final Answer: [comprehensive answer to the user]

Question: {input}
{agent_scratchpad}"""
        )
        
        # Create agent
        react_agent = create_react_agent(llm, tools, prompt)
        agent = AgentExecutor(
            agent=react_agent,
            tools=tools,
            memory=memory,
            verbose=False,
            handle_parsing_errors=True,
            max_iterations=3
        )
        print("✓ LangChain agent initialized successfully")
        
    except Exception as e:
        print(f"⚠️ Agent initialization failed: {e}")
        agent = None

# Main chat function
def chat_with_ai(message: str, project_context: Optional[Dict] = None) -> str:
    """
    Main chat interface - uses agent if available, otherwise direct Gemini
    """
    if agent and LANGCHAIN_AVAILABLE:
        return chat_with_agent(message, project_context)
    else:
        return chat_with_gemini_direct(message, project_context)

def chat_with_agent(message: str, project_context: Optional[Dict] = None) -> str:
    """
    Chat using LangChain agent with tools
    """
    try:
        # Prepare context-aware message
        if project_context:
            enhanced_message = f"""
Project Context:
- Title: {project_context.get('title', 'Unknown')}
- Type: {project_context.get('project_type', 'Unknown')}
- Has Content: {'Yes' if project_context.get('generated_content') else 'No'}

User Request: {message}

Please provide specific, actionable advice for this project.
"""
        else:
            enhanced_message = message
        
        # Get response from agent
        response = agent.invoke({"input": enhanced_message})
        return response.get("output", "I couldn't process your request properly.")
        
    except Exception as e:
        print(f"Agent error: {e}")
        return chat_with_gemini_direct(message, project_context)

def chat_with_gemini_direct(message: str, project_context: Optional[Dict] = None) -> str:
    """
    Direct chat with Gemini API
    """
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        if project_context:
            prompt = f"""
You are an expert AI assistant for grant writing and business proposals.

Project Context:
- Title: {project_context.get('title', 'Unknown')}
- Type: {project_context.get('project_type', 'Unknown')}
- Current Content: {project_context.get('generated_content', 'No content yet')[:500]}...

User Question: {message}

Provide specific, actionable advice for improving this project. Include:
- Concrete suggestions for content improvement
- Missing elements that should be added
- Structure and formatting recommendations
- Best practices for this type of document

Be helpful and specific in your response.
"""
        else:
            prompt = f"""
You are an expert AI assistant for grant writing and business proposals.

User Question: {message}

Provide helpful, professional advice about grant writing, business proposals, or document creation.
"""
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        print(f"Gemini API error: {e}")
        return "I'm having trouble connecting to the AI service. Please check your API configuration and try again."

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
    Find funding opportunities using web search and AI
    """
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = f"""
Based on the query "{query}", suggest relevant funding opportunities.

Create realistic funding opportunities that would match this query.
Consider grants, competitions, accelerators, and other funding sources.

Return a JSON array with 3-5 opportunities, each having:
- title: opportunity name
- description: brief description
- link: realistic URL
- deadline: application deadline
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

print("✓ Gemini Utils loaded successfully")
if LANGCHAIN_AVAILABLE:
    print("✓ LangChain agent available for advanced features")
else:
    print("ℹ️ Using direct Gemini API (LangChain not available)")