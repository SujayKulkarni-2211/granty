# document_templates/technical_report_templates.py
import uuid

TECHNICAL_REPORT_TEMPLATES = [
    {
        'id': str(uuid.uuid4()),
        'name': 'Software Architecture Report',
        'description': 'Technical report for documenting software architecture following industry best practices',
        'category': 'technical_report',
        'sections': [
            {
                'id': 'architecture-overview',
                'title': 'Architecture Overview',
                'description': 'High-level system architecture including key views and standards',
                'questions': [
                    {
                        'id': 'overview-description',
                        'text': 'Provide a high‑level description of the system architecture and stakeholder concerns.',
                        'type': 'textarea',
                        'sample_answer': (
                            "This architecture is modeled using the C4 framework (context, containers, components, code) "
                            "to describe system views tailored to developers, operations, and business stakeholders. "
                            "It follows ISO/IEC/IEEE 42010 architecture description principles, describing viewpoints such as "
                            "logical structure, deployment topology, and runtime interactions. Key components are microservices "
                            "based on Spring Boot and containerized with Docker, deployed on Kubernetes (EKS), and exposed via "
                            "REST/gRPC APIs. The overall design supports modularity, scalability, and separation of concerns."
                        )
                    }
                ]
            },
            {
                'id': 'architectural-decisions',
                'title': 'Architectural Decisions',
                'description': 'Significant design choices and rationale',
                'questions': [
                    {
                        'id': 'decision-rationale',
                        'text': 'Enumerate key architectural decisions and their rationales.',
                        'type': 'textarea',
                        'sample_answer': (
                            "1. Adopted microservices over monolith to support independent deployment and scalability.\n"
                            "2. Chose Kafka-based event-driven messaging for loose coupling and high throughput.\n"
                            "3. Used PostgreSQL for relational data and Redis for caching to meet latency (< 50 ms) requirements.\n"
                            "4. Standardized API definitions with OpenAPI and JSON Schema for consistency.\n"
                            "Decisions were documented via ADRs (architecture decision records) per arc42 practice."
                        )
                    }
                ]
            },
            {
                'id': 'quality-attributes',
                'title': 'Quality Attributes',
                'description': 'Performance, reliability, security, maintainability',
                'questions': [
                    {
                        'id': 'quality-scenarios',
                        'text': 'Describe key quality scenarios and how architecture handles them.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Performance: auto‑scaling in EKS ensures horizontal scaling under peak load of 10 k concurrent users. "
                            "Reliability: services are stateless and use mutual TLS and circuit breakers for resilience. "
                            "Security: OAuth 2.0 JWT-based authentication and RBAC enforced in microservices. "
                            "Maintainability: code modularization and patterns aligned with arc42 reduce complexity. "
                            "Observability: integrated Prometheus/Grafana monitoring and centralized logging via ELK stack."
                        )
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Technical Feasibility Study',
        'description': 'Report assessing feasibility across technical, operational, economic, and organizational dimensions',
        'category': 'technical_report',
        'sections': [
            {
                'id': 'technical-feasibility',
                'title': 'Technical Feasibility',
                'description': 'Analysis of architecture, infrastructure, integration, tools, and skills',
                'questions': [
                    {
                        'id': 'technical-analysis',
                        'text': 'Evaluate technical feasibility: infrastructure, integration, tools, scalability.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Existing infrastructure (on‑premise VMs and AWS VPC) is sufficient to host microservices, "
                            "Kubernetes clusters, relational DB, message broker. Integration with legacy SOAP services "
                            "requires adapter layer—implementable using Spring Integration. Required skillsets (Docker, Kubernetes, Kafka) "
                            "are available in‑house. Potential bottlenecks include data synchronization (< 200 ms) in distributed nodes, "
                            "and technical debt in legacy modules. These risks are mitigated through phased pilot rollout and sandbox testing."
                        )
                    }
                ]
            },
            {
                'id': 'economic-feasibility',
                'title': 'Economic Feasibility',
                'description': 'Cost estimation, ROI, licensing, and budget analysis',
                'questions': [
                    {
                        'id': 'economic-assessment',
                        'text': 'Provide cost estimation and expected return on investment.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Estimated implementation cost: ~$350K (development, infrastructure, third‑party licenses). "
                            "Operational cost in AWS: ~$1.2K/month for production cluster. Projected ROI within 18 months based "
                            "on increased throughput and reduced downtime (estimated cost savings of $50K/month). Licensing costs "
                            "include commercial Kafka support ($10K/year) and monitoring tools ($5K/year). Break‑even expected in "
                            "month 18."
                        )
                    }
                ]
            },
            {
                'id': 'organizational-feasibility',
                'title': 'Organizational Feasibility',
                'description': 'Stakeholder alignment, change management, training needs',
                'questions': [
                    {
                        'id': 'organizational-analysis',
                        'text': 'Assess organizational readiness, stakeholder support, training, and change impact.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Project aligns with strategic objectives on digital transformation. Senior stakeholders (CTO, Engineering VP) "
                            "support it. End‑user teams require training on new dashboards and observability tools. Change management "
                            "includes onboarding workshops and pilot deployment to three business units. Adoption expected within 3 months post‑go‑live."
                        )
                    }
                ]
            }
        ]
    }
]
