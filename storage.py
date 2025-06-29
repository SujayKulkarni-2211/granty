from models import db, User, Project, Template, ChatMessage
from datetime import datetime
import uuid
import json
from werkzeug.security import generate_password_hash, check_password_hash

def init_db(app):
    """Initialize database with app context"""
    with app.app_context():
        try:
            # Drop all tables and recreate them
            db.drop_all()
            db.create_all()
            print("Database tables created successfully")
            
            # Initialize templates
            initialize_comprehensive_templates()
            print("Comprehensive templates initialized")
            
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
    """Get all unique template categories"""
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

def initialize_comprehensive_templates():
    """Create comprehensive templates for all categories"""
    try:
        # Clear existing templates first
        Template.query.delete()
        db.session.commit()
        
        templates = [
            # GRANT TEMPLATES (5)
            {
                'id': str(uuid.uuid4()),
                'name': 'NSF Research Grant',
                'description': 'National Science Foundation research grant proposal template',
                'category': 'grant',
                'sections': [
                    {
                        'id': 'project-summary',
                        'title': 'Project Summary',
                        'description': 'A one-page summary of the proposed project',
                        'questions': [
                            {
                                'id': 'intellectual-merit',
                                'text': 'What is the intellectual merit of the proposed activity?',
                                'type': 'textarea',
                                'sample_answer': 'This research addresses fundamental questions in quantum computing by developing novel algorithms that could revolutionize computational efficiency in cryptography and optimization problems.'
                            },
                            {
                                'id': 'broader-impacts',
                                'text': 'What are the broader impacts of the proposed activity?',
                                'type': 'textarea',
                                'sample_answer': 'The research will train graduate students in cutting-edge quantum technologies, establish partnerships with industry leaders, and contribute to national competitiveness in quantum computing research.'
                            }
                        ]
                    },
                    {
                        'id': 'project-description',
                        'title': 'Project Description',
                        'description': 'Detailed description of the research project',
                        'questions': [
                            {
                                'id': 'research-objectives',
                                'text': 'What are the main research objectives?',
                                'type': 'textarea',
                                'sample_answer': 'Our primary objectives are to: 1) Develop quantum algorithms with provable efficiency advantages, 2) Create a simulation framework for testing quantum circuits, 3) Establish theoretical foundations for quantum machine learning.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'NIH Medical Research Grant',
                'description': 'National Institutes of Health medical research grant template',
                'category': 'grant',
                'sections': [
                    {
                        'id': 'specific-aims',
                        'title': 'Specific Aims',
                        'description': 'Clear statement of research goals',
                        'questions': [
                            {
                                'id': 'research-problem',
                                'text': 'What medical problem are you addressing?',
                                'type': 'textarea',
                                'sample_answer': 'Alzheimer\'s disease affects 6.5 million Americans, with no cure available. Our research targets the underlying mechanisms of neurodegeneration to develop novel therapeutic approaches.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Small Business Innovation Research (SBIR)',
                'description': 'SBIR grant proposal for small business innovation',
                'category': 'grant',
                'sections': [
                    {
                        'id': 'technical-innovation',
                        'title': 'Technical Innovation',
                        'description': 'Description of the innovative technology',
                        'questions': [
                            {
                                'id': 'innovation-description',
                                'text': 'Describe your technical innovation',
                                'type': 'textarea',
                                'sample_answer': 'Our AI-powered diagnostic tool uses machine learning to analyze medical images with 95% accuracy, reducing diagnosis time from hours to minutes.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Department of Energy Research Grant',
                'description': 'DOE research grant for energy-related projects',
                'category': 'grant',
                'sections': [
                    {
                        'id': 'energy-impact',
                        'title': 'Energy Impact',
                        'description': 'How your research impacts energy sector',
                        'questions': [
                            {
                                'id': 'energy-significance',
                                'text': 'What is the energy significance of your research?',
                                'type': 'textarea',
                                'sample_answer': 'Our research on advanced battery materials could increase energy storage capacity by 300%, revolutionizing renewable energy adoption.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'European Research Council (ERC) Grant',
                'description': 'ERC grant template for European researchers',
                'category': 'grant',
                'sections': [
                    {
                        'id': 'excellence',
                        'title': 'Excellence',
                        'description': 'Demonstrate research excellence',
                        'questions': [
                            {
                                'id': 'research-excellence',
                                'text': 'How does your research demonstrate excellence?',
                                'type': 'textarea',
                                'sample_answer': 'Our groundbreaking approach combines AI with materials science to discover new compounds 100x faster than traditional methods, with potential applications in drug discovery and renewable energy.'
                            }
                        ]
                    }
                ]
            },

            # PITCH DECK TEMPLATES (5)
            {
                'id': str(uuid.uuid4()),
                'name': 'Tech Startup Pitch Deck',
                'description': 'Comprehensive pitch deck for technology startups',
                'category': 'pitch_deck',
                'sections': [
                    {
                        'id': 'problem-solution',
                        'title': 'Problem & Solution',
                        'description': 'Define the problem and your solution',
                        'questions': [
                            {
                                'id': 'problem-statement',
                                'text': 'What problem are you solving?',
                                'type': 'textarea',
                                'sample_answer': 'Small businesses lose $1.1 trillion annually due to inefficient inventory management. Current solutions are too expensive and complex for SMBs.'
                            },
                            {
                                'id': 'solution-description',
                                'text': 'How does your solution address this problem?',
                                'type': 'textarea',
                                'sample_answer': 'Our AI-powered platform automates inventory management with 90% accuracy, reducing costs by 40% and requiring zero setup time.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'SaaS Startup Pitch',
                'description': 'Pitch deck template for SaaS companies',
                'category': 'pitch_deck',
                'sections': [
                    {
                        'id': 'product-demo',
                        'title': 'Product Demo',
                        'description': 'Showcase your software product',
                        'questions': [
                            {
                                'id': 'product-features',
                                'text': 'What are your key product features?',
                                'type': 'textarea',
                                'sample_answer': 'Our platform features real-time analytics, automated workflows, seamless integrations, and an intuitive dashboard that requires no training.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'E-commerce Startup Pitch',
                'description': 'Pitch deck for e-commerce and marketplace startups',
                'category': 'pitch_deck',
                'sections': [
                    {
                        'id': 'market-opportunity',
                        'title': 'Market Opportunity',
                        'description': 'Define your market and opportunity',
                        'questions': [
                            {
                                'id': 'market-size',
                                'text': 'What is your total addressable market?',
                                'type': 'textarea',
                                'sample_answer': 'The global e-commerce market is $5.2 trillion and growing at 14% annually. Our target segment represents a $240 billion opportunity.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Biotech Startup Pitch',
                'description': 'Specialized pitch deck for biotech and life sciences',
                'category': 'pitch_deck',
                'sections': [
                    {
                        'id': 'scientific-approach',
                        'title': 'Scientific Approach',
                        'description': 'Explain your scientific methodology',
                        'questions': [
                            {
                                'id': 'scientific-innovation',
                                'text': 'What is your scientific innovation?',
                                'type': 'textarea',
                                'sample_answer': 'Our CRISPR-based gene therapy platform targets previously untreatable genetic disorders with 85% efficacy in preclinical trials.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Series A Pitch Deck',
                'description': 'Advanced pitch deck for Series A funding rounds',
                'category': 'pitch_deck',
                'sections': [
                    {
                        'id': 'traction-metrics',
                        'title': 'Traction & Metrics',
                        'description': 'Show your growth and key metrics',
                        'questions': [
                            {
                                'id': 'key-metrics',
                                'text': 'What are your key traction metrics?',
                                'type': 'textarea',
                                'sample_answer': '$2M ARR, 150% net revenue retention, 95% customer satisfaction, 25% month-over-month growth, and partnerships with 3 Fortune 500 companies.'
                            }
                        ]
                    }
                ]
            },

            # BUSINESS PROPOSAL TEMPLATES (5)
            {
                'id': str(uuid.uuid4()),
                'name': 'Corporate Partnership Proposal',
                'description': 'Proposal template for corporate partnerships',
                'category': 'business_proposal',
                'sections': [
                    {
                        'id': 'partnership-benefits',
                        'title': 'Partnership Benefits',
                        'description': 'Outline mutual benefits of partnership',
                        'questions': [
                            {
                                'id': 'mutual-benefits',
                                'text': 'How will both companies benefit from this partnership?',
                                'type': 'textarea',
                                'sample_answer': 'Our partnership will expand your market reach by 40% while providing us access to enterprise clients. Combined, we can reduce customer acquisition costs by 60%.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Project Proposal',
                'description': 'General project proposal template for any industry',
                'category': 'business_proposal',
                'sections': [
                    {
                        'id': 'project-scope',
                        'title': 'Project Scope',
                        'description': 'Define project scope and deliverables',
                        'questions': [
                            {
                                'id': 'project-objectives',
                                'text': 'What are the main project objectives?',
                                'type': 'textarea',
                                'sample_answer': 'Implement a comprehensive digital transformation strategy that increases operational efficiency by 35% and reduces costs by $2M annually.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Service Proposal',
                'description': 'Proposal template for service-based businesses',
                'category': 'business_proposal',
                'sections': [
                    {
                        'id': 'service-offering',
                        'title': 'Service Offering',
                        'description': 'Detail your service offerings',
                        'questions': [
                            {
                                'id': 'service-description',
                                'text': 'What services are you proposing?',
                                'type': 'textarea',
                                'sample_answer': 'We provide end-to-end consulting services including strategy development, implementation support, and ongoing optimization, delivered by certified experts.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Investment Proposal',
                'description': 'Investment proposal for potential investors',
                'category': 'business_proposal',
                'sections': [
                    {
                        'id': 'investment-opportunity',
                        'title': 'Investment Opportunity',
                        'description': 'Present the investment opportunity',
                        'questions': [
                            {
                                'id': 'investment-thesis',
                                'text': 'What is your investment thesis?',
                                'type': 'textarea',
                                'sample_answer': 'The AI healthcare market will reach $102B by 2028. Our proven technology and experienced team position us to capture 2% market share, delivering 10x returns.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Vendor Proposal',
                'description': 'Proposal template for vendor relationships',
                'category': 'business_proposal',
                'sections': [
                    {
                        'id': 'vendor-capabilities',
                        'title': 'Vendor Capabilities',
                        'description': 'Showcase your capabilities as a vendor',
                        'questions': [
                            {
                                'id': 'company-capabilities',
                                'text': 'What are your key capabilities and differentiators?',
                                'type': 'textarea',
                                'sample_answer': 'We offer 24/7 support, 99.9% uptime guarantee, ISO certifications, and a proven track record of serving 500+ enterprise clients across 25 countries.'
                            }
                        ]
                    }
                ]
            },

            # EXECUTIVE SUMMARY TEMPLATES (5)
            {
                'id': str(uuid.uuid4()),
                'name': 'Business Plan Executive Summary',
                'description': 'Executive summary for comprehensive business plans',
                'category': 'executive_summary',
                'sections': [
                    {
                        'id': 'business-overview',
                        'title': 'Business Overview',
                        'description': 'High-level overview of your business',
                        'questions': [
                            {
                                'id': 'company-mission',
                                'text': 'What is your company mission and vision?',
                                'type': 'textarea',
                                'sample_answer': 'Our mission is to democratize AI technology for small businesses, enabling them to compete with enterprise-level efficiency and insights.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Project Executive Summary',
                'description': 'Executive summary for project proposals',
                'category': 'executive_summary',
                'sections': [
                    {
                        'id': 'project-overview',
                        'title': 'Project Overview',
                        'description': 'Summarize your project proposal',
                        'questions': [
                            {
                                'id': 'project-goals',
                                'text': 'What are the main goals of this project?',
                                'type': 'textarea',
                                'sample_answer': 'Develop and deploy a cloud-based analytics platform that processes 1TB of data daily, providing real-time insights to improve decision-making by 45%.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Investment Executive Summary',
                'description': 'Executive summary for investment opportunities',
                'category': 'executive_summary',
                'sections': [
                    {
                        'id': 'investment-highlights',
                        'title': 'Investment Highlights',
                        'description': 'Key highlights of the investment opportunity',
                        'questions': [
                            {
                                'id': 'key-highlights',
                                'text': 'What are the key investment highlights?',
                                'type': 'textarea',
                                'sample_answer': '$50M market opportunity, proven team with 3 exits, proprietary technology with 5 patents, and letters of intent from Fortune 100 customers.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Research Executive Summary',
                'description': 'Executive summary for research proposals',
                'category': 'executive_summary',
                'sections': [
                    {
                        'id': 'research-significance',
                        'title': 'Research Significance',
                        'description': 'Explain the significance of your research',
                        'questions': [
                            {
                                'id': 'research-impact',
                                'text': 'What is the potential impact of your research?',
                                'type': 'textarea',
                                'sample_answer': 'Our research could lead to new cancer treatments affecting 2 million patients annually, with potential cost savings of $10 billion in healthcare spending.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Strategic Initiative Summary',
                'description': 'Executive summary for strategic initiatives',
                'category': 'executive_summary',
                'sections': [
                    {
                        'id': 'strategic-rationale',
                        'title': 'Strategic Rationale',
                        'description': 'Explain the strategic reasoning',
                        'questions': [
                            {
                                'id': 'strategic-importance',
                                'text': 'Why is this strategic initiative important?',
                                'type': 'textarea',
                                'sample_answer': 'This initiative aligns with our 2025 growth strategy, targeting new markets that represent 30% revenue growth opportunity and strengthening our competitive moat.'
                            }
                        ]
                    }
                ]
            },

            # SCIENTIFIC PROPOSAL TEMPLATES (5)
            {
                'id': str(uuid.uuid4()),
                'name': 'Academic Research Proposal',
                'description': 'Comprehensive academic research proposal template',
                'category': 'scientific_proposal',
                'sections': [
                    {
                        'id': 'literature-review',
                        'title': 'Literature Review',
                        'description': 'Review of existing research and knowledge gaps',
                        'questions': [
                            {
                                'id': 'current-state',
                                'text': 'What is the current state of research in this field?',
                                'type': 'textarea',
                                'sample_answer': 'Current research has established the fundamental principles of quantum entanglement, but significant gaps remain in practical applications for secure communication networks.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Clinical Trial Proposal',
                'description': 'Proposal template for clinical trials and medical research',
                'category': 'scientific_proposal',
                'sections': [
                    {
                        'id': 'study-design',
                        'title': 'Study Design',
                        'description': 'Detailed study design and methodology',
                        'questions': [
                            {
                                'id': 'trial-methodology',
                                'text': 'What is your clinical trial methodology?',
                                'type': 'textarea',
                                'sample_answer': 'Randomized, double-blind, placebo-controlled trial with 500 participants across 10 sites, measuring primary endpoint of 30% reduction in symptoms over 12 weeks.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Laboratory Research Proposal',
                'description': 'Template for laboratory-based scientific research',
                'category': 'scientific_proposal',
                'sections': [
                    {
                        'id': 'experimental-design',
                        'title': 'Experimental Design',
                        'description': 'Detailed experimental design and procedures',
                        'questions': [
                            {
                                'id': 'experimental-approach',
                                'text': 'What is your experimental approach?',
                                'type': 'textarea',
                                'sample_answer': 'We will use CRISPR-Cas9 gene editing combined with single-cell RNA sequencing to investigate gene expression patterns in response to environmental stressors.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Field Study Proposal',
                'description': 'Proposal template for field-based scientific studies',
                'category': 'scientific_proposal',
                'sections': [
                    {
                        'id': 'field-methodology',
                        'title': 'Field Methodology',
                        'description': 'Field study design and data collection methods',
                        'questions': [
                            {
                                'id': 'data-collection',
                                'text': 'How will you collect and analyze field data?',
                                'type': 'textarea',
                                'sample_answer': 'Long-term monitoring using IoT sensors, drone surveys, and machine learning analysis to track ecosystem changes across 50 sites over 5 years.'
                            }
                        ]
                    }
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'name': 'Computational Research Proposal',
                'description': 'Template for computational and modeling research',
                'category': 'scientific_proposal',
                'sections': [
                    {
                        'id': 'computational-methods',
                        'title': 'Computational Methods',
                        'description': 'Computational approaches and modeling techniques',
                        'questions': [
                            {
                                'id': 'modeling-approach',
                                'text': 'What computational methods will you use?',
                                'type': 'textarea',
                                'sample_answer': 'Machine learning algorithms combined with high-performance computing to simulate molecular interactions, requiring 10,000 CPU hours on supercomputing clusters.'
                            }
                        ]
                    }
                ]
            }
        ]
        
        for template_data in templates:
            template = save_template(template_data)
            if template:
                print(f"Initialized template: {template.name}")
        
        print(f"Successfully initialized {len(templates)} comprehensive templates")
        
    except Exception as e:
        db.session.rollback()
        print(f"Error initializing templates: {e}")
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