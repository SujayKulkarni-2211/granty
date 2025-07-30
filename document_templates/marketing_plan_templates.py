# document_templates/marketing_plan_templates.py
import uuid

MARKETING_PLAN_TEMPLATES = [
    {
        'id': str(uuid.uuid4()),
        'name': 'Digital Marketing Strategy',
        'description': 'Comprehensive digital marketing strategy template structured via SOSTAC and RACE frameworks',
        'category': 'marketing_plan',
        'sections': [
            {
                'id': 'executive-summary',
                'title': 'Executive Summary',
                'description': 'Overview of objectives, scope and strategic direction',
                'questions': [
                    {
                        'id': 'summary-text',
                        'text': 'Provide an executive summary of the digital marketing approach.',
                        'type': 'textarea',
                        'sample_answer': (
                            "This digital marketing strategy aims to increase brand awareness by 40% and lead generation by 25% "
                            "over 12 months. Using the RACE (Reach‑Act‑Convert‑Engage) framework, we will leverage owned, earned, "
                            "shared, and paid media (PESO model) across content, social media, email campaigns, and targeted ads. "
                            "Key targets include a conversion rate of 5% on landing pages, a 20% increase in qualified leads, "
                            "and maintaining a cost per acquisition under ₹500."
                        )
                    }
                ]
            },
            {
                'id': 'situation-analysis',
                'title': 'Situation Analysis',
                'description': 'SWOT and market environment assessment',
                'questions': [
                    {
                        'id': 'swot-analysis',
                        'text': 'Summarize current strengths, weaknesses, opportunities, and threats.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Strengths: Strong existing SEO visibility, engaged social media community.\n"
                            "Weaknesses: Limited email subscriber base, low paid ad experience.\n"
                            "Opportunities: Rapid growth in regional language search volume (+30%), partnerships with complementary B2B channels.\n"
                            "Threats: Competitive paid search market, fast-changing social media algorithms affecting reach (e.g., Instagram/TikTok feeds)."
                        )
                    }
                ]
            },
            {
                'id': 'target-audience',
                'title': 'Target Audience & Buyer Personas',
                'description': 'Define market segments and detailed personas',
                'questions': [
                    {
                        'id': 'audience-personas',
                        'text': 'Who are your target segments and buyer personas?',
                        'type': 'textarea',
                        'sample_answer': (
                            "Buyer Persona A: Mid‑level IT Manager in Bengaluru (age 30‑45), values efficiency, reads technical blogs, "
                            "prefers LinkedIn content. \n"
                            "Persona B: Startup founder (age 25‑35) in India, tech‑savvy, engages on Twitter/X and YouTube, "
                            "looks for fast deployment solutions."
                        )
                    }
                ]
            },
            {
                'id': 'marketing-strategy',
                'title': 'Marketing Strategy & Channel Mix',
                'description': 'Strategic approach and channel selection per PESO model',
                'questions': [
                    {
                        'id': 'strategy-text',
                        'text': 'Describe your strategy and choice of marketing channels.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Paid: Google Ads targeting high‑intent keywords, LinkedIn sponsored posts.\n"
                            "Owned: Company blog, YouTube channel, email newsletter.\n"
                            "Earned: Guest contributions on industry sites, media coverage.\n"
                            "Shared: Social media posts, community forums, partnership collaborations.\n"
                            "Tactics include SEO optimization for long‑tail queries, repurposing blog posts into videos, "
                            "monthly webinars to drive lead magnets."
                        )
                    }
                ]
            },
            {
                'id': 'budget',
                'title': 'Budget & Resources',
                'description': 'Estimated costs and resource allocation',
                'questions': [
                    {
                        'id': 'budget-estimate',
                        'text': 'Provide a budget breakdown and resource plan.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Total annual budget: ₹15 lakhs.\n"
                            "Paid media (Google & LinkedIn): ₹6 L.\n"
                            "Content & SEO tools (Ahrefs, Grammarly): ₹2 L.\n"
                            "Email marketing platform: ₹1 L.\n"
                            "Outsourcing content creation and design: ₹3 L.\n"
                            "Team time: 40% of two FTE marketers."
                        )
                    }
                ]
            },
            {
                'id': 'metrics-and-control',
                'title': 'Metrics, KPIs & Control',
                'description': 'Define performance indicators and how you’ll monitor performance',
                'questions': [
                    {
                        'id': 'kpis',
                        'text': 'What KPIs will you track and how?',
                        'type': 'textarea',
                        'sample_answer': (
                            "KPIs: website traffic (+40%), conversion rate (≥5%), qualified leads (+20%), email open rate (≥25%), "
                            "social engagement growth (+30%).\n"
                            "Monitoring: Google Analytics for behavior funnel, monthly campaign dashboards in Data Studio, "
                            "quarterly reviews and adjustments."
                        )
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Product Launch Marketing Plan',
        'description': 'Marketing plan template tailored for launching a new product in digital and offline channels',
        'category': 'marketing_plan',
        'sections': [
            {
                'id': 'launch-overview',
                'title': 'Launch Goals & Objectives',
                'description': 'Define SMART launch goals',
                'questions': [
                    {
                        'id': 'launch-goals',
                        'text': 'What are the launch goals (SMART)?',
                        'type': 'textarea',
                        'sample_answer': (
                            "Specific: Generate 1,000 pre‑orders before launch; Measurable: capture leads via landing page; "
                            "Achievable: historic email conversion rate 8%; Relevant: aligns with new product revenue target; "
                            "Time‑bound: within 3 months."
                        )
                    }
                ]
            },
            {
                'id': 'audience-and-positioning',
                'title': 'Target Audience & Positioning',
                'description': 'Define buyer groups and brand positioning',
                'questions': [
                    {
                        'id': 'audience-positioning',
                        'text': 'Who is the audience and how is the product positioned?',
                        'type': 'textarea',
                        'sample_answer': (
                            "Audience: early adopters in SME tech (25‑40 years old), decision-makers evaluating modular SaaS products. "
                            "Positioning: affordable, quick-to-deploy solution with best‑in‑class uptime (99.9%) and backed by support."
                        )
                    }
                ]
            },
            {
                'id': 'launch-strategy',
                'title': 'Launch Strategy & Mix',
                'description': 'Approach across channels for launch phase',
                'questions': [
                    {
                        'id': 'launch-mix',
                        'text': 'Outline the promotional mix for product launch.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Pre-launch teaser via social media; influencer reviews and affiliate partnerships (earned/shared); "
                            "paid ads (Google, Facebook) driving to launch-specific landing page. "
                            "Owned media: countdown email drip & blog series. "
                            "Hosted webinar for feature demos and Q&A."
                        )
                    }
                ]
            },
            {
                'id': 'timeline-and-resources',
                'title': 'Timeline & Roles',
                'description': 'Detailed timeline and team responsibilities',
                'questions': [
                    {
                        'id': 'timeline',
                        'text': 'Provide project timeline and role assignments.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Week −8 to launch: asset creation (design, content);\n"
                            "Week −4: pre-launch emailing and paid ads kick‑off;\n"
                            "Launch week: live webinar, influencer live‑stream;\n"
                            "Post-launch Month 1–3: nurtures via email, review outreach.\n"
                            "Roles: Marketing Manager leads coordination, Content Specialist writes blog/email, Social Media Exec handles influencer and social campaigns."
                        )
                    }
                ]
            },
            {
                'id': 'measurement',
                'title': 'Metrics & Success Criteria',
                'description': 'Defines metrics and evaluation process',
                'questions': [
                    {
                        'id': 'launch-kpis',
                        'text': 'What metrics define launch success?',
                        'type': 'textarea',
                        'sample_answer': (
                            "Metrics: pre-orders, landing page conversion (target ≥10%), ad CTR ≥3%, webinar attendance ≥100, "
                            "social mentions and tag usage. "
                            "Dashboard created in Google Data Studio; weekly tracking during launch; retrospective review at end of Month 1."
                        )
                    }
                ]
            }
        ]
    }
]
