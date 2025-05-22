import os
import json
import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def extract_sections_with_sample_answers(content):
    """
    Use Gemini to extract sections, questions, and generate sample answers from custom template
    """
    import uuid
    
    print(f"DEBUG: Starting custom template extraction with sample answers...")
    print(f"DEBUG: Content length: {len(content)} characters")
    
    try:
        models_to_try = ['gemini-1.5-flash', 'gemini-1.5-pro']
        
        for model_name in models_to_try:
            try:
                print(f"DEBUG: Trying model: {model_name}")
                model = genai.GenerativeModel(model_name)
                
                prompt = f"""
                You are a grant writing assistant. Analyze the provided grant template and extract sections, questions, and generate realistic sample answers.
                
                For each section found, create questions that need to be answered, and provide realistic sample answers that would be appropriate for a typical grant application.
                
                Format your response as a JSON array of sections, where each section has:
                - id: a unique string identifier (use kebab-case)
                - title: the section title
                - description: a brief description of the section
                - questions: an array of question objects, each with:
                  - id: a unique string identifier (use kebab-case)
                  - text: the question text
                  - type: either "text" for short answers or "textarea" for longer responses
                  - sample_answer: a realistic sample answer that demonstrates what should be written
                
                Make the sample answers professional, realistic, and helpful as examples. They should be 1-3 sentences for text fields and 1-2 paragraphs for textarea fields.
                
                Template content:
                {content}
                
                Return ONLY the JSON array, nothing else.
                """
                
                response = model.generate_content(prompt)
                print(f"DEBUG: Gemini response received, length: {len(response.text)} characters")
                
                # Clean the response
                response_text = response.text.strip()
                if response_text.startswith('```json'):
                    response_text = response_text[7:]
                if response_text.endswith('```'):
                    response_text = response_text[:-3]
                response_text = response_text.strip()
                
                # Parse the response as JSON
                sections = json.loads(response_text)
                
                # Validate the structure
                if isinstance(sections, list) and len(sections) > 0:
                    valid_sections = []
                    for i, section in enumerate(sections):
                        if isinstance(section, dict):
                            valid_section = {
                                'id': section.get('id', f'section-{i+1}'),
                                'title': section.get('title', f'Section {i+1}'),
                                'description': section.get('description', ''),
                                'questions': []
                            }
                            
                            # Validate questions
                            questions = section.get('questions', [])
                            if isinstance(questions, list):
                                for j, question in enumerate(questions):
                                    if isinstance(question, dict):
                                        valid_question = {
                                            'id': question.get('id', f'q{i+1}-{j+1}'),
                                            'text': question.get('text', f'Question {j+1}'),
                                            'type': question.get('type', 'textarea'),
                                            'sample_answer': question.get('sample_answer', 'Please provide your response here.')
                                        }
                                        valid_section['questions'].append(valid_question)
                            
                            if valid_section['questions']:
                                valid_sections.append(valid_section)
                    
                    if valid_sections:
                        print(f"DEBUG: Successfully extracted {len(valid_sections)} sections with sample answers")
                        return valid_sections
                        
            except Exception as model_error:
                print(f"DEBUG: Error with model {model_name}: {model_error}")
                continue
        
        # Fallback to content analysis
        print("DEBUG: All models failed, creating sections with sample answers from content analysis...")
        return create_sections_with_samples_from_content(content)
        
    except Exception as e:
        print(f"DEBUG: Complete failure: {e}")
        return create_default_sections_with_samples()

