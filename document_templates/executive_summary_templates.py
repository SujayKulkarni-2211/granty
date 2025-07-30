# document_templates/executive_summary_templates.py
import uuid

EXECUTIVE_SUMMARY_TEMPLATES = [
    {
        'id': str(uuid.uuid4()),
        'name': 'Business Plan Executive Summary',
        'description': 'Comprehensive executive summary for business plans and investment proposals',
        'category': 'executive_summary',
        'sections': [
            {
                'id': 'company-overview',
                'title': 'Company Overview',
                'description': 'Introduction and business concept',
                'questions': [
                    {
                        'id': 'company-introduction',
                        'text': 'Provide a brief introduction to your company, including name, location, and mission',
                        'type': 'textarea',
                        'sample_answer': 'TechFlow Solutions, based in Austin, Texas, is a fintech startup that democratizes access to capital for small businesses through AI-powered lending decisions. Our mission is to eliminate traditional barriers to business financing.'
                    },
                    {
                        'id': 'value-proposition',
                        'text': 'What is your unique value proposition and competitive advantage?',
                        'type': 'textarea',
                        'sample_answer': 'We reduce loan approval time from 6 weeks to 48 hours using proprietary AI algorithms, with 40% lower default rates and 60% reduced operational costs compared to traditional lenders.'
                    }
                ]
            },
            {
                'id': 'market-opportunity',
                'title': 'Market Opportunity',
                'description': 'Market analysis and target customers',
                'questions': [
                    {
                        'id': 'market-size',
                        'text': 'What is your target market size and growth potential?',
                        'type': 'textarea',
                        'sample_answer': 'TAM: $180B alternative lending market, SAM: $45B SMB segment, SOM: $2.2B addressable market with 28M underbanked small businesses. Market growing at 15% CAGR.'
                    },
                    {
                        'id': 'target-customers',
                        'text': 'Who are your target customers and what problems do you solve for them?',
                        'type': 'textarea',
                        'sample_answer': 'Target: Small businesses ($50K-$2M revenue) with limited credit history. We solve: 90% loan rejection rates, 6-month approval times, excessive documentation requirements, and lack of personalized service.'
                    }
                ]
            },
            {
                'id': 'products-services',
                'title': 'Products and Services',
                'description': 'Core offerings and key features',
                'questions': [
                    {
                        'id': 'core-offerings',
                        'text': 'What are your core products or services and their key benefits?',
                        'type': 'textarea',
                        'sample_answer': 'Core offerings: AI-powered business loans ($10K-$500K), real-time credit assessment, automated underwriting, and personalized financial advisory services. Benefits: 48-hour decisions, 30% lower rates, no collateral required.'
                    },
                    {
                        'id': 'competitive-advantages',
                        'text': 'What are your key competitive advantages and differentiators?',
                        'type': 'textarea',
                        'sample_answer': 'Proprietary AI with 85% accuracy in default prediction, partnerships with 500+ data providers, 24/7 automated processing, and personalized customer experience with dedicated relationship managers.'
                    }
                ]
            },
            {
                'id': 'business-model',
                'title': 'Business Model',
                'description': 'Revenue generation and financial strategy',
                'questions': [
                    {
                        'id': 'revenue-model',
                        'text': 'How does your business generate revenue?',
                        'type': 'textarea',
                        'sample_answer': 'Revenue streams: Origination fees (2-4% per loan), servicing fees (1.5% annually), premium analytics subscriptions ($200/month), and marketplace commissions (0.75% on partner loans).'
                    },
                    {
                        'id': 'financial-projections',
                        'text': 'What are your key financial projections and milestones?',
                        'type': 'textarea',
                        'sample_answer': 'Projections: Year 1: $3M revenue, Year 2: $12M, Year 3: $35M. Unit economics: CAC $380, LTV $2,400, 18-month payback. EBITDA positive by Month 20, targeting 30% margins at scale.'
                    }
                ]
            },
            {
                'id': 'management-team',
                'title': 'Management Team',
                'description': 'Leadership and key personnel',
                'questions': [
                    {
                        'id': 'leadership-team',
                        'text': 'Who are your key leaders and what relevant experience do they bring?',
                        'type': 'textarea',
                        'sample_answer': 'CEO: 12 years fintech experience (ex-VP at JPMorgan Chase), CTO: AI/ML expert (ex-Google, 4 patents), COO: Operations leader (scaled 2 fintech startups to $100M+ revenue).'
                    }
                ]
            },
            {
                'id': 'funding-requirements',
                'title': 'Funding Requirements',
                'description': 'Investment needs and use of funds',
                'questions': [
                    {
                        'id': 'funding-ask',
                        'text': 'How much funding are you seeking and how will it be used?',
                        'type': 'textarea',
                        'sample_answer': 'Seeking $8M Series A: $3M product development and AI enhancement, $2.5M market expansion, $1.5M team scaling (25 new hires), $1M regulatory compliance and working capital.'
                    },
                    {
                        'id': 'investor-returns',
                        'text': 'What returns and exit opportunities can investors expect?',
                        'type': 'textarea',
                        'sample_answer': 'Target exit: IPO or strategic acquisition in 5-7 years at $1.5-2B valuation. Projected investor returns: 12-20x multiple based on comparable fintech exits (OnDeck $1.3B, Kabbage $1.2B).'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Project Executive Summary',
        'description': 'Executive summary template for project proposals and initiatives',
        'category': 'executive_summary',
        'sections': [
            {
                'id': 'project-context',
                'title': 'Project Context',
                'description': 'Project background and importance',
                'questions': [
                    {
                        'id': 'project-overview',
                        'text': 'What is the project and why is it important to the organization?',
                        'type': 'textarea',
                        'sample_answer': 'Digital Transformation Initiative: Implementing cloud-based ERP system across 5 business units to modernize operations, improve efficiency by 35%, and support projected 50% business growth over next 3 years.'
                    },
                    {
                        'id': 'strategic-alignment',
                        'text': 'How does this project align with organizational strategy and goals?',
                        'type': 'textarea',
                        'sample_answer': 'Directly supports 2025 strategic plan objectives: operational excellence, digital-first customer experience, and scalable growth platform. Critical enabler for expansion into 3 new markets.'
                    }
                ]
            },
            {
                'id': 'problem-opportunity',
                'title': 'Problem and Opportunity',
                'description': 'Current challenges and business case',
                'questions': [
                    {
                        'id': 'current-challenges',
                        'text': 'What specific problems or challenges does this project address?',
                        'type': 'textarea',
                        'sample_answer': 'Current challenges: 25% operational inefficiency from manual processes, fragmented data across 12 legacy systems, inability to access real-time reporting, and limited scalability for growth.'
                    },
                    {
                        'id': 'business-impact',
                        'text': 'What is the business impact if these challenges are not addressed?',
                        'type': 'textarea',
                        'sample_answer': 'Without action: $2.5M annual losses from inefficiencies, competitive disadvantage, inability to capitalize on 50% projected growth, and risk of regulatory compliance issues.'
                    }
                ]
            },
            {
                'id': 'proposed-solution',
                'title': 'Proposed Solution',
                'description': 'Project approach and methodology',
                'questions': [
                    {
                        'id': 'solution-approach',
                        'text': 'What is your recommended solution and implementation approach?',
                        'type': 'textarea',
                        'sample_answer': 'Phased ERP implementation using Agile methodology: Phase 1-Finance (12 weeks), Phase 2-Operations (16 weeks), Phase 3-Integration (8 weeks), with parallel training and change management.'
                    },
                    {
                        'id': 'key-deliverables',
                        'text': 'What are the key deliverables and expected outcomes?',
                        'type': 'textarea',
                        'sample_answer': 'Deliverables: Fully integrated ERP system, migrated data from legacy systems, trained workforce (200+ users), process documentation, and 6-month post-implementation support.'
                    }
                ]
            },
            {
                'id': 'project-timeline',
                'title': 'Timeline and Milestones',
                'description': 'Project schedule and critical milestones',
                'questions': [
                    {
                        'id': 'timeline-overview',
                        'text': 'What is the overall timeline and what are the critical milestones?',
                        'type': 'textarea',
                        'sample_answer': '36-week implementation: Weeks 1-12 (Phase 1 completion), Weeks 13-28 (Phase 2 completion), Weeks 29-36 (Integration and go-live). Critical milestones: System design approval, data migration, user training, production deployment.'
                    }
                ]
            },
            {
                'id': 'resources-budget',
                'title': 'Resources and Budget',
                'description': 'Resource requirements and financial investment',
                'questions': [
                    {
                        'id': 'budget-overview',
                        'text': 'What is the total budget and resource requirements?',
                        'type': 'textarea',
                        'sample_answer': 'Total budget: $1.2M - Software licenses ($450K), Implementation services ($500K), Training ($150K), Infrastructure ($100K). Human resources: 8 FTE internal team, 4 external consultants.'
                    },
                    {
                        'id': 'roi-justification',
                        'text': 'What is the expected return on investment and business benefits?',
                        'type': 'textarea',
                        'sample_answer': 'Expected ROI: 285% over 3 years. Annual benefits: $1.8M cost savings, 35% efficiency improvement, 50% reduction in manual errors, real-time reporting capabilities, enhanced compliance.'
                    }
                ]
            },
            {
                'id': 'risks-mitigation',
                'title': 'Risks and Mitigation',
                'description': 'Key risks and management strategies',
                'questions': [
                    {
                        'id': 'key-risks',
                        'text': 'What are the key risks and how will they be mitigated?',
                        'type': 'textarea',
                        'sample_answer': 'Key risks: Data migration complexity (60% probability), user adoption resistance (45%), integration challenges (35%). Mitigation: Dedicated data team, comprehensive change management, prototype testing, 15% schedule buffer.'
                    }
                ]
            },
            {
                'id': 'next-steps',
                'title': 'Next Steps and Approval',
                'description': 'Required actions and decision points',
                'questions': [
                    {
                        'id': 'immediate-actions',
                        'text': 'What are the immediate next steps and approval requirements?',
                        'type': 'textarea',
                        'sample_answer': 'Next steps: Executive committee approval (Week 1), vendor contract finalization (Week 2), project team formation (Week 3), project kickoff (Week 4). Seeking approval for $1.2M budget allocation.'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Strategic Initiative Summary',
        'description': 'Executive summary for strategic initiatives and organizational change programs',
        'category': 'executive_summary',
        'sections': [
            {
                'id': 'strategic-context',
                'title': 'Strategic Context',
                'description': 'Strategic background and organizational importance',
                'questions': [
                    {
                        'id': 'initiative-overview',
                        'text': 'What is the strategic initiative and why is it critical for the organization?',
                        'type': 'textarea',
                        'sample_answer': 'Customer Experience Transformation Initiative: Comprehensive program to achieve industry-leading NPS of 70+ through omnichannel integration, AI-powered personalization, and service excellence across all touchpoints.'
                    },
                    {
                        'id': 'strategic-rationale',
                        'text': 'What is the strategic rationale and connection to business objectives?',
                        'type': 'textarea',
                        'sample_answer': 'Critical for 2025-2027 strategic plan: drive 25% revenue growth through customer retention, capture $50M in new market opportunities, and differentiate from competitors in commoditized market.'
                    }
                ]
            },
            {
                'id': 'current-state-analysis',
                'title': 'Current State Analysis',
                'description': 'Assessment of current situation and gaps',
                'questions': [
                    {
                        'id': 'current-performance',
                        'text': 'What is the current state and performance baseline?',
                        'type': 'textarea',
                        'sample_answer': 'Current state: NPS 35 (industry average 45), 22% customer churn rate, fragmented experience across 6 channels, 48-hour average response time, and limited personalization capabilities.'
                    },
                    {
                        'id': 'performance-gaps',
                        'text': 'What are the key performance gaps and competitive disadvantages?',
                        'type': 'textarea',
                        'sample_answer': 'Performance gaps: 30-point NPS deficit vs. best-in-class, 2x higher churn than competitors, 15x slower response than digital leaders, resulting in $8M annual revenue impact.'
                    }
                ]
            },
            {
                'id': 'strategic-vision',
                'title': 'Strategic Vision',
                'description': 'Future state vision and success criteria',
                'questions': [
                    {
                        'id': 'future-vision',
                        'text': 'What is the future state vision and transformation goals?',
                        'type': 'textarea',
                        'sample_answer': 'Vision: Industry-leading customer experience with NPS 70+, seamless omnichannel journey, 2-hour response time, 95% first-contact resolution, and AI-driven personalization for 2M+ customers.'
                    },
                    {
                        'id': 'success-metrics',
                        'text': 'What are the key success metrics and performance targets?',
                        'type': 'textarea',
                        'sample_answer': 'Success metrics: NPS increase to 70+, churn reduction to 8%, response time under 2 hours, customer satisfaction 95%+, $15M incremental revenue, 40% efficiency improvement.'
                    }
                ]
            },
            {
                'id': 'transformation-approach',
                'title': 'Transformation Approach',
                'description': 'Strategic approach and implementation methodology',
                'questions': [
                    {
                        'id': 'transformation-strategy',
                        'text': 'What is the overall transformation strategy and approach?',
                        'type': 'textarea',
                        'sample_answer': 'Three-pillar approach: 1) Technology modernization (omnichannel platform, AI/ML capabilities), 2) Process optimization (service design, automation), 3) Culture transformation (customer-centric mindset, skills development).'
                    },
                    {
                        'id': 'key-initiatives',
                        'text': 'What are the key initiatives and transformation programs?',
                        'type': 'textarea',
                        'sample_answer': 'Key initiatives: Customer data platform implementation, omnichannel service portal, AI chatbot deployment, agent training program, process automation, and performance management system.'
                    }
                ]
            },
            {
                'id': 'implementation-roadmap',
                'title': 'Implementation Roadmap',
                'description': 'Timeline and phased implementation plan',
                'questions': [
                    {
                        'id': 'implementation-phases',
                        'text': 'What are the key implementation phases and timeline?',
                        'type': 'textarea',
                        'sample_answer': '24-month roadmap: Phase 1 (Months 1-8): Foundation and quick wins, Phase 2 (Months 9-16): Core transformation, Phase 3 (Months 17-24): Optimization and scale.'
                    },
                    {
                        'id': 'critical-milestones',
                        'text': 'What are the critical milestones and dependencies?',
                        'type': 'textarea',
                        'sample_answer': 'Critical milestones: Customer data platform live (Month 6), omnichannel portal launch (Month 12), AI implementation (Month 18), full transformation (Month 24). Dependencies: IT infrastructure, change management, training.'
                    }
                ]
            },
            {
                'id': 'investment-returns',
                'title': 'Investment and Returns',
                'description': 'Financial investment and expected returns',
                'questions': [
                    {
                        'id': 'investment-requirements',
                        'text': 'What is the total investment required across all initiatives?',
                        'type': 'textarea',
                        'sample_answer': 'Total investment: $12M over 24 months - Technology ($6M), Process improvement ($3M), Change management ($2M), Training and development ($1M). Annual operating impact: +$500K.'
                    },
                    {
                        'id': 'business-value',
                        'text': 'What is the expected business value and return on investment?',
                        'type': 'textarea',
                        'sample_answer': 'Expected returns: $25M incremental revenue over 3 years, $8M cost savings, 220% ROI. Payback period: 18 months. Additional benefits: brand differentiation, employee engagement, market leadership.'
                    }
                ]
            },
            {
                'id': 'change-management',
                'title': 'Change Management',
                'description': 'Organizational change and risk management',
                'questions': [
                    {
                        'id': 'organizational-impact',
                        'text': 'What is the organizational impact and change management approach?',
                        'type': 'textarea',
                        'sample_answer': 'Impact: 500+ employees across customer service, sales, and operations. Change approach: Executive sponsorship, change champions network, comprehensive training, communication plan, and cultural transformation program.'
                    },
                    {
                        'id': 'success-factors',
                        'text': 'What are the critical success factors and risk mitigation strategies?',
                        'type': 'textarea',
                        'sample_answer': 'Success factors: Strong leadership commitment, employee engagement, technology adoption, customer feedback integration. Risk mitigation: Pilot programs, staged rollouts, continuous monitoring, and agile adaptation.'
                    }
                ]
            }
        ]
    }
]