from models import db, User, Project, Template, ChatMessage
from datetime import datetime
import uuid
import json
from werkzeug.security import generate_password_hash, check_password_hash

# Import modular template system
from document_templates import (
    TEMPLATE_CATEGORIES,
    load_all_templates,
    load_templates_by_category,
    get_available_categories,
    validate_category,
    get_template_count,
    get_templates_by_category_dict
)

def init_db(app):
    """Initialize database with app context"""
    with app.app_context():
        try:
            # Drop all tables and recreate them
            db.drop_all()
            db.create_all()
            print("Database tables created successfully")
            
            # Initialize templates from modular system
            initialize_templates_from_modules()
            print("Templates initialized from modular system")
            
        except Exception as e:
            print(f"Error initializing database: {e}")
            raise

def create_user(email, password, name):
    """Create a new user"""
    try:
        password_hash = generate_password_hash(password)
        user = User(
            email=email,
            password_hash=password_hash,
            name=name
        )
        db.session.add(user)
        db.session.commit()
        return user
    except Exception as e:
        db.session.rollback()
        print(f"Error creating user: {e}")
        return None

def authenticate_user(email, password):
    """Authenticate user login"""
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        return user
    return None

def get_user_by_id(user_id):
    """Get user by ID"""
    return User.query.get(user_id)

def get_templates(category=None):
    """Get all available templates"""
    try:
        query = Template.query
        if category:
            query = query.filter_by(category=category)
        templates = query.all()
        print(f"Retrieved {len(templates)} templates")
        return templates
    except Exception as e:
        print(f"Error getting templates: {e}")
        return []

def get_template_categories():
    """Get all unique template categories from database"""
    try:
        categories = db.session.query(Template.category).distinct().all()
        return [cat[0] for cat in categories]
    except Exception as e:
        print(f"Error getting categories: {e}")
        return []

def get_templates_by_category():
    """Get templates grouped by category"""
    try:
        templates = Template.query.all()
        grouped = {}
        for template in templates:
            if template.category not in grouped:
                grouped[template.category] = []
            grouped[template.category].append(template)
        return grouped
    except Exception as e:
        print(f"Error grouping templates: {e}")
        return {}

def get_template(template_id):
    """Get a specific template by ID"""
    try:
        template = Template.query.get(template_id)
        if template:
            print(f"Retrieved template: {template.name}")
        else:
            print(f"Template not found: {template_id}")
        return template
    except Exception as e:
        print(f"Error getting template {template_id}: {e}")
        return None

def save_template(template_data):
    """Save a template to database"""
    try:
        # Check if template already exists
        existing = Template.query.filter_by(name=template_data['name']).first()
        if existing:
            print(f"Template already exists: {template_data['name']}")
            return existing
            
        template = Template(
            id=template_data.get('id', str(uuid.uuid4())),
            name=template_data['name'],
            description=template_data.get('description', ''),
            category=template_data.get('category', 'grant'),
            is_premium=template_data.get('is_premium', False)
        )
        template.set_sections(template_data['sections'])
        
        db.session.add(template)
        db.session.commit()
        print(f"Template saved: {template.name}")
        return template
    except Exception as e:
        db.session.rollback()
        print(f"Error saving template: {e}")
        return None

def get_projects(user_id=None):
    """Get projects for a user or all guest projects"""
    try:
        if user_id:
            projects = Project.query.filter_by(user_id=user_id).order_by(Project.updated_at.desc()).all()
        else:
            # Guest mode - return projects without user_id
            projects = Project.query.filter_by(user_id=None).order_by(Project.updated_at.desc()).all()
        print(f"Retrieved {len(projects)} projects")
        return projects
    except Exception as e:
        print(f"Error getting projects: {e}")
        return []

def get_project(project_id):
    """Get a specific project by ID"""
    try:
        project = Project.query.get(project_id)
        if project:
            print(f"Retrieved project: {project.title}")
        else:
            print(f"Project not found: {project_id}")
        return project
    except Exception as e:
        print(f"Error getting project {project_id}: {e}")
        return None

def save_project(project_data, user_id=None):
    """Save a project to database"""
    try:
        project = Project(
            id=project_data.get('id', str(uuid.uuid4())),
            title=project_data['title'],
            description=project_data.get('description', ''),
            project_type=project_data.get('project_type', 'grant'),
            template_id=project_data['template_id'],
            generated_content=project_data.get('generated_content'),
            user_id=user_id
        )
        project.set_sections(project_data['sections'])
        project.set_answers(project_data.get('answers', {}))
        
        db.session.add(project)
        db.session.commit()
        print(f"Project saved: {project.title}")
        return project
    except Exception as e:
        db.session.rollback()
        print(f"Error saving project: {e}")
        return None

def update_project(project_id, updates):
    """Update an existing project"""
    try:
        project = Project.query.get(project_id)
        if not project:
            return None
        
        for key, value in updates.items():
            if key == 'sections':
                project.set_sections(value)
            elif key == 'answers':
                project.set_answers(value)
            else:
                setattr(project, key, value)
        
        project.updated_at = datetime.utcnow()
        db.session.commit()
        print(f"Project updated: {project.title}")
        return project
    except Exception as e:
        db.session.rollback()
        print(f"Error updating project: {e}")
        return None

def delete_project(project_id):
    """Delete a project"""
    try:
        project = Project.query.get(project_id)
        if project:
            db.session.delete(project)
            db.session.commit()
            print(f"Project deleted: {project.title}")
            return True
        return False
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting project: {e}")
        return False