def create_sections_with_samples_from_content(content):
    """
    Fallback function to create sections with sample answers by analyzing content
    """
    import uuid
    import re
    
    print("DEBUG: Creating sections with sample answers from content analysis...")
    
    sections = []
    
    # Common grant sections with sample answers
    common_sections = [
        {
            'title': 'Project Overview',
            'description': 'Basic information about your project',
            'questions': [
                {
                    'text': 'What is the title of your project?',
                    'type': 'text',
                    'sample_answer': 'Innovative Community Development Initiative for Rural Education'
                },
                {
                    'text': 'Provide a brief description of your project.',
                    'type': 'textarea',
                    'sample_answer': 'This project aims to improve educational outcomes in rural communities by implementing technology-enhanced learning programs. We will establish computer labs, provide teacher training, and develop digital curricula that addresses local needs and challenges.'
                }
            ]
        },
        {
            'title': 'Organization Information',
            'description': 'Details about your organization',
            'questions': [
                {
                    'text': 'What is your organization name?',
                    'type': 'text',
                    'sample_answer': 'Community Education Foundation'
                },
                {
                    'text': 'Describe your organization\'s mission and experience.',
                    'type': 'textarea',
                    'sample_answer': 'Our organization has been dedicated to improving educational access in underserved communities for over 15 years. We have successfully implemented 25+ educational programs reaching over 5,000 students across rural areas.'
                }
            ]
        },
        {
            'title': 'Project Goals and Objectives',
            'description': 'Specific goals and measurable objectives',
            'questions': [
                {
                    'text': 'What are the main goals of this project?',
                    'type': 'textarea',
                    'sample_answer': 'Our primary goals are to: 1) Increase student engagement through technology integration, 2) Improve academic performance by 25% in participating schools, 3) Train 50 teachers in digital teaching methods, and 4) Create sustainable educational programs that continue beyond the grant period.'
                }
            ]
        },
        {
            'title': 'Budget and Resources',
            'description': 'Financial requirements and resource allocation',
            'questions': [
                {
                    'text': 'What is the total budget requested?',
                    'type': 'text',
                    'sample_answer': '$75,000'
                },
                {
                    'text': 'Provide a detailed budget breakdown.',
                    'type': 'textarea',
                    'sample_answer': 'Personnel (40% - $30,000): Project coordinator and training staff\nEquipment (35% - $26,250): Computers, tablets, and networking equipment\nTraining Materials (15% - $11,250): Curriculum development and educational resources\nOperational Costs (10% - $7,500): Transportation, utilities, and administrative expenses'
                }
            ]
        }
    ]
    
    # Create sections with unique IDs
    for i, section_data in enumerate(common_sections):
        section = {
            'id': f'section-{i+1}',
            'title': section_data['title'],
            'description': section_data['description'],
            'questions': []
        }
        
        for j, question_data in enumerate(section_data['questions']):
            question = {
                'id': f'q{i+1}-{j+1}',
                'text': question_data['text'],
                'type': question_data['type'],
                'sample_answer': question_data['sample_answer']
            }
            section['questions'].append(question)
        
        sections.append(section)
    
    print(f"DEBUG: Created {len(sections)} sections with sample answers from content analysis")
    return sections

def create_default_sections_with_samples():
    """
    Create default sections with sample answers as last resort
    """
    import uuid
    
    return [
        {
            'id': str(uuid.uuid4()),
            'title': 'Project Information',
            'description': 'Basic information about your grant project',
            'questions': [
                {
                    'id': str(uuid.uuid4()),
                    'text': 'What is your project about?',
                    'type': 'textarea',
                    'sample_answer': 'Our project focuses on addressing critical community needs through innovative solutions. We aim to create lasting positive impact by leveraging resources effectively and engaging stakeholders meaningfully.'
                }
            ]
        }
    ]

def generate_grant_content(draft, template):
    """
    Generate the full grant content using Gemini
    """
    try:
        print(f"DEBUG: Starting content generation for draft {draft['id']}")
        
        # Use Gemini model for content generation
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Check if we have meaningful answers
        answers = draft.get('answers', {})
        if not answers or all(not str(v).strip() for v in answers.values()):
            print("DEBUG: No meaningful answers found, generating basic template")
            return generate_basic_template_content(draft, template)
        
        # Prepare context for Gemini
        sections_content = []
        for section in draft['sections']:
            section_data = {
                'title': section['title'],
                'description': section['description'],
                'content': []
            }
            
            for question in section.get('questions', []):
                question_id = question['id']
                answer = answers.get(question_id, '').strip()
                
                if answer:
                    section_data['content'].append({
                        'question': question['text'],
                        'answer': answer
                    })
            
            if section_data['content']:
                sections_content.append(section_data)
        
        # Create comprehensive prompt
        prompt = f"""
        You are a professional grant writer. Create a complete, well-structured grant proposal based on the following information:
        
        Project Title: {draft['title']}
        Template: {template['name']}
        
        Sections and Responses:
        """
        
        for section in sections_content:
            prompt += f"\n\n=== {section['title']} ===\n"
            prompt += f"Purpose: {section['description']}\n"
            for item in section['content']:
                prompt += f"Q: {item['question']}\nA: {item['answer']}\n"
        
        prompt += """
        
        Instructions:
        1. Create a professional, compelling grant proposal
        2. Use proper HTML formatting with headings, paragraphs, and lists
        3. Expand on the provided answers to create comprehensive content
        4. Maintain a persuasive, professional tone throughout
        5. Ensure logical flow between sections
        6. Include specific details and measurable outcomes where possible
        7. Format the output as clean HTML that can be displayed in a web browser
        
        Generate the complete grant proposal now:
        """
        
        print("DEBUG: Sending prompt to Gemini...")
        response = model.generate_content(prompt)
        print(f"DEBUG: Generated content length: {len(response.text)} characters")
        
        return response.text
        
    except Exception as e:
        print(f"ERROR: Failed to generate content: {e}")
        import traceback
        traceback.print_exc()
        return generate_basic_template_content(draft, template)

