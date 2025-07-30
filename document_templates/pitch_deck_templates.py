# document_templates/pitch_deck_templates.py
import uuid

PITCH_DECK_TEMPLATES = [
    {
        'id': str(uuid.uuid4()),
        'name': 'Tech Startup Pitch Deck',
        'description': 'Comprehensive pitch deck for technology startups',
        'category': 'pitch_deck',
        'sections': [
            {
                'id': 'problem-solution',
                'title': 'Problem & Solution',
                'description': 'Define problem and solution with compelling narrative',
                'questions': [
                    {
                        'id': 'problem-statement',
                        'text': 'What problem are you solving?',
                        'type': 'textarea',
                        'sample_answer': 'Tell a story about a real person experiencing this problem. For example: "Sarah, a busy marketing manager, spends 3 hours every week manually creating reports from 5 different tools, missing strategic work time. This affects 67% of marketing professionals who waste 15+ hours weekly on repetitive data compilation instead of driving growth." Focus on the pain point, quantify the impact, and make it relatable to your target audience.'
                    },
                    {
                        'id': 'solution-overview',
                        'text': 'How does your solution address this problem?',
                        'type': 'textarea',
                        'sample_answer': 'Our AI-powered analytics platform automatically aggregates data from multiple marketing tools and generates comprehensive reports in under 2 minutes. Key differentiators: 1) One-click integration with 50+ marketing platforms, 2) AI-driven insights that identify growth opportunities, 3) Real-time collaboration features for team alignment. This saves marketing teams 15+ hours weekly while improving decision-making speed by 300%.'
                    },
                    {
                        'id': 'unique-value-proposition',
                        'text': 'What makes your solution unique?',
                        'type': 'textarea',
                        'sample_answer': 'Unlike existing solutions that require technical setup and only offer basic reporting, we provide: 1) Zero-code implementation in under 5 minutes, 2) Predictive analytics that forecast campaign performance 30 days ahead, 3) Built-in A/B testing recommendations. Our proprietary ML algorithm processes 10M+ data points to deliver actionable insights that increase marketing ROI by an average of 45%.'
                    }
                ]
            },
            {
                'id': 'market-opportunity',
                'title': 'Market Opportunity',
                'description': 'Market size, trends, and opportunity analysis',
                'questions': [
                    {
                        'id': 'market-size',
                        'text': 'What is your total addressable market (TAM)?',
                        'type': 'textarea',
                        'sample_answer': 'The global marketing analytics software market is $4.2B in 2024, growing at 15.6% CAGR. Our TAM: $4.2B (all marketing analytics), SAM: $1.8B (SMB & mid-market companies with 50-500 employees), SOM: $180M (companies spending $50K+ annually on marketing tools). Key market drivers include increased digital marketing spend (+12% YoY), demand for data-driven decisions (+23% adoption), and marketing technology consolidation trends.'
                    }
                ]
            },
            {
                'id': 'business-model',
                'title': 'Business Model',
                'description': 'Revenue model and pricing strategy',
                'questions': [
                    {
                        'id': 'revenue-model',
                        'text': 'How do you generate revenue?',
                        'type': 'textarea',
                        'sample_answer': 'SaaS subscription model with three tiers: Starter ($99/month, up to 5 integrations), Professional ($299/month, unlimited integrations + advanced analytics), Enterprise ($799/month, custom features + dedicated support). Additional revenue streams: Implementation services ($2,500 one-time), Training programs ($500/session), API usage fees ($0.10/1000 calls). Average customer LTV: $18,500, with 89% gross margins.'
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
                'description': 'Software product showcase with key features',
                'questions': [
                    {
                        'id': 'product-features',
                        'text': 'What are your key product features?',
                        'type': 'textarea',
                        'sample_answer': 'Core Platform Features: 1) Unified Dashboard - Real-time view of all marketing metrics with customizable widgets and drag-drop interface, 2) Smart Integrations - Native connectors to 50+ platforms (Google Ads, Facebook, HubSpot, Salesforce) with 2-minute setup, 3) AI Analytics Engine - Predictive modeling that identifies top-performing campaigns and suggests optimization strategies, 4) Automated Reporting - Scheduled reports with executive summaries delivered via email/Slack, 5) Collaboration Tools - Team workspaces, annotation features, and approval workflows. Each feature addresses specific user pain points identified through 200+ customer interviews.'
                    },
                    {
                        'id': 'product-differentiation',
                        'text': 'How does your product differ from competitors?',
                        'type': 'textarea',
                        'sample_answer': 'Competitive Advantages: 1) Setup Speed - 5 minutes vs 2-4 weeks for enterprise solutions, 2) AI-First Approach - Proprietary machine learning models trained on 50M+ marketing campaigns vs basic statistical reporting, 3) User Experience - Designed for marketers, not data scientists (4.8/5 user rating vs industry average 3.2/5), 4) Pricing - 60% less expensive than enterprise alternatives while offering more integrations than budget tools, 5) Customer Success - 24/7 chat support with 2-minute response time and dedicated CSM for Pro+ plans.'
                    },
                    {
                        'id': 'technical-architecture',
                        'text': 'What is your technical infrastructure?',
                        'type': 'textarea',
                        'sample_answer': 'Built on modern cloud-native architecture: 1) Frontend - React.js with TypeScript for responsive web app, mobile-optimized interface, 2) Backend - Node.js microservices architecture on AWS with auto-scaling capabilities, 3) Database - PostgreSQL for transactional data, ClickHouse for analytics workloads, Redis for caching, 4) Security - SOC 2 Type II certified, AES-256 encryption, GDPR compliant, 5) Performance - 99.9% uptime SLA, <500ms API response times, processing 1M+ data points per minute. Infrastructure scales automatically to handle customer growth.'
                    }
                ]
            },
            {
                'id': 'customer-validation',
                'title': 'Customer Validation',
                'description': 'Customer feedback, testimonials, and case studies',
                'questions': [
                    {
                        'id': 'customer-testimonials',
                        'text': 'What do your customers say about your product?',
                        'type': 'textarea',
                        'sample_answer': 'Customer Success Stories: "TechStart Inc reduced report generation time from 8 hours to 15 minutes, allowing our team to focus on strategy instead of data compilation. ROI increased 34% in first quarter." - Sarah Chen, CMO. Key metrics from 50+ customers: 4.8/5 average rating, 92% customer satisfaction score, 87% would recommend to peers. Customer outcomes: Average 67% time savings on reporting, 45% improvement in campaign performance, 23% increase in marketing qualified leads. 89% of customers upgrade to higher plans within 6 months.'
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
                'description': 'Growth metrics and key performance indicators',
                'questions': [
                    {
                        'id': 'key-metrics',
                        'text': 'What are your key traction metrics?',
                        'type': 'textarea',
                        'sample_answer': 'Growth Metrics (Last 24 months): Monthly Recurring Revenue (MRR): $285K (+340% YoY), growing $45K monthly. Annual Recurring Revenue (ARR): $3.4M run rate. Customer Count: 487 active customers (+280% YoY), adding 35-40 new customers monthly. Customer Acquisition Cost (CAC): $1,850, down from $3,200 (improving 42%). Customer Lifetime Value (LTV): $18,500, LTV:CAC ratio of 10:1. Monthly Churn Rate: 3.2% (best-in-class for SMB SaaS). Net Revenue Retention: 118% indicating strong expansion revenue. Gross Margins: 89% with improving unit economics.'
                    },
                    {
                        'id': 'unit-economics',
                        'text': 'What are your unit economics and financial projections?',
                        'type': 'textarea',
                        'sample_answer': 'Unit Economics: Average Revenue Per User (ARPU): $487/month, growing 8% quarterly as customers upgrade tiers. Payback Period: 12 months (industry benchmark: 18 months). Gross Revenue Retention: 97% indicating strong product-market fit. Sales Efficiency: 1.2x LTV:CAC ratio improving to 1.5x target. Financial Projections (Next 3 years): Year 1: $8.5M ARR (+150% growth), Year 2: $21M ARR (+147% growth), Year 3: $45M ARR (+114% growth). Path to profitability: Break-even at $12M ARR (projected Month 18), 25% EBITDA margins by Year 3.'
                    },
                    {
                        'id': 'market-traction',
                        'text': 'What market validation have you achieved?',
                        'type': 'textarea',
                        'sample_answer': 'Market Validation Milestones: Product-Market Fit Indicators: 40%+ organic growth rate, 89% customer satisfaction, 92% would recommend to peers, 35% of new customers from referrals. Partnership Traction: Integration partnerships with HubSpot, Salesforce, Google (driving 23% of new signups). Industry Recognition: "Top 10 Marketing Tech Startups 2024" by TechCrunch, G2 Leader Badge (4.6/5 rating, 150+ reviews). Customer Logos: Notable customers include TechCorp, GrowthCo, StartupX spanning healthcare, fintech, and e-commerce verticals. Geographic Expansion: 23% international customers across UK, Canada, Australia with localized product versions.'
                    },
                    {
                        'id': 'competitive-position',
                        'text': 'How do you compete in the market?',
                        'type': 'textarea',
                        'sample_answer': 'Competitive Positioning: Market share in target segment: 2.3% and growing (+0.8% YoY). Win rate against direct competitors: 67% in head-to-head sales situations. Key differentiators winning deals: 1) 10x faster implementation (5 min vs 50 hours), 2) 40% lower total cost of ownership, 3) Superior user experience (4.8/5 vs 3.2/5 industry average). Competitive moats being built: 1) Network effects from data insights, 2) 50+ pre-built integrations creating switching costs, 3) Proprietary ML algorithms improving with scale, 4) Strong brand recognition in SMB market. Customer acquisition becoming increasingly efficient through product-led growth.'
                    }
                ]
            },
            {
                'id': 'scaling-strategy',
                'title': 'Scaling Strategy',
                'description': 'Growth plans and execution strategy',
                'questions': [
                    {
                        'id': 'growth-strategy',
                        'text': 'How will you scale the business?',
                        'type': 'textarea',
                        'sample_answer': 'Scaling Strategy: 1) Sales Team Expansion: Hire 8 additional AEs and 4 SDRs (current: 3 AEs, 2 SDRs), targeting $85K ARR per rep. Implement sales enablement program and CRM optimization. 2) Product Development: Expand to enterprise segment with advanced features (SSO, advanced permissions, custom integrations). Launch mobile app and API marketplace. 3) Marketing: Scale content marketing (targeting 50K monthly organic visitors), launch partner program, expand conference presence. 4) Geographic Expansion: Open European operations (London office), localize for GDPR compliance, hire regional sales team. Goal: 3x revenue in 24 months through improved efficiency and market expansion.'
                    },
                    {
                        'id': 'team-expansion',
                        'text': 'What are your hiring and team growth plans?',
                        'type': 'textarea',
                        'sample_answer': 'Team Growth Plan (Next 18 months): Current team: 23 employees (8 engineering, 5 sales/marketing, 4 customer success, 6 operations). Hiring roadmap: 1) Engineering: +12 engineers (4 frontend, 4 backend, 2 data scientists, 2 DevOps) to accelerate product development, 2) Sales: +8 account executives, +4 SDRs, +1 sales manager to scale revenue, 3) Customer Success: +3 CSMs, +2 support specialists to maintain high NPS, 4) Operations: +1 CFO, +2 people ops, +1 legal counsel for scaling infrastructure. Key leadership hires: VP of Engineering (Q2), VP of Sales (Q3), Head of International (Q4). Target team size: 55 employees by end of Year 2.'
                    }
                ]
            },
            {
                'id': 'funding-ask',
                'title': 'Funding Ask',
                'description': 'Investment requirements and use of funds',
                'questions': [
                    {
                        'id': 'funding-amount',
                        'text': 'How much funding are you seeking?',
                        'type': 'textarea',
                        'sample_answer': 'Funding Request: $12M Series A to accelerate growth and market expansion. Use of Funds Breakdown: 1) Team Expansion (60% - $7.2M): Engineering team scaling, sales team growth, key leadership hires, 2) Product Development (20% - $2.4M): Enterprise features, mobile app, API platform, security enhancements, 3) Marketing & Sales (15% - $1.8M): Lead generation, conference presence, content marketing, sales enablement tools, 4) Operations & Infrastructure (5% - $600K): Office expansion, legal, compliance, financial systems. Timeline: 24-month runway to reach $25M ARR and profitability. Expected ROI: 5-8x return for investors based on comparable market exits.'
                    },
                    {
                        'id': 'investor-value',
                        'text': 'What value do you bring to investors?',
                        'type': 'textarea',
                        'sample_answer': 'Investment Opportunity: Market Opportunity: $4.2B growing at 15.6% CAGR with clear path to capture $180M serviceable market. Strong Unit Economics: 10:1 LTV:CAC ratio, 89% gross margins, 12-month payback period improving quarterly. Experienced Team: Combined 45+ years experience at Google, Salesforce, HubSpot with 2 previous successful exits totaling $340M. Proven Traction: $3.4M ARR with 340% YoY growth, strong customer retention, expanding into enterprise segment. Exit Potential: Comparable companies (ChartIO acquired for $200M, Looker for $2.6B) validate market opportunity. Conservative exit projection: $150-300M in 5-7 years based on revenue multiples and growth trajectories.'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'B2B Enterprise Pitch Deck',
        'description': 'Pitch deck template for B2B enterprise solutions',
        'category': 'pitch_deck',
        'sections': [
            {
                'id': 'enterprise-problem',
                'title': 'Enterprise Problem Statement',
                'description': 'Large-scale business problems and pain points',
                'questions': [
                    {
                        'id': 'enterprise-pain-points',
                        'text': 'What enterprise-level problems are you solving?',
                        'type': 'textarea',
                        'sample_answer': 'Enterprise Challenge: Fortune 500 companies lose $2.3M annually per 1,000 employees due to inefficient internal processes and disconnected systems. Key pain points: 1) Data Silos - Critical business data trapped in 15+ systems with no unified view, 2) Manual Processes - 67% of enterprise workflows still require manual intervention, costing 35 hours per employee monthly, 3) Compliance Risk - 89% of enterprises struggle with audit trails and regulatory compliance across distributed systems, 4) Security Gaps - Integration challenges create security vulnerabilities and access control issues. This impacts 85% of Global 2000 companies seeking digital transformation solutions.'
                    }
                ]
            },
            {
                'id': 'enterprise-solution',
                'title': 'Enterprise Solution',
                'description': 'Scalable solution for large organizations',
                'questions': [
                    {
                        'id': 'enterprise-features',
                        'text': 'What enterprise-grade features do you offer?',
                        'type': 'textarea',
                        'sample_answer': 'Enterprise Platform Features: 1) Unified Data Platform - Single source of truth connecting 200+ enterprise systems with real-time synchronization, 2) AI-Powered Automation - Intelligent workflow engine automating 80% of routine processes with approval chains, 3) Enterprise Security - SOC 2 Type II, ISO 27001, GDPR compliant with zero-trust architecture and SSO integration, 4) Advanced Analytics - Executive dashboards with predictive insights and custom KPI tracking, 5) White-Glove Implementation - Dedicated customer success team with 6-month onboarding program. Platform processes 100M+ transactions daily with 99.99% uptime SLA.'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Pre-Seed Pitch Deck',
        'description': 'Early-stage pitch deck for pre-seed funding',
        'category': 'pitch_deck',
        'sections': [
            {
                'id': 'early-stage-traction',
                'title': 'Early Traction',
                'description': 'Early validation and initial metrics',
                'questions': [
                    {
                        'id': 'early-metrics',
                        'text': 'What early traction have you achieved?',
                        'type': 'textarea',
                        'sample_answer': 'Early Validation Metrics: Beta User Engagement: 150 beta users with 78% weekly active usage, average session time 23 minutes. Customer Discovery: 200+ customer interviews validating core problem, 67% said they would pay for solution immediately. Waitlist Growth: 1,200 potential customers on waitlist growing 15% weekly through organic referrals. MVP Performance: 4.2/5 user rating, 89% would recommend to colleagues, key feature adoption rate 94%. Market Validation: 3 pilot customers committed to 6-month paid pilots ($2,500 each), 12 additional prospects in advanced discussions. Social Proof: Featured in TechCrunch, 500+ LinkedIn followers, 85% positive feedback on ProductHunt soft launch.'
                    }
                ]
            }
        ]
    }
]

# Additional helper functions for template management
def get_template_by_category(category):
    """Return all templates for a specific category"""
    return [template for template in PITCH_DECK_TEMPLATES if template['category'] == category]

def get_template_by_id(template_id):
    """Return a specific template by ID"""
    return next((template for template in PITCH_DECK_TEMPLATES if template['id'] == template_id), None)

def get_all_categories():
    """Return all unique categories"""
    return list(set(template['category'] for template in PITCH_DECK_TEMPLATES))

# Template validation
def validate_template_structure(template):
    """Validate that a template has all required fields"""
    required_fields = ['id', 'name', 'description', 'category', 'sections']
    section_required_fields = ['id', 'title', 'description', 'questions']
    question_required_fields = ['id', 'text', 'type', 'sample_answer']
    
    # Validate template level
    for field in required_fields:
        if field not in template:
            return False, f"Missing required field: {field}"
    
    # Validate sections
    for section in template['sections']:
        for field in section_required_fields:
            if field not in section:
                return False, f"Section missing required field: {field}"
        
        # Validate questions
        for question in section['questions']:
            for field in question_required_fields:
                if field not in question:
                    return False, f"Question missing required field: {field}"
    
    return True, "Template structure is valid"
