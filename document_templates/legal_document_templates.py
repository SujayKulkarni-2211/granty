import uuid

LEGAL_DOCUMENT_TEMPLATES = [
    {
        'id': str(uuid.uuid4()),
        'name': 'Mutual Non‑Disclosure Agreement',
        'description': 'Protect confidential business information between parties',
        'category': 'legal_document',
        'sections': [
            {
                'id': 'parties-purpose',
                'title': 'Parties & Purpose',
                'description': 'Identify parties and purpose of the NDA',
                'questions': [
                    {
                        'id': 'nda-overview',
                        'text': 'Describe the parties involved and the confidentiality scope.',
                        'type': 'textarea',
                        'sample_answer': (
                            "This Mutual NDA (“Agreement”) is between ABC Solutions Pvt. Ltd. (“Disclosing Party” or “Receiving Party”) "
                            "and XYZ Tech LLP (“Receiving Party” or “Disclosing Party”), concerning exchange of confidential business plans, "
                            "technical designs, and financial data for evaluation of a strategic partnership."
                        )
                    }
                ]
            },
            {
                'id': 'definitions',
                'title': 'Definition of Confidential Information',
                'description': 'Clarify what constitutes confidential information',
                'questions': [
                    {
                        'id': 'definitions-text',
                        'text': 'Define what information is considered confidential and any exclusions.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Confidential Information includes trade secrets, product roadmaps, customer lists, pricing, R&D data, "
                            "and unpublished patent applications. Exclusions: information publicly available, known prior to disclosure, "
                            "or rightfully obtained from third party without obligation."
                        )
                    }
                ]
            },
            {
                'id': 'obligations',
                'title': 'Obligations & Limitations',
                'description': 'Responsibilities of recipient',
                'questions': [
                    {
                        'id': 'obligations-text',
                        'text': 'Describe obligations and permitted use limitations.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Recipient must use Confidential Information solely for the stated purpose, restrict access to those on a need‑to‑know basis, "
                            "apply reasonable security measures, and return or destroy materials upon request or termination of the agreement."
                        )
                    }
                ]
            },
            {
                'id': 'term-governance',
                'title': 'Term, Duration & Governing Law',
                'description': 'Length of confidentiality and legal jurisdiction',
                'questions': [
                    {
                        'id': 'term-text',
                        'text': 'Specify term of NDA, duration of confidentiality, and jurisdiction.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Term: effective for 2 years from signing. Confidentiality obligations survive for 3 years post-expiration. "
                            "Governing law: Indian law, Bengaluru courts have exclusive jurisdiction."
                        )
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Independent Contractor Agreement',
        'description': 'Contract template for freelance or consultant engagement',
        'category': 'legal_document',
        'sections': [
            {
                'id': 'scope-deliverables',
                'title': 'Scope of Work & Deliverables',
                'description': 'Define work scope, timeline, and deliverables',
                'questions': [
                    {
                        'id': 'scope-text',
                        'text': 'Summarize the services and expected deliverables.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Consultant shall design and deliver a user‑testing report and UX wireframes within 8 weeks. "
                            "Deliverables: weekly progress reports, final test report, and revised wireframe set in Figma format."
                        )
                    }
                ]
            },
            {
                'id': 'payment-terms',
                'title': 'Payment Terms',
                'description': 'Compensation, invoicing, and timing',
                'questions': [
                    {
                        'id': 'payment-text',
                        'text': 'Describe fee structure and invoicing schedule.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Total fee ₹2 L paid in two instalments: ₹1 L on commencement, ₹1 L on delivery of final report. "
                            "Invoices due net 15 days; late payments subject to 1% interest/month."
                        )
                    }
                ]
            },
            {
                'id': 'confidentiality-ip',
                'title': 'Confidentiality & Intellectual Property',
                'description': 'NDA inclusion and ownership of work',
                'questions': [
                    {
                        'id': 'confidentiality-ip-text',
                        'text': 'Explain IP ownership and confidentiality obligations.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Consultant shall sign NDA covering confidential materials. All deliverables and derived IP are assigned to Client upon payment. "
                            "Consultant retains no rights."
                        )
                    }
                ]
            },
            {
                'id': 'termination-dispute',
                'title': 'Termination & Dispute Resolution',
                'description': 'Ending conditions and conflict resolution',
                'questions': [
                    {
                        'id': 'termination-text',
                        'text': 'Define termination conditions and dispute resolution mechanism.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Either party may terminate with 14 days’ written notice. For material breach, immediate termination allowed. "
                            "Disputes subject to arbitration under Indian Arbitration and Conciliation Act, seat in Bengaluru."
                        )
                    }
                ]
            }
        ]
    }
]
