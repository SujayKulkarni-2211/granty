# document_templates/business_proposal_templates.py
import uuid

BUSINESS_PROPOSAL_TEMPLATES = [
    {
        'id': str(uuid.uuid4()),
        'name': 'Corporate Partnership Proposal',
        'description': 'Comprehensive proposal template for strategic corporate partnerships and alliances',
        'category': 'business_proposal',
        'sections': [
            {
                'id': 'executive-summary',
                'title': 'Executive Summary',
                'description': 'High-level overview of the partnership opportunity',
                'questions': [
                    {
                        'id': 'partnership-vision',
                        'text': 'What is the overall vision for this partnership?',
                        'type': 'textarea',
                        'sample_answer': 'Our partnership will create a strategic alliance that combines your market leadership with our innovative technology platform, targeting a $500M market opportunity in digital transformation services.'
                    },
                    {
                        'id': 'key-benefits',
                        'text': 'What are the top 3 key benefits for both organizations?',
                        'type': 'textarea',
                        'sample_answer': '1) Expanded market reach to 2,000+ enterprise clients, 2) Cost reduction of 30% through shared resources, 3) Accelerated innovation through combined R&D efforts.'
                    }
                ]
            },
            {
                'id': 'business-overview',
                'title': 'Business Overview',
                'description': 'Background information about both organizations',
                'questions': [
                    {
                        'id': 'company-background',
                        'text': 'Provide background information about your company',
                        'type': 'textarea',
                        'sample_answer': 'Founded in 2018, TechCorp has grown to serve 500+ clients with our AI-powered analytics platform, generating $50M ARR with 40% YoY growth.'
                    },
                    {
                        'id': 'partner-alignment',
                        'text': 'How do the companies align in terms of values and culture?',
                        'type': 'textarea',
                        'sample_answer': 'Both organizations share a commitment to innovation, customer-centricity, and sustainable business practices, creating natural synergies for collaboration.'
                    }
                ]
            },
            {
                'id': 'partnership-objectives',
                'title': 'Partnership Objectives',
                'description': 'Specific goals and objectives of the partnership',
                'questions': [
                    {
                        'id': 'mutual-goals',
                        'text': 'What are the mutual goals and objectives?',
                        'type': 'textarea',
                        'sample_answer': 'Joint objectives include: capturing 15% market share in enterprise AI, developing 3 co-branded solutions, establishing presence in 5 new geographic markets.'
                    },
                    {
                        'id': 'success-metrics',
                        'text': 'How will success be measured and tracked?',
                        'type': 'textarea',
                        'sample_answer': 'Success metrics: $100M combined revenue by Year 2, 95% customer satisfaction, 50+ joint client implementations, and 25% cost savings through operational synergies.'
                    }
                ]
            },
            {
                'id': 'collaboration-scope',
                'title': 'Collaboration Scope',
                'description': 'Detailed scope of collaboration and responsibilities',
                'questions': [
                    {
                        'id': 'scope-activities',
                        'text': 'What specific activities will be included in the collaboration?',
                        'type': 'textarea',
                        'sample_answer': 'Co-development of AI solutions, joint sales and marketing initiatives, shared customer support, integrated technology platforms, and collaborative R&D projects.'
                    },
                    {
                        'id': 'responsibilities',
                        'text': 'What are each party\'s roles and responsibilities?',
                        'type': 'textarea',
                        'sample_answer': 'Partner A: Sales channel access, industry expertise, regulatory compliance. Partner B: Technology platform, R&D capabilities, technical implementation and support.'
                    }
                ]
            },
            {
                'id': 'financial-structure',
                'title': 'Financial Structure',
                'description': 'Revenue sharing and financial arrangements',
                'questions': [
                    {
                        'id': 'revenue-model',
                        'text': 'How will revenue be shared between partners?',
                        'type': 'textarea',
                        'sample_answer': 'Revenue split: 60/40 for joint solutions based on contribution, with separate tracking for referral fees (10%) and co-developed products (50/50 split).'
                    },
                    {
                        'id': 'investment-requirements',
                        'text': 'What investments or resources are required from each party?',
                        'type': 'textarea',
                        'sample_answer': 'Each party commits $2M in development resources, 10 FTE personnel, shared marketing budget of $1M, and technology infrastructure support.'
                    }
                ]
            },
            {
                'id': 'implementation-timeline',
                'title': 'Implementation Timeline',
                'description': 'Project timeline and key milestones',
                'questions': [
                    {
                        'id': 'timeline-phases',
                        'text': 'What are the key phases and milestones?',
                        'type': 'textarea',
                        'sample_answer': 'Phase 1 (Months 1-3): Legal agreements and team formation. Phase 2 (Months 4-8): Product development and integration. Phase 3 (Months 9-12): Market launch and scaling.'
                    },
                    {
                        'id': 'deliverables',
                        'text': 'What are the key deliverables and deadlines?',
                        'type': 'textarea',
                        'sample_answer': 'Q1: Partnership agreement signed, joint team established. Q2: MVP product development. Q3: Beta testing with 10 clients. Q4: Commercial launch and first $10M in joint revenue.'
                    }
                ]
            },
            {
                'id': 'risk-management',
                'title': 'Risk Management',
                'description': 'Potential risks and mitigation strategies',
                'questions': [
                    {
                        'id': 'key-risks',
                        'text': 'What are the key risks and challenges?',
                        'type': 'textarea',
                        'sample_answer': 'Key risks: Market competition, technology integration challenges, cultural alignment issues, regulatory changes, and potential IP conflicts.'
                    },
                    {
                        'id': 'mitigation-strategies',
                        'text': 'How will risks be mitigated and managed?',
                        'type': 'textarea',
                        'sample_answer': 'Risk mitigation: Monthly steering committee reviews, dedicated integration team, clear IP agreements, competitive analysis updates, and exit clause provisions.'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Project Proposal',
        'description': 'Comprehensive project proposal template for business initiatives and implementations',
        'category': 'business_proposal',
        'sections': [
            {
                'id': 'project-overview',
                'title': 'Project Overview',
                'description': 'Executive summary and project introduction',
                'questions': [
                    {
                        'id': 'project-title',
                        'text': 'What is the project title and brief description?',
                        'type': 'text',
                        'sample_answer': 'Digital Transformation Initiative: Enterprise Resource Planning System Implementation'
                    },
                    {
                        'id': 'project-purpose',
                        'text': 'What is the purpose and strategic importance of this project?',
                        'type': 'textarea',
                        'sample_answer': 'This project will modernize our core business operations through ERP implementation, improving efficiency by 40%, reducing costs by $2M annually, and enabling data-driven decision making.'
                    }
                ]
            },
            {
                'id': 'problem-statement',
                'title': 'Problem Statement',
                'description': 'Current challenges and business needs',
                'questions': [
                    {
                        'id': 'current-challenges',
                        'text': 'What specific problems or challenges does this project address?',
                        'type': 'textarea',
                        'sample_answer': 'Current challenges include: fragmented data systems, manual processes causing 25% inefficiency, lack of real-time reporting, and difficulty scaling operations to meet 50% growth targets.'
                    },
                    {
                        'id': 'business-impact',
                        'text': 'What is the business impact of not addressing these issues?',
                        'type': 'textarea',
                        'sample_answer': 'Without action: continued 25% operational inefficiency, $3M annual losses from manual errors, inability to scale for projected growth, and competitive disadvantage in market responsiveness.'
                    }
                ]
            },
            {
                'id': 'project-objectives',
                'title': 'Project Objectives',
                'description': 'Specific, measurable project goals',
                'questions': [
                    {
                        'id': 'smart-objectives',
                        'text': 'What are the SMART objectives for this project?',
                        'type': 'textarea',
                        'sample_answer': 'Objectives: 1) Implement ERP system across 5 departments by Q3, 2) Achieve 40% reduction in processing time, 3) Enable real-time reporting for 95% of operations, 4) Train 200+ users to proficiency level.'
                    },
                    {
                        'id': 'success-criteria',
                        'text': 'How will project success be measured?',
                        'type': 'textarea',
                        'sample_answer': 'Success metrics: System uptime >99.5%, user adoption >90%, ROI of 300% within 18 months, customer satisfaction score >8.5, and operational cost reduction of $2M annually.'
                    }
                ]
            },
            {
                'id': 'proposed-solution',
                'title': 'Proposed Solution',
                'description': 'Detailed solution and approach',
                'questions': [
                    {
                        'id': 'solution-approach',
                        'text': 'What is your proposed solution and methodology?',
                        'type': 'textarea',
                        'sample_answer': 'Phased ERP implementation using Agile methodology: Phase 1 - Finance/Accounting, Phase 2 - Operations/Supply Chain, Phase 3 - HR/CRM integration, with parallel data migration and training programs.'
                    },
                    {
                        'id': 'technology-stack',
                        'text': 'What technologies, tools, or systems will be used?',
                        'type': 'textarea',
                        'sample_answer': 'Technology stack: SAP S/4HANA Cloud, Microsoft Azure infrastructure, Power BI for analytics, custom integration APIs, and mobile applications for field operations.'
                    }
                ]
            },
            {
                'id': 'project-scope',
                'title': 'Project Scope',
                'description': 'Scope boundaries and deliverables',
                'questions': [
                    {
                        'id': 'scope-inclusions',
                        'text': 'What is included in the project scope?',
                        'type': 'textarea',
                        'sample_answer': 'Scope includes: ERP system configuration, data migration from 3 legacy systems, integration with existing CRM, user training for 200+ employees, documentation, and 6-month post-implementation support.'
                    },
                    {
                        'id': 'scope-exclusions',
                        'text': 'What is explicitly excluded from the project scope?',
                        'type': 'textarea',
                        'sample_answer': 'Exclusions: Hardware procurement (client responsibility), third-party software licenses, customizations beyond standard configuration, and modifications to existing business processes.'
                    },
                    {
                        'id': 'key-deliverables',
                        'text': 'What are the key project deliverables?',
                        'type': 'textarea',
                        'sample_answer': 'Deliverables: Configured ERP system, migrated data, integration with existing systems, user training materials, process documentation, testing reports, and go-live support plan.'
                    }
                ]
            },
            {
                'id': 'project-timeline',
                'title': 'Project Timeline',
                'description': 'Detailed project schedule and milestones',
                'questions': [
                    {
                        'id': 'project-phases',
                        'text': 'What are the main project phases and durations?',
                        'type': 'textarea',
                        'sample_answer': 'Phase 1: Planning & Design (8 weeks), Phase 2: Development & Configuration (16 weeks), Phase 3: Testing & Training (8 weeks), Phase 4: Deployment & Go-live (4 weeks).'
                    },
                    {
                        'id': 'critical-milestones',
                        'text': 'What are the critical milestones and dependencies?',
                        'type': 'textarea',
                        'sample_answer': 'Critical milestones: System design approval (Week 8), data migration completion (Week 20), user acceptance testing (Week 28), production go-live (Week 32), project closure (Week 36).'
                    }
                ]
            },
            {
                'id': 'budget-resources',
                'title': 'Budget and Resources',
                'description': 'Project costs and resource requirements',
                'questions': [
                    {
                        'id': 'total-budget',
                        'text': 'What is the total project budget breakdown?',
                        'type': 'textarea',
                        'sample_answer': 'Total budget: $850K - Software licenses ($300K), Implementation services ($350K), Training ($75K), Infrastructure ($75K), Contingency 10% ($50K).'
                    },
                    {
                        'id': 'resource-requirements',
                        'text': 'What human resources and expertise are required?',
                        'type': 'textarea',
                        'sample_answer': 'Resources needed: Project Manager (full-time), ERP Consultant (full-time), Technical Lead (full-time), 3 Business Analysts (part-time), Training Coordinator (part-time).'
                    }
                ]
            },
            {
                'id': 'risk-assessment',
                'title': 'Risk Assessment',
                'description': 'Project risks and mitigation strategies',
                'questions': [
                    {
                        'id': 'project-risks',
                        'text': 'What are the key project risks and their probability/impact?',
                        'type': 'textarea',
                        'sample_answer': 'High risks: Data migration complexity (70% probability), user adoption resistance (60% probability). Medium risks: Integration challenges (40%), timeline delays (35%).'
                    },
                    {
                        'id': 'risk-mitigation',
                        'text': 'What are the risk mitigation and contingency plans?',
                        'type': 'textarea',
                        'sample_answer': 'Mitigation strategies: Detailed data audit and cleanup, comprehensive change management program, prototype testing, dedicated integration team, and 15% schedule buffer.'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Investment Proposal',
        'description': 'Professional investment proposal template for securing funding from investors',
        'category': 'business_proposal',
        'sections': [
            {
                'id': 'executive-summary',
                'title': 'Executive Summary',
                'description': 'Compelling overview of investment opportunity',
                'questions': [
                    {
                        'id': 'business-overview',
                        'text': 'Provide a compelling overview of your business and opportunity',
                        'type': 'textarea',
                        'sample_answer': 'FinTech startup revolutionizing SMB lending with AI-powered risk assessment, serving underbanked market of 30M small businesses, seeking $5M Series A to capture $250B market opportunity.'
                    },
                    {
                        'id': 'investment-ask',
                        'text': 'What is your specific investment ask and use of funds?',
                        'type': 'textarea',
                        'sample_answer': 'Seeking $5M Series A funding: $2M for product development, $1.5M for market expansion, $1M for team scaling, $500K for regulatory compliance and working capital.'
                    }
                ]
            },
            {
                'id': 'business-description',
                'title': 'Business Description',
                'description': 'Detailed business model and value proposition',
                'questions': [
                    {
                        'id': 'company-mission',
                        'text': 'What is your company mission and vision?',
                        'type': 'textarea',
                        'sample_answer': 'Mission: Democratize access to capital for small businesses through AI-powered lending decisions. Vision: Become the leading alternative lending platform for SMBs globally.'
                    },
                    {
                        'id': 'value-proposition',
                        'text': 'What is your unique value proposition and competitive advantage?',
                        'type': 'textarea',
                        'sample_answer': 'Unique advantages: 90% faster loan decisions, 40% lower default rates through AI risk modeling, 24/7 automated processing, and access to previously underserved markets.'
                    },
                    {
                        'id': 'business-model',
                        'text': 'How does your business model work and generate revenue?',
                        'type': 'textarea',
                        'sample_answer': 'Revenue model: Origination fees (2-5% per loan), servicing fees (1% annually), premium analytics services ($500/month), and marketplace commission (0.5% on partner loans).'
                    }
                ]
            },
            {
                'id': 'market-analysis',
                'title': 'Market Analysis',
                'description': 'Market size, opportunity, and competitive landscape',
                'questions': [
                    {
                        'id': 'market-size',
                        'text': 'What is the total addressable market (TAM) and opportunity?',
                        'type': 'textarea',
                        'sample_answer': 'TAM: $250B alternative lending market, SAM: $75B SMB segment, SOM: $2.5B target market with 30M underbanked small businesses averaging $85K annual revenue.'
                    },
                    {
                        'id': 'target-customers',
                        'text': 'Who are your target customers and what are their pain points?',
                        'type': 'textarea',
                        'sample_answer': 'Target: Small businesses ($100K-$5M revenue) with limited credit history. Pain points: 6-month loan approval times, 60% rejection rates, excessive documentation requirements, high interest rates.'
                    },
                    {
                        'id': 'competitive-landscape',
                        'text': 'What is the competitive landscape and your positioning?',
                        'type': 'textarea',
                        'sample_answer': 'Competitors: OnDeck, Kabbage, Square Capital. Our differentiation: Superior AI accuracy (15% better default prediction), 48-hour decisions vs 2-week industry average, 35% lower costs.'
                    }
                ]
            },
            {
                'id': 'financial-projections',
                'title': 'Financial Projections',
                'description': 'Revenue forecasts and financial metrics',
                'questions': [
                    {
                        'id': 'revenue-projections',
                        'text': 'What are your 5-year revenue and growth projections?',
                        'type': 'textarea',
                        'sample_answer': 'Revenue projection: Year 1: $2M, Year 2: $8M, Year 3: $25M, Year 4: $65M, Year 5: $150M. Growth drivers: 300% YoY customer acquisition, 25% annual loan size increase.'
                    },
                    {
                        'id': 'unit-economics',
                        'text': 'What are your key unit economics and profitability metrics?',
                        'type': 'textarea',
                        'sample_answer': 'Unit economics: CAC $450, LTV $2,800 (LTV/CAC = 6.2x), 18-month payback period, 65% gross margins, EBITDA positive by Month 24 with 25% margins at scale.'
                    },
                    {
                        'id': 'funding-milestones',
                        'text': 'What milestones will this funding help you achieve?',
                        'type': 'textarea',
                        'sample_answer': 'Milestones: $25M loan originations by Year 2, expand to 10 states, achieve profitability, build team to 75 employees, prepare for Series B ($15M) by Month 18.'
                    }
                ]
            },
            {
                'id': 'management-team',
                'title': 'Management Team',
                'description': 'Leadership team and key personnel',
                'questions': [
                    {
                        'id': 'founding-team',
                        'text': 'Who are the founders and what relevant experience do they bring?',
                        'type': 'textarea',
                        'sample_answer': 'CEO: 15 years in fintech (former VP at Goldman Sachs), CTO: AI/ML expert (ex-Google, 3 patents), COO: Operations leader (scaled 2 startups to $100M+ revenue).'
                    },
                    {
                        'id': 'advisory-board',
                        'text': 'Who are your key advisors and board members?',
                        'type': 'textarea',
                        'sample_answer': 'Advisory board: Former CEO of major regional bank, Partner at top-tier VC firm, Head of Small Business at Fortune 500 company, Regulatory expert in fintech compliance.'
                    },
                    {
                        'id': 'key-hires',
                        'text': 'What key hires will you make with this funding?',
                        'type': 'textarea',
                        'sample_answer': 'Key hires: VP of Sales, Head of Risk Management, Senior Data Scientists (3), Regional Managers (5), Customer Success team (8), Compliance specialists (2).'
                    }
                ]
            },
            {
                'id': 'investment-terms',
                'title': 'Investment Terms',
                'description': 'Investment structure and terms',
                'questions': [
                    {
                        'id': 'investment-structure',
                        'text': 'What is the proposed investment structure and terms?',
                        'type': 'textarea',
                        'sample_answer': 'Series A Preferred Stock: $5M investment, $15M pre-money valuation, 25% equity stake, 1x liquidation preference, anti-dilution protection, board seat for lead investor.'
                    },
                    {
                        'id': 'use-of-funds',
                        'text': 'How will the investment funds be allocated and used?',
                        'type': 'textarea',
                        'sample_answer': 'Fund allocation: Product development (40%), Sales & Marketing (30%), Team expansion (20%), Regulatory & Compliance (10%). Detailed 18-month spending plan available.'
                    }
                ]
            },
            {
                'id': 'exit-strategy',
                'title': 'Exit Strategy',
                'description': 'Long-term strategy and investor returns',
                'questions': [
                    {
                        'id': 'exit-scenarios',
                        'text': 'What are the potential exit scenarios and timeline?',
                        'type': 'textarea',
                        'sample_answer': 'Exit options: IPO (5-7 years, $2B+ valuation target), Strategic acquisition by major bank/fintech (3-5 years, 8-12x revenue multiple), Private equity rollup (4-6 years).'
                    },
                    {
                        'id': 'investor-returns',
                        'text': 'What are the projected returns for investors?',
                        'type': 'textarea',
                        'sample_answer': 'Projected returns: 15-25x multiple over 5-7 years, based on comparable fintech exits (Kabbage $1.2B, OnDeck $1.3B). Conservative scenario: 10x return, optimistic: 30x return.'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Service Proposal',
        'description': 'Professional service proposal template for consulting and service-based businesses',
        'category': 'business_proposal',
        'sections': [
            {
                'id': 'client-understanding',
                'title': 'Client Understanding',
                'description': 'Demonstration of client needs and challenges',
                'questions': [
                    {
                        'id': 'client-situation',
                        'text': 'What is your understanding of the client\'s current situation?',
                        'type': 'textarea',
                        'sample_answer': 'Client faces 40% increase in customer service volume but maintains same staffing levels, resulting in 25% longer response times and declining customer satisfaction scores (dropped from 8.2 to 6.8).'
                    },
                    {
                        'id': 'pain-points',
                        'text': 'What specific pain points and challenges have you identified?',
                        'type': 'textarea',
                        'sample_answer': 'Key challenges: Overwhelmed support team, inconsistent response quality, lack of knowledge management system, no self-service options, and inability to track resolution metrics effectively.'
                    }
                ]
            },
            {
                'id': 'proposed-services',
                'title': 'Proposed Services',
                'description': 'Detailed service offerings and solutions',
                'questions': [
                    {
                        'id': 'service-overview',
                        'text': 'What services are you proposing to deliver?',
                        'type': 'textarea',
                        'sample_answer': 'Comprehensive customer service transformation: Process optimization, help desk implementation, agent training program, knowledge base development, and performance management system.'
                    },
                    {
                        'id': 'service-approach',
                        'text': 'What is your methodology and approach for delivering these services?',
                        'type': 'textarea',
                        'sample_answer': 'Four-phase approach: 1) Assessment & Analysis, 2) System Design & Implementation, 3) Training & Change Management, 4) Optimization & Performance Monitoring.'
                    },
                    {
                        'id': 'unique-differentiators',
                        'text': 'What makes your service approach unique and effective?',
                        'type': 'textarea',
                        'sample_answer': 'Differentiators: Proprietary customer journey mapping methodology, 24/7 implementation support, guaranteed 50% improvement in key metrics, and ongoing optimization for 12 months post-implementation.'
                    }
                ]
            },
            {
                'id': 'expected-outcomes',
                'title': 'Expected Outcomes',
                'description': 'Projected results and benefits',
                'questions': [
                    {
                        'id': 'measurable-results',
                        'text': 'What specific, measurable results can the client expect?',
                        'type': 'textarea',
                        'sample_answer': 'Expected results: 50% reduction in response time (4 hours to 2 hours), 85% first-call resolution rate, customer satisfaction increase to 9.0+, 30% reduction in support costs.'
                    },
                    {
                        'id': 'business-impact',
                        'text': 'What will be the broader business impact of these improvements?',
                        'type': 'textarea',
                        'sample_answer': 'Business impact: Enhanced customer retention (+15%), improved Net Promoter Score (+25 points), reduced churn rate (-20%), and increased customer lifetime value (+$500 per customer).'
                    }
                ]
            },
            {
                'id': 'implementation-plan',
                'title': 'Implementation Plan',
                'description': 'Detailed project timeline and phases',
                'questions': [
                    {
                        'id': 'project-phases',
                        'text': 'What are the key implementation phases and timelines?',
                        'type': 'textarea',
                        'sample_answer': 'Phase 1: Assessment (4 weeks), Phase 2: System Setup (6 weeks), Phase 3: Training (4 weeks), Phase 4: Go-live & Support (2 weeks), Phase 5: Optimization (ongoing).'
                    },
                    {
                        'id': 'key-milestones',
                        'text': 'What are the critical milestones and deliverables?',
                        'type': 'textarea',
                        'sample_answer': 'Milestones: Current state assessment complete, new system configured, staff trained and certified, go-live achieved, performance targets met, optimization plan implemented.'
                    }
                ]
            },
            {
                'id': 'team-expertise',
                'title': 'Team and Expertise',
                'description': 'Qualifications and team credentials',
                'questions': [
                    {
                        'id': 'team-qualifications',
                        'text': 'What qualifications and experience does your team bring?',
                        'type': 'textarea',
                        'sample_answer': 'Team credentials: Lead consultant with 15+ years in customer service optimization, certified project managers, help desk specialists with enterprise experience, and training experts with adult learning certifications.'
                    },
                    {
                        'id': 'relevant-experience',
                        'text': 'What relevant case studies or similar projects have you completed?',
                        'type': 'textarea',
                        'sample_answer': 'Recent successes: Reduced support costs by 35% for Fortune 500 retailer, improved satisfaction scores by 40% for healthcare provider, implemented 24/7 support for tech startup (scaled 10x).'
                    }
                ]
            },
            {
                'id': 'pricing-investment',
                'title': 'Pricing and Investment',
                'description': 'Service pricing and payment structure',
                'questions': [
                    {
                        'id': 'pricing-structure',
                        'text': 'What is your pricing structure and total investment required?',
                        'type': 'textarea',
                        'sample_answer': 'Total investment: $125,000 - Assessment ($15K), Implementation ($75K), Training ($20K), 12-month optimization support ($15K). Payment terms: 30% upfront, 50% at milestones, 20% upon completion.'
                    },
                    {
                        'id': 'roi-justification',
                        'text': 'How does the investment justify the return on investment?',
                        'type': 'textarea',
                        'sample_answer': 'ROI calculation: Annual savings of $200K from reduced support costs and improved efficiency. Project pays for itself in 7.5 months with 160% ROI in first year, 300%+ over three years.'
                    }
                ]
            },
            {
                'id': 'terms-conditions',
                'title': 'Terms and Conditions',
                'description': 'Project terms and service agreements',
                'questions': [
                    {
                        'id': 'service-guarantees',
                        'text': 'What guarantees or service level agreements do you provide?',
                        'type': 'textarea',
                        'sample_answer': 'Service guarantees: 50% improvement in key metrics or partial refund, 99% system uptime during implementation, 48-hour response time for support issues, and satisfaction guarantee.'
                    },
                    {
                        'id': 'project-terms',
                        'text': 'What are the key terms and conditions for this engagement?',
                        'type': 'textarea',
                        'sample_answer': 'Key terms: 16-week initial engagement, 12-month ongoing support included, intellectual property rights defined, confidentiality agreement, change order process for scope modifications.'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Vendor Proposal',
        'description': 'Comprehensive vendor proposal template for supplier and vendor relationships',
        'category': 'business_proposal',
        'sections': [
            {
                'id': 'company-profile',
                'title': 'Company Profile',
                'description': 'Vendor company background and credentials',
                'questions': [
                    {
                        'id': 'company-overview',
                        'text': 'Provide an overview of your company and core capabilities',
                        'type': 'textarea',
                        'sample_answer': 'Established in 2010, TechSupply Corp is a leading provider of enterprise IT equipment and services, serving 500+ clients across North America with $50M annual revenue and ISO 9001 certification.'
                    },
                    {
                        'id': 'certifications-credentials',
                        'text': 'What certifications, credentials, and industry recognition do you hold?',
                        'type': 'textarea',
                        'sample_answer': 'Certifications: ISO 9001:2015, SOC 2 Type II compliance, Microsoft Gold Partner, Cisco Premier Partner, AWS Advanced Consulting Partner, ITIL v4 certified team members.'
                    }
                ]
            },
            {
                'id': 'products-services',
                'title': 'Products and Services',
                'description': 'Detailed product/service offerings',
                'questions': [
                    {
                        'id': 'core-offerings',
                        'text': 'What are your core products and services?',
                        'type': 'textarea',
                        'sample_answer': 'Core offerings: Enterprise hardware procurement, cloud infrastructure services, managed IT support, cybersecurity solutions, data center services, and 24/7 technical support.'
                    },
                    {
                        'id': 'product-advantages',
                        'text': 'What are the key advantages and differentiators of your offerings?',
                        'type': 'textarea',
                        'sample_answer': 'Key advantages: 15-20% cost savings through volume purchasing, 99.9% service uptime guarantee, 24/7 support with 4-hour response time, and comprehensive warranty coverage.'
                    }
                ]
            },
            {
                'id': 'technical-capabilities',
                'title': 'Technical Capabilities',
                'description': 'Technical expertise and infrastructure',
                'questions': [
                    {
                        'id': 'technical-expertise',
                        'text': 'What technical expertise and capabilities does your team possess?',
                        'type': 'textarea',
                        'sample_answer': 'Technical team: 50+ certified engineers, expertise in cloud platforms (AWS, Azure, GCP), networking specialists, cybersecurity experts, and project managers with enterprise experience.'
                    },
                    {
                        'id': 'infrastructure-capacity',
                        'text': 'What infrastructure and capacity do you have to serve our needs?',
                        'type': 'textarea',
                        'sample_answer': 'Infrastructure: 100,000 sq ft warehouse, nationwide distribution network, redundant data centers, 24/7 NOC, and capacity to handle $10M+ monthly volume with same-day shipping.'
                    }
                ]
            },
            {
                'id': 'client-references',
                'title': 'Client References',
                'description': 'Customer testimonials and case studies',
                'questions': [
                    {
                        'id': 'key-clients',
                        'text': 'Who are some of your key clients and what results have you delivered?',
                        'type': 'textarea',
                        'sample_answer': 'Key clients: Fortune 500 manufacturer (30% cost reduction), Regional healthcare system (99.8% uptime), Tech startup (scaled infrastructure 500%), Government agency (security compliance achieved).'
                    },
                    {
                        'id': 'client-testimonials',
                        'text': 'Can you provide specific client testimonials or references?',
                        'type': 'textarea',
                        'sample_answer': 'Client feedback: "TechSupply reduced our IT costs by 25% while improving service quality" - CTO, Manufacturing Corp. "Outstanding support and reliability" - IT Director, Healthcare System.'
                    }
                ]
            },
            {
                'id': 'pricing-terms',
                'title': 'Pricing and Terms',
                'description': 'Pricing structure and commercial terms',
                'questions': [
                    {
                        'id': 'pricing-model',
                        'text': 'What is your pricing model and cost structure?',
                        'type': 'textarea',
                        'sample_answer': 'Pricing model: Volume-based discounts (5-20% based on annual spend), competitive market pricing, no setup fees, transparent pricing with quarterly reviews, and flexible payment terms.'
                    },
                    {
                        'id': 'contract-terms',
                        'text': 'What are your standard contract terms and conditions?',
                        'type': 'textarea',
                        'sample_answer': 'Contract terms: 3-year preferred agreements, 30-day payment terms, performance guarantees, annual price protection, early termination clauses, and comprehensive SLA coverage.'
                    }
                ]
            },
            {
                'id': 'service-support',
                'title': 'Service and Support',
                'description': 'Ongoing service and support capabilities',
                'questions': [
                    {
                        'id': 'support-model',
                        'text': 'What support model and service levels do you provide?',
                        'type': 'textarea',
                        'sample_answer': 'Support model: 24/7/365 helpdesk, dedicated account manager, escalation procedures, remote monitoring, on-site support when needed, and proactive maintenance programs.'
                    },
                    {
                        'id': 'quality-assurance',
                        'text': 'How do you ensure quality and continuous improvement?',
                        'type': 'textarea',
                        'sample_answer': 'Quality assurance: Monthly service reviews, customer satisfaction surveys, continuous staff training, process improvement programs, and compliance audits with corrective action plans.'
                    }
                ]
            },
            {
                'id': 'implementation-onboarding',
                'title': 'Implementation and Onboarding',
                'description': 'Onboarding process and transition plan',
                'questions': [
                    {
                        'id': 'onboarding-process',
                        'text': 'What is your onboarding and implementation process?',
                        'type': 'textarea',
                        'sample_answer': 'Onboarding process: Discovery phase (2 weeks), system integration (4 weeks), staff training (2 weeks), parallel operations (2 weeks), full transition (1 week), with dedicated transition manager.'
                    },
                    {
                        'id': 'transition-support',
                        'text': 'How will you ensure smooth transition from current vendor?',
                        'type': 'textarea',
                        'sample_answer': 'Transition support: Detailed migration plan, coordination with existing vendor, zero-downtime transition, knowledge transfer sessions, and 90-day enhanced support period.'
                    }
                ]
            }
        ]
    }
]