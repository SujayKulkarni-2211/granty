import os
import json
from datetime import datetime
import uuid

def get_templates():
    """Get all available templates"""
    templates = []
    template_dir = 'data/templates'
    
    if not os.path.exists(template_dir):
        os.makedirs(template_dir)
        initialize_default_templates()
    
    for filename in os.listdir(template_dir):
        if filename.endswith('.json'):
            with open(os.path.join(template_dir, filename), 'r') as f:
                template = json.load(f)
                templates.append(template)
    
    return templates

def get_template(template_id):
    """Get a specific template by ID"""
    template_path = f'data/templates/{template_id}.json'
    
    if os.path.exists(template_path):
        with open(template_path, 'r') as f:
            return json.load(f)
    
    return None

def save_template(template):
    """Save a template to disk"""
    template_dir = 'data/templates'
    
    if not os.path.exists(template_dir):
        os.makedirs(template_dir)
    
    with open(f'{template_dir}/{template["id"]}.json', 'w') as f:
        json.dump(template, f, indent=2)

def get_drafts():
    """Get all available drafts"""
    drafts = []
    drafts_dir = 'data/drafts'
    
    if not os.path.exists(drafts_dir):
        os.makedirs(drafts_dir)
    
    for filename in os.listdir(drafts_dir):
        if filename.endswith('.json'):
            with open(os.path.join(drafts_dir, filename), 'r') as f:
                draft = json.load(f)
                drafts.append(draft)
    
    # Sort by updated_at (newest first)
    drafts.sort(key=lambda x: x.get('updated_at', ''), reverse=True)
    
    return drafts

def get_draft(draft_id):
    """Get a specific draft by ID"""
    draft_path = f'data/drafts/{draft_id}.json'
    
    if os.path.exists(draft_path):
        with open(draft_path, 'r') as f:
            return json.load(f)
    
    return None

def save_draft(draft):
    """Save a draft to disk"""
    drafts_dir = 'data/drafts'
    
    if not os.path.exists(drafts_dir):
        os.makedirs(drafts_dir)
    
    with open(f'{drafts_dir}/{draft["id"]}.json', 'w') as f:
        json.dump(draft, f, indent=2)

def delete_draft(draft_id):
    """Delete a draft"""
    draft_path = f'data/drafts/{draft_id}.json'
    
    if os.path.exists(draft_path):
        os.remove(draft_path)
        return True
    
    return False

def initialize_default_templates():
    """Create default templates if none exist"""
    templates = [
        {
            'id': str(uuid.uuid4()),
            'name': 'NSF Research Grant',
            'description': 'National Science Foundation research grant proposal template',
            'sections': [
                {
                    'id': str(uuid.uuid4()),
                    'title': 'Project Summary',
                    'description': 'A one-page summary of the proposed project',
                    'questions': [
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What is the intellectual merit of the proposed activity?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What are the broader impacts of the proposed activity?',
                            'type': 'textarea'
                        }
                    ]
                },
                {
                    'id': str(uuid.uuid4()),
                    'title': 'Project Description',
                    'description': 'A comprehensive description of the proposed project',
                    'questions': [
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What are the specific aims of this research?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What is the background and significance of this research?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What is the research design and methodology?',
                            'type': 'textarea'
                        }
                    ]
                },
                {
                    'id': str(uuid.uuid4()),
                    'title': 'Budget and Budget Justification',
                    'description': 'Detailed budget and justification for the proposed project',
                    'questions': [
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What is the total budget requested?',
                            'type': 'text'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'Provide a breakdown of the budget by category (personnel, equipment, etc.)',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'Justify the budget items in relation to the project goals',
                            'type': 'textarea'
                        }
                    ]
                }
            ],
            'created_at': datetime.now().isoformat()
        },
        {
            'id': str(uuid.uuid4()),
            'name': 'NIH Grant Application',
            'description': 'National Institutes of Health grant application template',
            'sections': [
                {
                    'id': str(uuid.uuid4()),
                    'title': 'Specific Aims',
                    'description': 'A concise summary of the aims of the project',
                    'questions': [
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What is the purpose of the proposed research?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What are the specific objectives and hypotheses?',
                            'type': 'textarea'
                        }
                    ]
                },
                {
                    'id': str(uuid.uuid4()),
                    'title': 'Research Strategy',
                    'description': 'Detailed description of the research strategy',
                    'questions': [
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What is the significance of this research?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What is the innovation in this research?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What is the approach for this research?',
                            'type': 'textarea'
                        }
                    ]
                },
                {
                    'id': str(uuid.uuid4()),
                    'title': 'Biographical Sketch',
                    'description': 'Information about the principal investigator',
                    'questions': [
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What is the professional background of the PI?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'List relevant publications and previous research',
                            'type': 'textarea'
                        }
                    ]
                }
            ],
            'created_at': datetime.now().isoformat()
        },
        {
            'id': str(uuid.uuid4()),
            'name': 'Startup Grant Proposal',
            'description': 'Template for startup funding proposals',
            'sections': [
                {
                    'id': str(uuid.uuid4()),
                    'title': 'Executive Summary',
                    'description': 'A brief overview of the startup and funding request',
                    'questions': [
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What problem does your startup solve?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What is your solution and how is it unique?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'How much funding are you requesting and how will it be used?',
                            'type': 'textarea'
                        }
                    ]
                },
                {
                    'id': str(uuid.uuid4()),
                    'title': 'Market Analysis',
                    'description': 'Analysis of the target market and competition',
                    'questions': [
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'Who is your target market and how large is it?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'Who are your competitors and how do you differentiate?',
                            'type': 'textarea'
                        }
                    ]
                },
                {
                    'id': str(uuid.uuid4()),
                    'title': 'Business Model',
                    'description': 'Description of the business model and revenue streams',
                    'questions': [
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What is your business model?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What are your revenue streams?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What is your go-to-market strategy?',
                            'type': 'textarea'
                        }
                    ]
                },
                {
                    'id': str(uuid.uuid4()),
                    'title': 'Financial Projections',
                    'description': 'Financial projections for the next 3-5 years',
                    'questions': [
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What are your revenue projections for the next 3 years?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'What are your expense projections for the next 3 years?',
                            'type': 'textarea'
                        },
                        {
                            'id': str(uuid.uuid4()),
                            'text': 'When do you expect to reach profitability?',
                            'type': 'textarea'
                        }
                    ]
                }
            ],
            'created_at': datetime.now().isoformat()
        }
    ]
    
    for template in templates:
        save_template(template)