def generate_basic_template_content(draft, template):
    """
    Generate basic template content when AI generation fails or no answers provided
    """
    print("DEBUG: Generating basic template content")
    
    content = f"""
    <div style="max-width: 800px; margin: 0 auto; padding: 20px; font-family: Arial, sans-serif; line-height: 1.6;">
        <h1 style="color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px;">{draft['title']}</h1>
        <p style="color: #7f8c8d; margin-bottom: 30px;"><em>Generated on {draft.get('updated_at', 'Unknown date')}</em></p>
        
        <div style="background: #ecf0f1; padding: 20px; border-radius: 8px; margin-bottom: 30px;">
            <h2 style="color: #2980b9; margin-top: 0;">Grant Proposal Overview</h2>
            <p style="font-size: 16px;">This comprehensive grant proposal has been developed using the <strong>{template['name']}</strong> template, incorporating your detailed responses to create a professional funding request.</p>
        </div>
    """
    
    # Add sections with user answers
    answers = draft.get('answers', {})
    
    for section in draft.get('sections', []):
        content += f"""
        <section style="margin-bottom: 40px;">
            <h2 style="color: #2c3e50; border-left: 4px solid #3498db; padding-left: 15px; margin-bottom: 20px;">{section['title']}</h2>
            <p style="color: #7f8c8d; margin-bottom: 20px; font-style: italic;">{section['description']}</p>
        """
        
        # Check if we have answers for this section
        section_answers = []
        for question in section.get('questions', []):
            answer = answers.get(question['id'], '').strip()
            if answer:
                section_answers.append({
                    'question': question['text'],
                    'answer': answer,
                    'type': question.get('type', 'textarea')
                })
        
        if section_answers:
            for item in section_answers:
                if item['type'] == 'text':
                    content += f"""
                    <div style="margin-bottom: 20px;">
                        <h4 style="color: #34495e; margin-bottom: 8px;">{item['question']}</h4>
                        <p style="background: #f8f9fa; padding: 10px; border-radius: 4px; margin: 0;"><strong>{item['answer']}</strong></p>
                    </div>
                    """
                else:
                    content += f"""
                    <div style="margin-bottom: 25px;">
                        <h4 style="color: #34495e; margin-bottom: 10px;">{item['question']}</h4>
                        <div style="background: #ffffff; padding: 15px; border: 1px solid #dee2e6; border-radius: 6px;">
                            <p style="margin: 0; text-align: justify;">{item['answer']}</p>
                        </div>
                    </div>
                    """
        else:
            content += f"""
            <div style="background: #fff3cd; border: 1px solid #ffeaa7; padding: 15px; border-radius: 6px;">
                <p style="margin: 0; color: #856404;"><em>Please complete the questions for {section['title']} in the editor to enhance this section.</em></p>
            </div>
            """
        
        content += "</section>"
    
    # Add conclusion
    content += """
        <section style="margin-top: 50px; padding-top: 30px; border-top: 2px solid #ecf0f1;">
            <h2 style="color: #2c3e50;">Conclusion</h2>
            <p style="font-size: 16px; text-align: justify;">This grant proposal represents a comprehensive plan to achieve meaningful impact through strategic implementation of resources and expertise. We are committed to delivering exceptional results and maintaining transparent communication throughout the project lifecycle.</p>
            
            <div style="background: #d4edda; border: 1px solid #c3e6cb; padding: 20px; border-radius: 8px; margin-top: 25px;">
                <h3 style="color: #155724; margin-top: 0;">Next Steps</h3>
                <p style="margin: 0; color: #155724;">We welcome the opportunity to discuss this proposal in detail and provide any additional information required for your review process.</p>
            </div>
        </section>
    </div>
    """
    
    return content

def generate_section_content(section, answers):
    """
    Generate content for a specific section using Gemini
    """
    try:
        print(f"DEBUG: Generating content for section: {section['title']}")
        
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Prepare section context
        section_context = {
            'title': section['title'],
            'description': section['description'],
            'questions': []
        }
        
        for question in section.get('questions', []):
            question_id = question['id']
            answer = answers.get(question_id, '').strip()
            
            if answer:
                section_context['questions'].append({
                    'text': question['text'],
                    'answer': answer
                })
        
        if not section_context['questions']:
            return f"""
            <h3>{section['title']}</h3>
            <p>{section['description']}</p>
            <p><em>No responses provided for this section yet.</em></p>
            """
        
        # Create prompt for section generation
        prompt = f"""
        You are a professional grant writer. Generate compelling content for this section of a grant proposal:
        
        Section: {section_context['title']}
        Purpose: {section_context['description']}
        
        Questions and Answers:
        """
        
        for q_and_a in section_context['questions']:
            prompt += f"\nQ: {q_and_a['text']}\nA: {q_and_a['answer']}\n"
        
        prompt += """
        
        Instructions:
        1. Create professional, persuasive content based on the answers
        2. Use proper HTML formatting
        3. Expand on the answers to create comprehensive narrative
        4. Maintain consistency with grant writing best practices
        
        Generate the section content:
        """
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        print(f"ERROR: Failed to generate section content: {e}")
        return f"""
        <h3>{section['title']}</h3>
        <p>{section['description']}</p>
        <p><em>Error generating content for this section.</em></p>
        """