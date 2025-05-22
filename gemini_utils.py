import os
import ast
import json
import re
import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)


def extract_sections_from_custom(content):
    """
    Use Gemini to extract sections and questions from a custom uploaded template
    """
    model = genai.GenerativeModel()

    prompt = f"""
    You are a grant writing assistant. I'm going to provide you with a custom grant template.
    Please analyze it and extract the main sections and potential questions that need to be answered for each section.
    
    Format your response as a JSON array of sections, where each section has:
    - id: a unique string identifier
    - title: the section title
    - description: a brief description of the section
    - questions: an array of question objects, each with:
      - id: a unique string identifier
      - text: the question text
      - type: either "text" for short answers or "textarea" for longer responses
    
    Here is the template content:
    
    {content}
    
    Return ONLY the JSON array, nothing else.
    """

    response = model.generate_content(prompt)

    try:

        # Extract the required part of the response
        text_block = response.candidates[0].content.parts[0].text
        json_match = re.search(r"```json\n(.*?)```", text_block, re.DOTALL)
        json_str = json_match.group(1)
        sections = json.loads(json_str)
        return sections
    except json.JSONDecodeError:
        # If parsing fails, return a default section structure
        import uuid
        return [
            {
                'id': str(uuid.uuid4()),
                'title': 'Custom Section',
                'description': 'Section extracted from custom template',
                'questions': [
                    {
                        'id': str(uuid.uuid4()),
                        'text': 'Please provide content for this section',
                        'type': 'textarea'
                    }
                ]
            }
        ]


def generate_answers(draft_sections, file_contents):
    '''Use Gemini to generate answers for the questions in the draft'''
    model = genai.GenerativeModel()
    general_format = {
        "sections": [
            {
                "id": "id_of_section1",
                "title": "title_of_section1",
                "description": "description_of_section1",
                "questions": [
                    {
                        "id": "id_of_question1_section1",
                        "text": "Question1",
                        "type": "type_of_question1_section1(can be ignored)"
                    },
                    {
                        "id": "id_of_question2_section1",
                        "text": "Question2",
                        "type": "type_of_question2_section1(can be ignored)"
                    },]
            },
            {
                "id": "id_of_section2",
                "title": "title_of_section2",
                "description": "description_of_section2",
                "questions": [
                    {
                        "id": "id_of_question1_section2",
                        "text": "Question2",
                        "type": "type_of_question2_section2(can be ignored)"
                    },
                    {
                        "id": "id_of_question2_section2",
                        "text": "Question2",
                        "type": "type_of_question2_section2(can be ignored)"
                    },]
            },
        ]
    }
    sample_answers = {"answers": [
        {
            "id": "id_of_section1",
            "answers": [
                {
                    "id": "id_of_question1_section1",
                    "text": "Answer1"
                },
                {
                    "id": "id_of_question2_section1",
                    "text": "Answer2"
                },]
        },
        {
            "id": "id_of_section2",
            "answers": [
                {
                    "id": "id_of_question1_section2",
                    "text": "Answer1"
                },
                {
                    "id": "id_of_question2_section2",
                    "text": "Answer2"
                },]
        }]}
    prompt = f'''
                You are a grant drafting agent who has to do a few specific tasks:
                You will be provided with a list of sections, each section will have a list of questions (with id for each question).
                You will have to (a) extract all the questions from the sections, (b) look through the content provided to you below and (c) answer the questions in a specific format.
                Here are some contents specific to the grant proposal that you can use (if you find any relevant information, else ignore it):
                {file_contents}
                Below are the questions that need to be answered:
                {str(draft_sections)}
                You will have to just return a JSON array in the following format:
                question_id: answer, question_id: answer, and so on.
    '''
    response = model.generate_content(prompt)
    try:
        # Extract the required part of the response
        text_block = response.candidates[0].content.parts[0].text
        json_match = re.search(r"```json\n(.*?)```", text_block, re.DOTALL)
        json_str = json_match.group(1)
        answers = ast.literal_eval(json_str)
        return answers
    except json.JSONDecodeError:
        # If parsing fails, return an empty dictionary
        return {
            "answers": []
        }


