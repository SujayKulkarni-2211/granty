# Document Templates Module

This modular template system allows easy addition and management of document templates across different categories.

## Structure

```
document_templates/
├── __init__.py                     # Template loader and main functions
├── categories.py                   # Category definitions
├── grant_templates.py              # Grant proposal templates
├── pitch_deck_templates.py         # Pitch deck templates
├── business_proposal_templates.py  # Business proposal templates
├── executive_summary_templates.py  # Executive summary templates
├── scientific_proposal_templates.py # Scientific proposal templates
├── marketing_plan_templates.py     # Marketing plan templates
├── technical_report_templates.py   # Technical report templates
└── README.md                       # This file
```

## Adding New Categories

1. **First, add the category to `categories.py`:**

```python
'new_category': {
    'name': 'Display Name',
    'description': 'Category description',
    'icon': 'fas fa-icon-name',
    'order': 11
}
```

2. **Create a new template file:** `new_category_templates.py`

```python
import uuid

NEW_CATEGORY_TEMPLATES = [
    {
        'id': str(uuid.uuid4()),
        'name': 'Template Name',
        'description': 'Template description',
        'category': 'new_category',
        'sections': [
            {
                'id': 'section-id',
                'title': 'Section Title',
                'description': 'Section description',
                'questions': [
                    {
                        'id': 'question-id',
                        'text': 'Question text?',
                        'type': 'textarea',
                        'sample_answer': 'Placeholder: Sample answer here'
                    }
                ]
            }
        ]
    }
]
```

3. **Update `__init__.py`:**

```python
# Add import
from .new_category_templates import NEW_CATEGORY_TEMPLATES

# Add to load_all_templates()
all_templates.extend(NEW_CATEGORY_TEMPLATES)

# Add to load_templates_by_category()
category_templates = {
    # ... existing categories ...
    'new_category': NEW_CATEGORY_TEMPLATES,
}
```

## Adding New Templates to Existing Categories

Simply add new template objects to the appropriate template file:

```python
# In existing_category_templates.py
EXISTING_CATEGORY_TEMPLATES = [
    # ... existing templates ...
    {
        'id': str(uuid.uuid4()),
        'name': 'New Template Name',
        'description': 'New template description',
        'category': 'existing_category',
        'sections': [
            # ... template sections ...
        ]
    }
]
```

## Template Structure

Each template must have:

* `id`: Unique identifier (use `str(uuid.uuid4())`)
* `name`: Template display name
* `description`: Brief description
* `category`: Must match a category in `categories.py`
* `sections`: Array of section objects

Each section must have:

* `id`: Unique section identifier
* `title`: Section display title
* `description`: Section description
* `questions`: Array of question objects

Each question must have:

* `id`: Unique question identifier
* `text`: Question text
* `type`: Input type ('text' or 'textarea')
* `sample_answer`: Placeholder/sample answer

## Usage in Application

The `storage.py` automatically loads all templates from this modular system:

```python
from document_templates import load_all_templates, TEMPLATE_CATEGORIES

# Load all templates
templates = load_all_templates()

# Get category information
categories = TEMPLATE_CATEGORIES
```

## Benefits

1. **Modular**: Each category has its own file
2. **Scalable**: Easy to add new categories and templates
3. **Maintainable**: Clear separation of concerns
4. **Flexible**: Templates can be easily modified or extended
5. **Organized**: Clear structure and naming conventions

## Current Categories

* **Research Grants**: NSF, NIH, SBIR templates
* **Pitch Decks**: Tech startup, SaaS, Series A templates
* **Business Proposals**: Partnership, project, investment templates
* **Executive Summaries**: Business plan, project, strategic templates
* **Scientific Proposals**: Academic, clinical, laboratory templates
* **Marketing Plans**: Digital marketing, product launch templates
* **Technical Reports**: Architecture, feasibility study templates

## Future Categories (Available but not implemented)

* **Project Charters**: Project initiation templates
* **Legal Documents**: Contract and legal templates
* **Financial Reports**: Financial analysis templates
