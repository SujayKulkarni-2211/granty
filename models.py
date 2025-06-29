from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, timedelta
import json
import uuid

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    # Email verification fields
    is_email_verified = db.Column(db.Boolean, default=False)
    email_verification_token = db.Column(db.String(255), unique=True, nullable=True)
    email_verification_sent_at = db.Column(db.DateTime, nullable=True)
    
    # Relationships
    projects = db.relationship('Project', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def get_project_count(self):
        return len(self.projects)
    
    def can_create_project(self):
        from config import MAX_PROJECTS_PER_USER
        return self.get_project_count() < MAX_PROJECTS_PER_USER
    
    def is_verification_token_valid(self):
        """Check if verification token is still valid (24 hours)"""
        if not self.email_verification_sent_at:
            return False
        return datetime.utcnow() - self.email_verification_sent_at < timedelta(hours=24)
    
    def generate_verification_token(self):
        """Generate and set verification token"""
        import secrets
        self.email_verification_token = secrets.token_urlsafe(32)
        self.email_verification_sent_at = datetime.utcnow()
        return self.email_verification_token

class Project(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    project_type = db.Column(db.String(50), nullable=False)  # grant, pitch_deck, business_proposal, etc.
    template_id = db.Column(db.String(36), nullable=False)
    sections = db.Column(db.Text, nullable=False)  # JSON string
    answers = db.Column(db.Text, default='{}')  # JSON string
    generated_content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign key
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=True)  # nullable for guest mode
    
    def get_sections(self):
        return json.loads(self.sections) if self.sections else []
    
    def set_sections(self, sections_data):
        self.sections = json.dumps(sections_data)
    
    def get_answers(self):
        return json.loads(self.answers) if self.answers else {}
    
    def set_answers(self, answers_data):
        self.answers = json.dumps(answers_data)

class Template(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50), nullable=False)  # grant, pitch_deck, business_proposal, etc.
    sections = db.Column(db.Text, nullable=False)  # JSON string
    is_premium = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def get_sections(self):
        return json.loads(self.sections) if self.sections else []
    
    def set_sections(self, sections_data):
        self.sections = json.dumps(sections_data)

class ChatMessage(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = db.Column(db.String(36), db.ForeignKey('project.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    project = db.relationship('Project', backref='chat_messages')