def generate_grant_content(draft, template):
    """
    Generate the full grant content using Gemini
    """
    model = genai.GenerativeModel()

    # Prepare the context for Gemini
    context = {
        'template_name': template['name'],
        'template_description': template['description'],
        'sections': []
    }

    for section in draft['sections']:
        section_data = {
            'title': section['title'],
            'description': section['description'],
            'questions': []
        }

        for question in section.get('questions', []):
            question_id = question['id']
            answer = draft['answers'].get(question_id, '')

            section_data['questions'].append({
                'text': question['text'],
                'answer': answer
            })

        context['sections'].append(section_data)

    # Add diagrams if available
    diagrams_context = []
    for diagram in draft.get('diagrams', []):
        diagrams_context.append({
            'title': diagram['title'],
            'type': diagram['type'],
            'description': f"Figure: {diagram['title']}"
        })

    context['diagrams'] = diagrams_context

    # Create the prompt for Gemini
    prompt = f"""
    You are a professional grant writer. I'm going to provide you with information about a grant proposal,
    including the template type, sections, questions, and the user's answers.
    
    Your task is to generate a complete, well-formatted grant proposal based on this information.
    The proposal should be professional, persuasive, and follow best practices for grant writing.
    
    For each section, use the user's answers to craft compelling content. Expand on their points,
    add appropriate transitions, and ensure the narrative flows well throughout the document.
    
    Here is the information:
    
    Template: {context['template_name']} - {context['template_description']}
    
    Sections:
    """

    for section in context['sections']:
        prompt += f"\n\n## {section['title']}\n{section['description']}\n"

        for question in section['questions']:
            prompt += f"\nQuestion: {question['text']}\nAnswer: {question['answer']}\n"

    if diagrams_context:
        prompt += "\n\nDiagrams to reference:\n"
        for diagram in diagrams_context:
            prompt += f"\n- {diagram['title']} ({diagram['type']}): {diagram['description']}\n"

    prompt += """
    
    Please generate a complete grant proposal with the following guidelines:
    1. Format each section with proper headings and subheadings
    2. Maintain a professional, persuasive tone throughout
    3. Expand on the user's answers to create comprehensive content
    4. Reference the diagrams where appropriate as figures
    5. Use markdown formatting for the output
    
    Generate the complete grant proposal now:
    """

    response = model.generate_content(prompt)
    return response.text


def generate_section_content(section, answers):
    """
    Generate content for a specific section using Gemini
    """
    model = genai.GenerativeModel()

    # Prepare the context for this section
    section_context = {
        'title': section['title'],
        'description': section['description'],
        'questions': []
    }

    for question in section.get('questions', []):
        question_id = question['id']
        answer = answers.get(question_id, '')

        section_context['questions'].append({
            'text': question['text'],
            'answer': answer
        })

    # Create the prompt for Gemini
    prompt = f"""
    You are a professional grant writer. I'm going to provide you with information about a section of a grant proposal,
    including the section title, description, questions, and the user's answers.
    
    Your task is to generate well-written content for this section based on the information provided.
    The content should be professional, persuasive, and follow best practices for grant writing.
    
    Here is the information:
    
    Section: {section_context['title']}
    Description: {section_context['description']}
    
    Questions and Answers:
    """

    for question in section_context['questions']:
        prompt += f"\nQuestion: {question['text']}\nAnswer: {question['answer']}\n"

    prompt += """
    
    Please generate content for this section with the following guidelines:
    1. Format with proper headings and subheadings as needed
    2. Maintain a professional, persuasive tone
    3. Expand on the user's answers to create comprehensive content
    4. Use markdown formatting for the output
    
    Generate the section content now:
    """

    response = model.generate_content(prompt)
    return response.text
