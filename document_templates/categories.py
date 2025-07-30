# document_templates/categories.py
"""
Template categories definition file.
Add new categories here first before creating templates for them.
"""

TEMPLATE_CATEGORIES = {
    'grant': {
        'name': 'Research Grants',
        'description': 'Professional grant proposal templates for research funding',
        'icon': 'fas fa-university',
        'order': 1
    },
    'pitch_deck': {
        'name': 'Pitch Decks',
        'description': 'Investor pitch deck templates for startups and businesses',
        'icon': 'fas fa-chart-line',
        'order': 2
    },
    'business_proposal': {
        'name': 'Business Proposals',
        'description': 'Professional business proposal templates',
        'icon': 'fas fa-handshake',
        'order': 3
    },
    'executive_summary': {
        'name': 'Executive Summaries',
        'description': 'Concise executive summary templates',
        'icon': 'fas fa-file-alt',
        'order': 4
    },
    'scientific_proposal': {
        'name': 'Scientific Proposals',
        'description': 'Academic and scientific research proposal templates',
        'icon': 'fas fa-microscope',
        'order': 5
    },
    'marketing_plan': {
        'name': 'Marketing Plans',
        'description': 'Comprehensive marketing strategy templates',
        'icon': 'fas fa-bullhorn',
        'order': 6
    },
    'technical_report': {
        'name': 'Technical Reports',
        'description': 'Technical documentation and report templates',
        'icon': 'fas fa-cogs',
        'order': 7
    },
    'project_charter': {
        'name': 'Project Charters',
        'description': 'Project initiation and charter templates',
        'icon': 'fas fa-project-diagram',
        'order': 8
    },
    'legal_document': {
        'name': 'Legal Documents',
        'description': 'Legal document templates and contracts',
        'icon': 'fas fa-gavel',
        'order': 9
    },
    'financial_report': {
        'name': 'Financial Reports',
        'description': 'Financial analysis and reporting templates',
        'icon': 'fas fa-chart-pie',
        'order': 10
    }
}

def get_available_categories():
    """Get list of available template categories"""
    return sorted(TEMPLATE_CATEGORIES.keys(), key=lambda x: TEMPLATE_CATEGORIES[x]['order'])

def get_category_info(category_key):
    """Get information about a specific category"""
    return TEMPLATE_CATEGORIES.get(category_key, {})

def validate_category(category_key):
    """Validate if category exists"""
    return category_key in TEMPLATE_CATEGORIES