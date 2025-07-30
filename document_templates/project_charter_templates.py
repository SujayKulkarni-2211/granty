import uuid

PROJECT_CHARTER_TEMPLATES = [
    {
        'id': str(uuid.uuid4()),
        'name': 'Standard Project Charter',
        'description': 'Project charter template covering key initiation elements to authorize and align projects',
        'category': 'project_charter',
        'sections': [
            {
                'id': 'project-overview',
                'title': 'Project Overview',
                'description': 'Top‑level summary: name, purpose, background, objectives',
                'questions': [
                    {
                        'id': 'project-summary',
                        'text': 'Provide project name, purpose, business justification, and high‑level objectives.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Project Aurora: Launch internal analytics platform to unify user behavior tracking "
                            "across mobile/web. Purpose: Reduce data silos and enable cross‑channel insights. "
                            "Business justification: current reporting takes 3+ days; unified dashboard expected "
                            "to cut that to near real‑time (< 2 hours), increasing marketing ROI by 15%. "
                            "Objectives: deliver MVP in 4 months, onboard 3 business teams within 6 months."
                        )
                    }
                ]
            },
            {
                'id': 'scope-deliverables',
                'title': 'Scope & Deliverables',
                'description': 'Define what is in scope, out of scope, expected deliverables',
                'questions': [
                    {
                        'id': 'scope-definition',
                        'text': 'What is in scope and out of scope? Also list key deliverables.',
                        'type': 'textarea',
                        'sample_answer': (
                            "In scope: design and deploy ETL pipelines, unified dashboard with user-level metrics, "
                            "API for data export. Out of scope: mobile app changes, CRM integration, legacy BI migration. "
                            "Deliverables: data ingestion layer, dashboard UI, API documentation, user‑training deck."
                        )
                    }
                ]
            },
            {
                'id': 'milestones-timeline',
                'title': 'Timeline & Milestones',
                'description': 'High‑level schedule with key milestones',
                'questions': [
                    {
                        'id': 'timeline',
                        'text': 'List project milestones and target dates.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Milestone schedule:\n"
                            "- Project kickoff: Aug 5, 2025\n"
                            "- Design phase complete: Sep 15, 2025\n"
                            "- ETL/data pipelines live (beta): Nov 1, 2025\n"
                            "- Dashboard MVP launch: Dec 15, 2025\n"
                            "- Team onboarding complete: Feb 28, 2026"
                        )
                    }
                ]
            },
            {
                'id': 'roles-stakeholders',
                'title': 'Stakeholders & Roles',
                'description': 'Key sponsors, project manager, team roles and authority',
                'questions': [
                    {
                        'id': 'roles-responsibilities',
                        'text': 'Who are the stakeholders and what are their roles & responsibilities?',
                        'type': 'textarea',
                        'sample_answer': (
                            "Sponsor: VP Analytics (Approves funding and direction). Project Manager: Jane Doe, "
                            "leads planning and execution. Tech Lead: Dev Ops Lead, owns ETL/deployment. BI Analyst: "
                            "designs dashboard metrics. Steering Committee: CTO, CMO; meets monthly for approvals."
                        )
                    }
                ]
            },
            {
                'id': 'budget-resources',
                'title': 'Resources & Budget',
                'description': 'Estimated budget, staffing, tools',
                'questions': [
                    {
                        'id': 'budget-details',
                        'text': 'Provide approximate budget and resource plan.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Estimated budget: ₹50 lakhs. Resources: 1 PM (0.5 FTE), 2 engineers (full‑time), 1 BI analyst (0.5 FTE). "
                            "Tools: Redshift/Databricks cluster (~₹15 L), BI licenses (Tableau/PowerBI, ₹5 L), "
                            "data engineering support (₹10 L). Buffer for unforeseen costs: ₹5 L."
                        )
                    }
                ]
            },
            {
                'id': 'risks-constraints',
                'title': 'Risks, Assumptions & Constraints',
                'description': 'Key project risks, assumptions and constraints',
                'questions': [
                    {
                        'id': 'risk-analysis',
                        'text': 'Identify major risks and assumptions.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Risks: delays in legacy data access; ETL pipeline performance under high load; resource turnover. "
                            "Assumptions: committed access to data, no major scope creep. Constraints: must integrate within existing "
                            "cloud infra, budget capped at ₹50 L."
                        )
                    }
                ]
            },
            {
                'id': 'approval-signatures',
                'title': 'Approval & Governance',
                'description': 'Formal approval from sponsor and sign‑off',
                'questions': [
                    {
                        'id': 'approvals',
                        'text': 'Who authorizes this charter? Provide names, roles, and approval date.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Approved by:\n"
                            "- VP Analytics: John Smith, 04‑Jul‑2025\n"
                            "- CTO: Priya Narayanan, 05‑Jul‑2025\n"
                            "Prepared by: Jane Doe (Project Manager), 01‑Jul‑2025"
                        )
                    }
                ]
            }
        ]
    }
]
