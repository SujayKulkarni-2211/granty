# document_templates/__init__.py
"""
Document Templates Package
Centralized template loading system for all document types
"""

from .categories import TEMPLATE_CATEGORIES, get_available_categories, validate_category
from .grant_templates import GRANT_TEMPLATES
from .pitch_deck_templates import PITCH_DECK_TEMPLATES
from .business_proposal_templates import BUSINESS_PROPOSAL_TEMPLATES
from .executive_summary_templates import EXECUTIVE_SUMMARY_TEMPLATES
from .scientific_proposal_templates import SCIENTIFIC_PROPOSAL_TEMPLATES
from .marketing_plan_templates import MARKETING_PLAN_TEMPLATES
from .technical_report_templates import TECHNICAL_REPORT_TEMPLATES
from .project_charter_templates import PROJECT_CHARTER_TEMPLATES
from .legal_document_templates import LEGAL_DOCUMENT_TEMPLATES
from .financial_report_templates import FINANCIAL_REPORT_TEMPLATES

def load_all_templates():
    """
    Load all templates from all template files
    Returns a list of all available templates
    """
    all_templates = []
    
    # Add templates from each category
    all_templates.extend(GRANT_TEMPLATES)
    all_templates.extend(PITCH_DECK_TEMPLATES)
    all_templates.extend(BUSINESS_PROPOSAL_TEMPLATES)
    all_templates.extend(EXECUTIVE_SUMMARY_TEMPLATES)
    all_templates.extend(SCIENTIFIC_PROPOSAL_TEMPLATES)
    all_templates.extend(MARKETING_PLAN_TEMPLATES)
    all_templates.extend(TECHNICAL_REPORT_TEMPLATES)
    all_templates.extend(PROJECT_CHARTER_TEMPLATES)
    all_templates.extend(LEGAL_DOCUMENT_TEMPLATES)
    all_templates.extend(FINANCIAL_REPORT_TEMPLATES)
    
    return all_templates

def load_templates_by_category(category):
    """
    Load templates for a specific category
    """
    if not validate_category(category):
        return []
    
    category_templates = {
        'grant': GRANT_TEMPLATES,
        'pitch_deck': PITCH_DECK_TEMPLATES,
        'business_proposal': BUSINESS_PROPOSAL_TEMPLATES,
        'executive_summary': EXECUTIVE_SUMMARY_TEMPLATES,
        'scientific_proposal': SCIENTIFIC_PROPOSAL_TEMPLATES,
        'marketing_plan': MARKETING_PLAN_TEMPLATES,
        'technical_report': TECHNICAL_REPORT_TEMPLATES,
        'project_charter': PROJECT_CHARTER_TEMPLATES,
        'legal_document': LEGAL_DOCUMENT_TEMPLATES,
        'financial_report': FINANCIAL_REPORT_TEMPLATES,
    }
    
    return category_templates.get(category, [])

def get_template_count():
    """Get total number of templates available"""
    return len(load_all_templates())

def get_templates_by_category_dict():
    """Get templates organized by category"""
    templates_dict = {}
    
    for category in get_available_categories():
        templates_dict[category] = load_templates_by_category(category)
    
    return templates_dict

# Export main functions
__all__ = [
    'TEMPLATE_CATEGORIES',
    'load_all_templates',
    'load_templates_by_category',
    'get_available_categories',
    'validate_category',
    'get_template_count',
    'get_templates_by_category_dict',
    
]