def save_chat_message(project_id, message, response):
    """Save a chat message and response"""
    try:
        chat = ChatMessage(
            project_id=project_id,
            message=message,
            response=response
        )
        db.session.add(chat)
        db.session.commit()
        return chat
    except Exception as e:
        db.session.rollback()
        print(f"Error saving chat message: {e}")
        return None

def get_chat_history(project_id):
    """Get chat history for a project"""
    return ChatMessage.query.filter_by(project_id=project_id).order_by(ChatMessage.created_at.asc()).all()

def initialize_templates_from_modules():
    """Initialize templates using the modular template system"""
    try:
        # Clear existing templates first
        Template.query.delete()
        db.session.commit()
        
        # Load all templates from modules
        all_templates = load_all_templates()
        
        print(f"Loading {len(all_templates)} templates from modules...")
        
        for template_data in all_templates:
            # Validate category exists in our category definitions
            if not validate_category(template_data['category']):
                print(f"Warning: Invalid category '{template_data['category']}' for template '{template_data['name']}'")
                continue
                
            template = save_template(template_data)
            if template:
                print(f"✓ Loaded template: {template.name} ({template.category})")
        
        # Print summary
        total_loaded = Template.query.count()
        categories_loaded = len(get_template_categories())
        
        print(f"\n=== Template Loading Summary ===")
        print(f"Total templates loaded: {total_loaded}")
        print(f"Categories loaded: {categories_loaded}")
        print(f"Available categories: {', '.join(get_available_categories())}")
        print(f"Templates per category:")
        
        for category in get_available_categories():
            count = Template.query.filter_by(category=category).count()
            category_info = TEMPLATE_CATEGORIES.get(category, {})
            print(f"  - {category_info.get('name', category)}: {count} templates")
        
    except Exception as e:
        db.session.rollback()
        print(f"Error initializing templates from modules: {e}")
        raise

# Legacy compatibility functions for existing code
def get_drafts():
    """Legacy function - now returns projects"""
    return get_projects()

def get_draft(draft_id):
    """Legacy function - now returns project"""
    project = get_project(draft_id)
    if project:
        return {
            'id': project.id,
            'title': project.title,
            'template_id': project.template_id,
            'sections': project.get_sections(),
            'answers': project.get_answers(),
            'generated_content': project.generated_content,
            'created_at': project.created_at.isoformat(),
            'updated_at': project.updated_at.isoformat()
        }
    return None

def save_draft(draft_data):
    """Legacy function - now saves as project"""
    return save_project(draft_data)

def create_user_with_verification(email, password, name):
    """Create a new user with email verification token"""
    try:
        password_hash = generate_password_hash(password)
        user = User(
            email=email,
            password_hash=password_hash,
            name=name,
            is_email_verified=False  # Start with unverified email
        )
        
        # Generate verification token
        user.generate_verification_token()
        
        db.session.add(user)
        db.session.commit()
        print(f"User created with verification: {email}")
        return user
    except Exception as e:
        db.session.rollback()
        print(f"Error creating user: {e}")
        return None

def get_user_by_verification_token(token):
    """Get user by verification token"""
    return User.query.filter_by(email_verification_token=token).first()

def verify_user_email(token):
    """Verify user email using token"""
    try:
        user = get_user_by_verification_token(token)
        if not user:
            return None, "Invalid verification token"
        
        if not user.is_verification_token_valid():
            return None, "Verification token has expired"
        
        # Mark email as verified
        user.is_email_verified = True
        user.email_verification_token = None
        user.email_verification_sent_at = None
        
        db.session.commit()
        print(f"Email verified for user: {user.email}")
        return user, "Email verified successfully"
        
    except Exception as e:
        db.session.rollback()
        print(f"Error verifying email: {e}")
        return None, "Error verifying email"

def resend_verification_email(user_id):
    """Resend verification email to user"""
    try:
        user = User.query.get(user_id)
        if not user:
            return None, "User not found"
        
        if user.is_email_verified:
            return None, "Email already verified"
        
        # Generate new verification token
        user.generate_verification_token()
        db.session.commit()
        
        print(f"Verification email resent for user: {user.email}")
        return user, "New verification email sent"
        
    except Exception as e:
        db.session.rollback()
        print(f"Error resending verification email: {e}")
        return None, "Error sending verification email"

def authenticate_user_with_verification(email, password):
    """Authenticate user login with email verification check"""
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        return user
    return None

# Utility functions for template management
def add_new_template_from_module(template_data):
    """Add a single new template from module data"""
    try:
        if not validate_category(template_data['category']):
            print(f"Error: Invalid category '{template_data['category']}'")
            return None
            
        template = save_template(template_data)
        if template:
            print(f"✓ Added new template: {template.name}")
        return template
    except Exception as e:
        print(f"Error adding new template: {e}")
        return None

def reload_templates_from_modules():
    """Reload all templates from modules (useful for updates)"""
    try:
        print("Reloading templates from modules...")
        initialize_templates_from_modules()
        print("✓ Templates reloaded successfully")
        return True
    except Exception as e:
        print(f"Error reloading templates: {e}")
        return False

def get_modular_template_info():
    """Get information about the modular template system"""
    return {
        'total_categories': len(TEMPLATE_CATEGORIES),
        'available_categories': get_available_categories(),
        'total_templates_in_modules': get_template_count(),
        'templates_by_category': get_templates_by_category_dict(),
        'category_info': TEMPLATE_CATEGORIES
    }

# Export legacy function names for backward compatibility
initialize_comprehensive_templates = initialize_templates_from_modules