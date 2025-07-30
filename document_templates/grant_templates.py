# document_templates/grant_templates.py
import uuid

GRANT_TEMPLATES = [
    {
        'id': str(uuid.uuid4()),
        'name': 'NSF Research Grant',
        'description': 'National Science Foundation research grant proposal template',
        'category': 'grant',
        'sections': [
            {
                'id': 'project-summary',
                'title': 'Project Summary',
                'description': 'One-page overview of the proposed project',
                'questions': [
                    {
                        'id': 'project-overview',
                        'text': 'Provide a clear and concise overview of your research project',
                        'type': 'textarea',
                        'sample_answer': 'This project investigates novel quantum computing algorithms for solving NP-hard optimization problems in logistics and supply chain management. We propose developing quantum-classical hybrid algorithms with demonstrated 1000x speedup over classical methods.'
                    },
                    {
                        'id': 'intellectual-merit',
                        'text': 'What is the intellectual merit of the proposed activity?',
                        'type': 'textarea',
                        'sample_answer': 'This research advances quantum algorithm theory by developing provably efficient quantum optimization protocols. Novel contributions include: (1) quantum approximate optimization algorithms with theoretical guarantees, (2) error-corrected implementations on NISQ devices, (3) complexity analysis demonstrating exponential quantum advantage.'
                    },
                    {
                        'id': 'broader-impacts',
                        'text': 'What are the broader impacts of the proposed activity?',
                        'type': 'textarea',
                        'sample_answer': 'Broader impacts include: (1) Training 3 PhD students and 2 postdocs in quantum computing, (2) K-12 outreach through quantum computing workshops reaching 500+ students annually, (3) Industry partnerships with logistics companies, (4) Open-source quantum software benefiting global research community.'
                    }
                ]
            },
            {
                'id': 'project-description',
                'title': 'Project Description',
                'description': 'Detailed research plan and methodology',
                'questions': [
                    {
                        'id': 'research-objectives',
                        'text': 'What are the specific research objectives and aims?',
                        'type': 'textarea',
                        'sample_answer': 'Objectives: (1) Develop quantum optimization algorithms for vehicle routing problems, (2) Implement error mitigation techniques for NISQ devices, (3) Demonstrate quantum advantage on real-world logistics datasets, (4) Create theoretical framework for quantum-classical optimization convergence.'
                    },
                    {
                        'id': 'methodology',
                        'text': 'Describe your research methodology and approach',
                        'type': 'textarea',
                        'sample_answer': 'Methodology combines theoretical algorithm development with experimental validation. Phase 1: Algorithm design using variational quantum optimization. Phase 2: Error correction implementation on IBM quantum hardware. Phase 3: Benchmarking against classical algorithms using industry datasets from FedEx and UPS partnerships.'
                    },
                    {
                        'id': 'expected-outcomes',
                        'text': 'What are the expected outcomes and deliverables?',
                        'type': 'textarea',
                        'sample_answer': 'Expected outcomes: (1) 5-8 peer-reviewed publications in top-tier venues (Nature, Science, Physical Review), (2) Open-source quantum optimization library with 1000+ GitHub stars, (3) 3 patent applications, (4) Prototype quantum algorithms demonstrated on 100+ qubit systems.'
                    }
                ]
            },
            {
                'id': 'research-team',
                'title': 'Research Team',
                'description': 'Principal investigator and team qualifications',
                'questions': [
                    {
                        'id': 'pi-qualifications',
                        'text': 'Describe the PI qualifications and relevant experience',
                        'type': 'textarea',
                        'sample_answer': 'PI: Dr. Sarah Chen, Professor of Quantum Computing at MIT. 15 years experience in quantum algorithms, 85 publications (h-index 45), $8M previous NSF funding. Key contributions: Developed quantum machine learning algorithms used by Google and IBM. Member of National Quantum Initiative Advisory Committee.'
                    },
                    {
                        'id': 'team-members',
                        'text': 'Who are the key team members and their roles?',
                        'type': 'textarea',
                        'sample_answer': 'Team: Co-PI Dr. Michael Kumar (optimization expert, 12 years industry experience), 3 PhD students (quantum algorithms specialization), 2 postdocs (experimental quantum computing), Software Engineer (quantum software development), Industry Advisory Board (FedEx CTO, IBM Quantum VP).'
                    }
                ]
            },
            {
                'id': 'budget-justification',
                'title': 'Budget and Justification',
                'description': 'Detailed budget and cost justification',
                'questions': [
                    {
                        'id': 'total-budget',
                        'text': 'What is the total budget and breakdown by category?',
                        'type': 'textarea',
                        'sample_answer': 'Total 3-year budget: $850,000. Personnel (65%): $552,500 (PI 25% summer, Co-PI 10% AY, 3 PhD students, 2 postdocs). Equipment (20%): $170,000 (quantum computing hardware, servers). Travel (10%): $85,000 (conferences, collaborations). Other (5%): $42,500 (supplies, publication costs).'
                    },
                    {
                        'id': 'cost-effectiveness',
                        'text': 'How does the budget demonstrate cost-effectiveness?',
                        'type': 'textarea',
                        'sample_answer': 'Budget leverages existing $2M quantum lab infrastructure. Cost per publication: $106,000 (8 expected papers). Training cost per student: $94,000 (9 students/postdocs). Industry partnership provides $200,000 in-kind computing resources, doubling effective budget impact.'
                    }
                ]
            },
            {
                'id': 'facilities-resources',
                'title': 'Facilities and Resources',
                'description': 'Available facilities and institutional support',
                'questions': [
                    {
                        'id': 'institutional-resources',
                        'text': 'What institutional facilities and resources are available?',
                        'type': 'textarea',
                        'sample_answer': 'MIT Quantum Engineering Lab: 5000 sq ft facility with dilution refrigerators, quantum control electronics, cleanroom access. Computing resources: 500-node classical cluster, dedicated quantum simulators. Library: comprehensive quantum computing collection. Administrative support: dedicated grants management office.'
                    },
                    {
                        'id': 'external-partnerships',
                        'text': 'What external partnerships and collaborations support this work?',
                        'type': 'textarea',
                        'sample_answer': 'External partnerships: IBM Quantum Network (hardware access), Google Quantum Lab (algorithm testing), MIT-Industry Quantum Alliance (12 companies), NSF Quantum Leap Challenge Institute membership. International: collaboration agreements with Oxford, ETH Zurich, University of Tokyo quantum groups.'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'NIH Medical Research Grant (R01)',
        'description': 'National Institutes of Health R01 research grant template',
        'category': 'grant',
        'sections': [
            {
                'id': 'specific-aims',
                'title': 'Specific Aims',
                'description': 'Research objectives and significance',
                'questions': [
                    {
                        'id': 'research-problem',
                        'text': 'What medical problem or health challenge are you addressing?',
                        'type': 'textarea',
                        'sample_answer': 'Alzheimers disease affects 6.5 million Americans with no disease-modifying treatments. Current diagnostics detect pathology 15-20 years after onset, missing critical intervention windows. Early biomarker detection could enable preventive therapies, potentially reducing disease incidence by 40%.'
                    },
                    {
                        'id': 'central-hypothesis',
                        'text': 'What is your central hypothesis and rationale?',
                        'type': 'textarea',
                        'sample_answer': 'Central hypothesis: Multimodal AI analysis of retinal imaging, blood biomarkers, and cognitive assessments can detect Alzheimers pathology 10-15 years before clinical symptoms. Rationale: Retinal changes mirror brain pathology, blood biomarkers indicate amyloid/tau accumulation, cognitive micro-changes precede dementia.'
                    },
                    {
                        'id': 'specific-aims-list',
                        'text': 'List your 2-3 specific aims with testable hypotheses',
                        'type': 'textarea',
                        'sample_answer': 'Aim 1: Develop AI algorithms integrating retinal OCT, fundus photography, and blood proteomics for Alzheimers prediction (n=2000 subjects, 85% accuracy target). Aim 2: Validate biomarker panel in longitudinal cohort study (n=1500, 10-year follow-up). Aim 3: Create clinical decision support tool for primary care physicians.'
                    }
                ]
            },
            {
                'id': 'research-strategy',
                'title': 'Research Strategy',
                'description': 'Significance, innovation, and approach',
                'questions': [
                    {
                        'id': 'significance',
                        'text': 'What is the significance and impact of this research?',
                        'type': 'textarea',
                        'sample_answer': 'Significance: Early Alzheimers detection could delay nursing home placement by 2.8 years, saving $373,000 per patient. Population impact: screening 50M Americans aged 50+ could identify 5M at-risk individuals for preventive interventions. Scientific impact: establishes retinal imaging as CNS biomarker platform.'
                    },
                    {
                        'id': 'innovation',
                        'text': 'What innovative approaches or technologies will you use?',
                        'type': 'textarea',
                        'sample_answer': 'Innovation: (1) First multimodal AI combining retinal, blood, and cognitive data, (2) Novel deep learning architecture for longitudinal biomarker evolution, (3) Retinal vascular analysis using proprietary algorithms, (4) Integration with EHR systems for population screening.'
                    },
                    {
                        'id': 'research-approach',
                        'text': 'Describe your research approach and methodology',
                        'type': 'textarea',
                        'sample_answer': 'Approach: Prospective cohort study at 5 clinical sites. Year 1-2: Recruit 2000 participants (ages 50-75), collect baseline data. Year 3-4: Algorithm development using machine learning on 80% training set. Year 5: Validation on 20% held-out test set. Longitudinal follow-up for clinical outcomes confirmation.'
                    }
                ]
            },
            {
                'id': 'preliminary-studies',
                'title': 'Preliminary Studies',
                'description': 'Prior work and feasibility data',
                'questions': [
                    {
                        'id': 'prior-research',
                        'text': 'What preliminary data supports the feasibility of your approach?',
                        'type': 'textarea',
                        'sample_answer': 'Preliminary data: (1) Pilot study (n=200) showed 78% accuracy in Alzheimers prediction using retinal imaging alone, (2) Blood biomarker panel achieved 82% sensitivity/75% specificity, (3) Combined modalities reached 87% accuracy in cross-validation, (4) Algorithm processing time: <2 minutes per patient.'
                    },
                    {
                        'id': 'pilot-results',
                        'text': 'What key findings from pilot studies support your hypothesis?',
                        'type': 'textarea',
                        'sample_answer': 'Key findings: (1) Retinal vessel density correlates with CSF amyloid levels (r=0.73, p<0.001), (2) Blood neurofilament light predicts cognitive decline 5 years ahead (AUC=0.84), (3) AI model generalizes across populations (validated in 3 ethnic groups), (4) Clinical workflow integration feasible in primary care.'
                    }
                ]
            },
            {
                'id': 'human-subjects',
                'title': 'Human Subjects Research',
                'description': 'Human subjects protection and ethics',
                'questions': [
                    {
                        'id': 'subject-protection',
                        'text': 'How will you protect human subjects and ensure ethical research?',
                        'type': 'textarea',
                        'sample_answer': 'Human subjects protection: IRB approval from all sites, written informed consent, data de-identification protocols, secure data transmission (256-bit encryption), HIPAA compliance, Data Safety Monitoring Board oversight. Vulnerable populations excluded. Genetic data handled per NIH guidelines.'
                    },
                    {
                        'id': 'inclusion-criteria',
                        'text': 'What are your inclusion criteria and demographic targets?',
                        'type': 'textarea',
                        'sample_answer': 'Inclusion: Adults 50-75 years, cognitively normal (MoCA≥26), English/Spanish speaking. Demographics: 50% women, 30% minorities (Hispanic, African American), socioeconomically diverse. Exclusion: dementia diagnosis, major eye disease, recent chemotherapy. Target enrollment reflects US population diversity.'
                    }
                ]
            },
            {
                'id': 'research-team-nih',
                'title': 'Research Team and Environment',
                'description': 'Investigator qualifications and institutional support',
                'questions': [
                    {
                        'id': 'investigator-experience',
                        'text': 'What are the key qualifications of the research team?',
                        'type': 'textarea',
                        'sample_answer': 'PI: Dr. Lisa Rodriguez, Professor of Neurology, 18 years Alzheimers research, 120 publications (h-index 52), $15M NIH funding. Co-I: Dr. James Park (retinal imaging expert), Dr. Sarah Kim (AI/ML), Dr. Maria Santos (biomarker development). Team managed 5 previous NIH R01s with 100% completion rate.'
                    },
                    {
                        'id': 'institutional-environment',
                        'text': 'How does the institutional environment support this research?',
                        'type': 'textarea',
                        'sample_answer': 'Environment: Stanford Alzheimers Disease Research Center (ADRC), NIH-funded P30 center with 200+ faculty. Core facilities: Neuroimaging (3T/7T MRI), Biomarker lab (Luminex, Simoa), AI computing cluster (1000 GPUs). Clinical infrastructure: 5000+ research participants, electronic health records integration.'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'SBIR Phase I Grant',
        'description': 'Small Business Innovation Research Phase I proposal template',
        'category': 'grant',
        'sections': [
            {
                'id': 'technical-innovation',
                'title': 'Technical Innovation',
                'description': 'Core innovation and technology description',
                'questions': [
                    {
                        'id': 'innovation-description',
                        'text': 'Describe your core technical innovation and breakthrough',
                        'type': 'textarea',
                        'sample_answer': 'Revolutionary AI-powered medical diagnostic platform using computer vision to analyze chest X-rays with 94% accuracy (vs 87% for radiologists). Key innovation: proprietary deep learning architecture combining attention mechanisms with uncertainty quantification, trained on 2M+ anonymized images from 15 countries.'
                    },
                    {
                        'id': 'technical-approach',
                        'text': 'What is your technical approach and methodology?',
                        'type': 'textarea',
                        'sample_answer': 'Technical approach: (1) Multi-scale convolutional neural networks for feature extraction, (2) Transformer-based attention for region-of-interest identification, (3) Bayesian uncertainty estimation for confidence scoring, (4) Federated learning for continuous model improvement, (5) Edge deployment for real-time inference.'
                    },
                    {
                        'id': 'competitive-advantage',
                        'text': 'What gives you a competitive advantage over existing solutions?',
                        'type': 'textarea',
                        'sample_answer': 'Competitive advantages: (1) 15% higher accuracy than current market leaders (Zebra Medical, Aidoc), (2) 10x faster processing (2 seconds vs 20 seconds), (3) Works on low-quality images common in developing countries, (4) Uncertainty quantification reduces false positives by 40%, (5) Patent-pending ensemble architecture.'
                    }
                ]
            },
            {
                'id': 'market-opportunity',
                'title': 'Market Opportunity',
                'description': 'Market analysis and commercial potential',
                'questions': [
                    {
                        'id': 'market-size',
                        'text': 'What is the market size and growth potential?',
                        'type': 'textarea',
                        'sample_answer': 'Market size: Global AI medical imaging market $4.9B (2024), growing 25% CAGR to $22.4B by 2030. Target segments: Radiology AI ($2.1B), Point-of-care diagnostics ($800M). Addressable market: 15,000 hospitals in US, 180,000 globally. Each deployment: $50K-200K annual recurring revenue.'
                    },
                    {
                        'id': 'target-customers',
                        'text': 'Who are your target customers and their pain points?',
                        'type': 'textarea',
                        'sample_answer': 'Target customers: (1) Hospital radiology departments (radiologist shortage: 30,000 needed by 2030), (2) Urgent care centers (need rapid triage), (3) Telemedicine companies (remote diagnostics), (4) International NGOs (resource-limited settings). Pain points: diagnostic delays, high costs, inconsistent quality, radiologist burnout.'
                    },
                    {
                        'id': 'go-to-market',
                        'text': 'What is your go-to-market strategy and business model?',
                        'type': 'textarea',
                        'sample_answer': 'Go-to-market: (1) SaaS subscription model ($5-15 per scan), (2) Pilot programs with 5 health systems, (3) Channel partnerships with PACS vendors (GE, Philips), (4) International expansion via distributors. Revenue streams: software licenses, professional services, training, data analytics. Target: $10M ARR by Year 3.'
                    }
                ]
            },
            {
                'id': 'phase-i-objectives',
                'title': 'Phase I Objectives',
                'description': 'Specific Phase I goals and deliverables',
                'questions': [
                    {
                        'id': 'research-objectives',
                        'text': 'What are your specific Phase I research and development objectives?',
                        'type': 'textarea',
                        'sample_answer': 'Phase I objectives: (1) Develop prototype AI system with 92%+ accuracy on pneumonia detection, (2) Implement uncertainty quantification algorithms, (3) Create FDA pre-submission package, (4) Validate on 50,000 diverse chest X-rays, (5) Develop edge deployment capabilities, (6) File 2 patent applications.'
                    },
                    {
                        'id': 'technical-milestones',
                        'text': 'What are the key technical milestones and success criteria?',
                        'type': 'textarea',
                        'sample_answer': 'Technical milestones: Month 3: Baseline model achieving 90% accuracy. Month 6: Uncertainty quantification implementation. Month 9: Edge optimization complete. Month 12: Prototype validation on clinical dataset. Success criteria: >92% sensitivity, <5% false positive rate, <2 second processing time, deployment on standard hardware.'
                    },
                    {
                        'id': 'deliverables',
                        'text': 'What are the key Phase I deliverables and outcomes?',
                        'type': 'textarea',
                        'sample_answer': 'Deliverables: (1) Working prototype software with user interface, (2) Validation report on 50K+ cases, (3) Intellectual property portfolio (2 patents filed), (4) FDA pre-submission meeting summary, (5) Technical documentation and user manuals, (6) Phase II proposal for clinical trials and commercialization.'
                    }
                ]
            },
            {
                'id': 'commercialization-plan',
                'title': 'Commercialization Plan',
                'description': 'Commercial strategy and Phase II pathway',
                'questions': [
                    {
                        'id': 'phase-ii-strategy',
                        'text': 'What is your Phase II commercialization strategy?',
                        'type': 'textarea',
                        'sample_answer': 'Phase II strategy: (1) Clinical validation study at 3 hospitals (n=10,000 patients), (2) FDA 510(k) clearance submission, (3) Commercial pilot with 2 health systems, (4) Series A fundraising ($5M target), (5) Scale manufacturing and sales team, (6) International regulatory approvals (CE mark, Health Canada).'
                    },
                    {
                        'id': 'revenue-projections',
                        'text': 'What are your revenue projections and business metrics?',
                        'type': 'textarea',
                        'sample_answer': 'Revenue projections: Year 1 (Phase II): $500K pilot revenue. Year 2: $2.5M (10 customers, avg $250K). Year 3: $8M (40 customers). Year 5: $25M (100+ customers). Key metrics: $150K average contract value, 95% retention rate, 40% gross margins, customer acquisition cost $25K, lifetime value $800K.'
                    },
                    {
                        'id': 'funding-strategy',
                        'text': 'What is your funding strategy beyond SBIR?',
                        'type': 'textarea',
                        'sample_answer': 'Funding strategy: SBIR Phase I ($500K) + Phase II ($2M) provides 24-month runway. Year 2: Series A ($5M from healthcare VCs), Year 4: Series B ($15M for international expansion). Strategic partnerships with medical device companies for co-development and distribution. Revenue-based financing for growth capital.'
                    }
                ]
            },
            {
                'id': 'team-capabilities',
                'title': 'Team and Capabilities',
                'description': 'Team qualifications and company capabilities',
                'questions': [
                    {
                        'id': 'key-personnel',
                        'text': 'Who are your key team members and their qualifications?',
                        'type': 'textarea',
                        'sample_answer': 'Key team: CEO Dr. Jennifer Wu (MD/PhD, 12 years radiology, former Google Health), CTO Alex Chen (CS PhD Stanford, ex-Tesla Autopilot lead), VP Engineering Maria Lopez (10 years medical device development), Chief Medical Officer Dr. Robert Kim (radiologist, 500+ publications). Advisory board: 3 hospital CIOs, 2 radiology department heads.'
                    },
                    {
                        'id': 'company-capabilities',
                        'text': 'What are your company capabilities and resources?',
                        'type': 'textarea',
                        'sample_answer': 'Company capabilities: (1) AI/ML expertise: 8 PhD data scientists, (2) Medical device experience: FDA regulatory consultant, quality systems, (3) Clinical network: partnerships with 5 health systems, (4) Computing infrastructure: AWS credits, GPU clusters, (5) IP portfolio: 2 pending patents, freedom to operate analysis complete.'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'DOE Energy Research Grant',
        'description': 'Department of Energy research grant proposal template',
        'category': 'grant',
        'sections': [
            {
                'id': 'project-overview',
                'title': 'Project Overview',
                'description': 'Energy research project description',
                'questions': [
                    {
                        'id': 'energy-challenge',
                        'text': 'What energy challenge or opportunity does your research address?',
                        'type': 'textarea',
                        'sample_answer': 'Addresses critical challenge in renewable energy storage: developing next-generation solid-state batteries with 3x energy density and 10x longer lifespan than current lithium-ion technology. Breakthrough could enable 500-mile electric vehicle range and grid-scale renewable storage, accelerating clean energy transition.'
                    },
                    {
                        'id': 'research-innovation',
                        'text': 'What is your key research innovation and scientific approach?',
                        'type': 'textarea',
                        'sample_answer': 'Innovation: Novel ceramic electrolyte materials with unprecedented ionic conductivity (10^-2 S/cm at room temperature) using AI-designed crystal structures. Approach combines high-throughput computational screening, machine learning-guided synthesis, and advanced characterization to identify optimal compositions for solid-state battery applications.'
                    },
                    {
                        'id': 'energy-impact',
                        'text': 'What is the potential energy and environmental impact?',
                        'type': 'textarea',
                        'sample_answer': 'Energy impact: 40% reduction in battery costs, enabling $50/kWh energy storage target. Environmental impact: Eliminates toxic liquid electrolytes, reduces mining needs by 60% through higher efficiency. Market impact: $85B solid-state battery market by 2035, supporting 100% renewable grid and EV mass adoption.'
                    }
                ]
            },
            {
                'id': 'technical-approach',
                'title': 'Technical Approach',
                'description': 'Detailed technical methodology',
                'questions': [
                    {
                        'id': 'research-methodology',
                        'text': 'Describe your detailed technical approach and methodology',
                        'type': 'textarea',
                        'sample_answer': 'Methodology: (1) AI-driven materials discovery using density functional theory and machine learning models trained on 50,000+ crystal structures, (2) High-throughput synthesis using combinatorial thin-film deposition, (3) Advanced characterization (X-ray diffraction, impedance spectroscopy, cryo-EM), (4) Full-cell prototype testing under automotive conditions.'
                    },
                    {
                        'id': 'experimental-plan',
                        'text': 'What is your experimental plan and timeline?',
                        'type': 'textarea',
                        'sample_answer': 'Experimental plan: Year 1: Computational screening and synthesis of 100 candidate materials. Year 2: Optimization of top 10 candidates, scale-up synthesis. Year 3: Full battery prototypes, automotive testing, stability studies. Timeline includes quarterly go/no-go decisions based on performance milestones (conductivity, stability, cost targets).'
                    },
                    {
                        'id': 'risk-mitigation',
                        'text': 'What are the technical risks and mitigation strategies?',
                        'type': 'textarea',
                        'sample_answer': 'Technical risks: (1) Interface stability (mitigation: protective coatings, buffer layers), (2) Manufacturing scalability (mitigation: industrial partnerships, process optimization), (3) Cost targets (mitigation: abundant element focus, simplified synthesis). Alternative pathways identified for each major risk.'
                    }
                ]
            },
            {
                'id': 'team-facilities',
                'title': 'Team and Facilities',
                'description': 'Research team and institutional capabilities',
                'questions': [
                    {
                        'id': 'principal-investigator',
                        'text': 'What are the PI qualifications and relevant experience?',
                        'type': 'textarea',
                        'sample_answer': 'PI: Dr. Emily Zhang, Professor of Materials Science, MIT. 20 years battery research experience, 180 publications (h-index 68), $25M DOE funding history. Key achievements: Pioneered lithium metal anodes (licensed to 3 companies), developed solid electrolyte synthesis methods, 15 patents in energy storage.'
                    },
                    {
                        'id': 'research-facilities',
                        'text': 'What facilities and equipment are available for this research?',
                        'type': 'textarea',
                        'sample_answer': 'Facilities: MIT Materials Research Lab with $50M equipment: high-temperature furnaces, inert atmosphere gloveboxes, electron microscopy suite (TEM, SEM), X-ray facilities (synchrotron access), battery testing stations (200 channels), computational cluster (5000 cores). DOE-funded user facility access for advanced characterization.'
                    },
                    {
                        'id': 'collaborations',
                        'text': 'What external collaborations and partnerships support this work?',
                        'type': 'textarea',
                        'sample_answer': 'Collaborations: (1) National labs: Argonne (battery testing), NREL (device modeling), (2) Industry: Tesla (automotive requirements), CATL (manufacturing insights), (3) International: Toyota Central R&D (solid-state expertise), (4) Academic: Stanford (AI materials discovery), Georgia Tech (scale-up processes).'
                    }
                ]
            },
            {
                'id': 'budget-management',
                'title': 'Budget and Management',
                'description': 'Budget justification and project management',
                'questions': [
                    {
                        'id': 'budget-breakdown',
                        'text': 'Provide detailed budget breakdown and justification',
                        'type': 'textarea',
                        'sample_answer': 'Total 3-year budget: $1.5M. Personnel (55%): $825K (PI 20% AY + summer, 2 postdocs, 3 PhD students). Equipment (25%): $375K (synthesis equipment, testing systems). Materials (15%): $225K (precursor chemicals, substrates). Travel (5%): $75K (conferences, collaborations). Cost-effective leveraging of existing $5M lab infrastructure.'
                    },
                    {
                        'id': 'project-management',
                        'text': 'How will you manage the project and track progress?',
                        'type': 'textarea',
                        'sample_answer': 'Management approach: Quarterly milestones with go/no-go decisions, monthly team meetings, external advisory board reviews (semi-annual). Progress tracking: Key performance indicators (conductivity, stability, cost per kWh), risk register updates, publication/patent metrics. DOE reporting: annual progress reports, data management plan compliance.'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'European Research Council (ERC) Grant',
        'description': 'ERC Advanced Grant proposal template for European researchers',
        'category': 'grant',
        'sections': [
            {
                'id': 'excellence',
                'title': 'Scientific Excellence',
                'description': 'Ground-breaking nature and ambition of the research',
                'questions': [
                    {
                        'id': 'research-vision',
                        'text': 'What is your ground-breaking research vision and ambitious scientific goal?',
                        'type': 'textarea',
                        'sample_answer': 'Revolutionary vision: Create first complete digital twin of human brain metabolism to unlock personalized treatments for neurological disorders. Ambitious goal: Integrate 10^11 neurons with real-time metabolic modeling, enabling prediction of therapeutic outcomes with 95% accuracy. This paradigm shift from static to dynamic brain modeling could transform neuroscience and medicine.'
                    },
                    {
                        'id': 'breakthrough-concept',
                        'text': 'What is your breakthrough concept and why is it beyond current state-of-the-art?',
                        'type': 'textarea',
                        'sample_answer': 'Breakthrough concept: Multi-scale computational framework combining quantum molecular dynamics, cellular metabolism, and network neuroscience across 12 orders of magnitude (10^-10 to 10^2 meters). Beyond state-of-art: Current models address single scales; our approach uniquely integrates molecular, cellular, and systems levels with unprecedented temporal resolution (microseconds to years).'
                    },
                    {
                        'id': 'scientific-innovation',
                        'text': 'What are the key scientific innovations and methodological advances?',
                        'type': 'textarea',
                        'sample_answer': 'Key innovations: (1) Quantum-classical hybrid algorithms for protein folding in neural membranes, (2) AI-driven metabolic flux analysis using mass spectrometry imaging, (3) Real-time brain organoid validation platform, (4) Novel mathematical frameworks for cross-scale information flow, (5) Personalized brain models from individual neuroimaging and omics data.'
                    }
                ]
            },
            {
                'id': 'impact',
                'title': 'Impact',
                'description': 'Scientific and societal impact of the research',
                'questions': [
                    {
                        'id': 'scientific-impact',
                        'text': 'What will be the scientific impact and advancement of knowledge?',
                        'type': 'textarea',
                        'sample_answer': 'Scientific impact: Establishes new field of "Computational Neurometabolism" bridging neuroscience, systems biology, and precision medicine. Knowledge advancement: First mechanistic understanding of brain energy dynamics in health/disease. Expected 50+ high-impact publications, 10+ patents, new theoretical frameworks adopted by global research community.'
                    },
                    {
                        'id': 'societal-benefits',
                        'text': 'What are the broader societal and economic benefits?',
                        'type': 'textarea',
                        'sample_answer': 'Societal benefits: Personalized treatments for 50M Europeans with neurological disorders (Alzheimers, Parkinsons, epilepsy). Economic impact: €200B annual healthcare savings through precision medicine. Drug development acceleration: 50% reduction in clinical trial failures. Educational impact: Training 20+ PhD students in interdisciplinary computational neuroscience.'
                    },
                    {
                        'id': 'long-term-vision',
                        'text': 'What is your long-term vision and potential for future developments?',
                        'type': 'textarea',
                        'sample_answer': 'Long-term vision: "Brain-as-a-Service" platform enabling virtual clinical trials and personalized treatment optimization. Future developments: Extension to psychiatric disorders, brain-computer interfaces, cognitive enhancement. Spin-off companies, EU leadership in computational neuroscience, contribution to Human Brain Project 2.0 and European digital health initiatives.'
                    }
                ]
            },
            {
                'id': 'methodology',
                'title': 'Methodology',
                'description': 'Research methodology and experimental approach',
                'questions': [
                    {
                        'id': 'research-approach',
                        'text': 'Describe your overall research approach and methodology',
                        'type': 'textarea',
                        'sample_answer': 'Methodology: Multi-disciplinary approach combining computational modeling, experimental validation, and clinical translation. Phase 1: Develop multi-scale computational framework (Years 1-2). Phase 2: Experimental validation using brain organoids and animal models (Years 2-4). Phase 3: Clinical validation and personalization algorithms (Years 4-5). Iterative model refinement throughout.'
                    },
                    {
                        'id': 'work-packages',
                        'text': 'What are your key work packages and their interdependencies?',
                        'type': 'textarea',
                        'sample_answer': 'Work packages: WP1-Quantum molecular dynamics (12 months), WP2-Cellular metabolism modeling (18 months), WP3-Network integration (24 months), WP4-Experimental validation (36 months), WP5-Clinical translation (24 months). Critical path: WP1→WP2→WP3 for model development; WP4 validates each component; WP5 integrates for clinical application.'
                    },
                    {
                        'id': 'risk-management',
                        'text': 'What are the main risks and your mitigation strategies?',
                        'type': 'textarea',
                        'sample_answer': 'Main risks: (1) Computational complexity (mitigation: quantum computing partnerships, algorithmic optimization), (2) Model validation challenges (mitigation: multiple experimental platforms, statistical validation frameworks), (3) Clinical translation barriers (mitigation: regulatory consultants, clinical advisory board). Contingency plans for each work package.'
                    }
                ]
            },
            {
                'id': 'pi-profile',
                'title': 'Principal Investigator Profile',
                'description': 'PI qualifications and track record',
                'questions': [
                    {
                        'id': 'pi-excellence',
                        'text': 'Demonstrate your scientific excellence and leadership capabilities',
                        'type': 'textarea',
                        'sample_answer': 'Scientific excellence: Professor of Computational Neuroscience, ETH Zurich. 200+ publications (h-index 75), €15M research funding. Pioneered brain network modeling methods used by 1000+ researchers globally. Leadership: Director of European Brain Simulation Initiative, Editorial Board Nature Neuroscience, 50+ invited keynotes at international conferences.'
                    },
                    {
                        'id': 'relevant-experience',
                        'text': 'What is your most relevant experience for this ambitious project?',
                        'type': 'textarea',
                        'sample_answer': 'Relevant experience: 15 years developing multi-scale brain models, pioneer in computational neurometabolism. Key achievements: First whole-brain metabolic network (Nature, 2020), quantum effects in neural computation (Science, 2022). Previous ERC Starting Grant success (2018-2023). Strong track record in interdisciplinary collaboration and technology transfer.'
                    },
                    {
                        'id': 'team-building',
                        'text': 'How will you build and lead the research team?',
                        'type': 'textarea',
                        'sample_answer': 'Team building strategy: Recruit 3 senior postdocs (computational biology, quantum chemistry, clinical neuroscience), 6 PhD students across disciplines. Leadership approach: Weekly team meetings, quarterly retreats, individual mentoring plans. External collaborations: Harvard Medical School (clinical data), IBM Research (quantum computing), pharmaceutical partners for validation.'
                    }
                ]
            },
            {
                'id': 'resources-environment',
                'title': 'Resources and Environment',
                'description': 'Institutional support and research environment',
                'questions': [
                    {
                        'id': 'institutional-support',
                        'text': 'What institutional support and infrastructure is available?',
                        'type': 'textarea',
                        'sample_answer': 'Institutional support: ETH Zurich commitment of €2M matching funds, dedicated 500m² laboratory space, computing cluster (10,000 cores), quantum computing access through IBM partnership. Core facilities: Advanced neuroimaging (7T MRI), mass spectrometry, brain organoid platform. Administrative support: dedicated grants management, technology transfer office.'
                    },
                    {
                        'id': 'research-environment',
                        'text': 'How does the research environment foster interdisciplinary excellence?',
                        'type': 'textarea',
                        'sample_answer': 'Research environment: ETH Zurich ranks #1 in Europe for interdisciplinary research. Active collaborations across 5 departments (Computer Science, Biology, Physics, Medicine, Engineering). Proximity to University Hospital Zurich for clinical translation. Rich ecosystem: 50+ biotech companies, venture capital access, regulatory expertise for medical device development.'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Gates Foundation Global Health Grant',
        'description': 'Bill & Melinda Gates Foundation global health initiative grant template',
        'category': 'grant',
        'sections': [
            {
                'id': 'global-health-challenge',
                'title': 'Global Health Challenge',
                'description': 'Problem definition and health impact',
                'questions': [
                    {
                        'id': 'health-burden',
                        'text': 'What global health challenge does your project address and what is its burden?',
                        'type': 'textarea',
                        'sample_answer': 'Addresses tuberculosis (TB) diagnostic delays in sub-Saharan Africa affecting 2.5M people annually. Current challenge: 40% of TB cases undiagnosed due to lack of rapid, affordable diagnostics in rural settings. Health burden: 1.5M preventable deaths yearly, $12B economic impact. Our innovation targets 500M people in resource-limited settings lacking laboratory infrastructure.'
                    },
                    {
                        'id': 'target-population',
                        'text': 'Who is your target population and how will they benefit?',
                        'type': 'textarea',
                        'sample_answer': 'Target population: Rural populations in 15 sub-Saharan African countries with limited healthcare access. Primary beneficiaries: 50M people at TB risk, 500,000 annual suspected cases. Benefits: 90% reduction in diagnostic time (6 weeks to 2 hours), 60% cost reduction vs existing tests, accessible at village health posts. Secondary benefits: reduced transmission, improved treatment outcomes.'
                    },
                    {
                        'id': 'equity-considerations',
                        'text': 'How does your approach address health equity and reach marginalized populations?',
                        'type': 'textarea',
                        'sample_answer': 'Equity focus: Designed for hardest-to-reach populations including women, children, rural communities, and those living in extreme poverty. Approach: Mobile testing units, female community health workers, culturally appropriate training materials in local languages. Pricing: <$5 per test vs $25 for existing diagnostics. Gender equity: 50% female field staff, pregnancy-safe testing protocols.'
                    }
                ]
            },
            {
                'id': 'innovative-solution',
                'title': 'Innovative Solution',
                'description': 'Technical innovation and approach',
                'questions': [
                    {
                        'id': 'solution-description',
                        'text': 'Describe your innovative solution and how it addresses the challenge',
                        'type': 'textarea',
                        'sample_answer': 'Innovation: Smartphone-based AI diagnostic platform using cough sound analysis and chest imaging for TB detection. Solution combines: (1) AI algorithms trained on 100,000+ cough recordings, (2) Low-cost smartphone attachment for chest X-ray enhancement, (3) Cloud-based analysis with offline capability, (4) Integration with national health systems for case reporting and treatment tracking.'
                    },
                    {
                        'id': 'technical-innovation',
                        'text': 'What are the key technical innovations and scientific breakthroughs?',
                        'type': 'textarea',
                        'sample_answer': 'Technical breakthroughs: (1) Novel deep learning architecture achieving 94% TB detection accuracy from cough sounds alone, (2) Image enhancement algorithms improving smartphone X-ray quality 10-fold, (3) Federated learning enabling model improvement across sites while preserving privacy, (4) Battery-efficient edge computing for 7-day operation without charging.'
                    },
                    {
                        'id': 'scalability-potential',
                        'text': 'How will your solution scale to reach millions of people?',
                        'type': 'textarea',
                        'sample_answer': 'Scalability strategy: (1) Partnership with mobile network operators for distribution (MTN, Vodafone), (2) Integration with existing community health worker programs, (3) Open-source platform enabling local adaptation, (4) Manufacturing partnerships for <$100 device cost, (5) Government adoption through WHO pre-qualification process. Target: 10,000 devices deployed across 15 countries by Year 5.'
                    }
                ]
            },
            {
                'id': 'implementation-strategy',
                'title': 'Implementation Strategy',
                'description': 'Deployment plan and partnership approach',
                'questions': [
                    {
                        'id': 'implementation-plan',
                        'text': 'What is your detailed implementation plan and timeline?',
                        'type': 'textarea',
                        'sample_answer': 'Implementation timeline: Year 1: Prototype development and validation in 3 pilot sites (Kenya, Nigeria, Tanzania). Year 2: Clinical validation study (n=10,000 patients), regulatory approvals. Year 3: Scale-up manufacturing, train 1,000 community health workers. Years 4-5: Full deployment across 15 countries, health system integration, sustainability planning.'
                    },
                    {
                        'id': 'partnerships',
                        'text': 'What key partnerships will enable successful implementation?',
                        'type': 'textarea',
                        'sample_answer': 'Key partnerships: (1) Government: Ministries of Health in target countries, (2) Implementation: Partners in Health, Médecins Sans Frontières for field deployment, (3) Technical: WHO for standards development, (4) Manufacturing: local production partners, (5) Funding: co-investment from USAID, Wellcome Trust, (6) Academic: local universities for research capacity building.'
                    },
                    {
                        'id': 'sustainability-plan',
                        'text': 'How will you ensure long-term sustainability and local ownership?',
                        'type': 'textarea',
                        'sample_answer': 'Sustainability approach: (1) Local manufacturing capabilities in 3 African countries, (2) Training local technical teams for maintenance and support, (3) Integration with national health information systems, (4) Revenue model: government procurement + fee-for-service for private sector, (5) IP strategy: open-source core technology with local adaptation rights, (6) 10-year support commitment with declining external funding.'
                    }
                ]
            },
            {
                'id': 'evidence-evaluation',
                'title': 'Evidence and Evaluation',
                'description': 'Research approach and impact measurement',
                'questions': [
                    {
                        'id': 'evidence-generation',
                        'text': 'How will you generate robust evidence of impact and effectiveness?',
                        'type': 'textarea',
                        'sample_answer': 'Evidence generation: Randomized controlled trial design with 50,000 participants across 100 health facilities. Primary endpoints: diagnostic accuracy, time to treatment initiation, patient outcomes. Secondary endpoints: cost-effectiveness, healthcare worker satisfaction, system strengthening impacts. Mixed-methods evaluation including quantitative health outcomes and qualitative user experience studies.'
                    },
                    {
                        'id': 'monitoring-evaluation',
                        'text': 'What is your monitoring and evaluation framework?',
                        'type': 'textarea',
                        'sample_answer': 'M&E framework: (1) Real-time data dashboard tracking device usage, diagnostic accuracy, patient outcomes, (2) Quarterly external evaluations by independent research team, (3) Cost-effectiveness analysis using DALY methodology, (4) Health system strengthening metrics, (5) Patient and provider feedback loops, (6) Annual third-party impact assessment. Target: 90% diagnostic accuracy, 80% user satisfaction.'
                    },
                    {
                        'id': 'learning-adaptation',
                        'text': 'How will you incorporate learning and adapt your approach?',
                        'type': 'textarea',
                        'sample_answer': 'Learning approach: Agile implementation with quarterly adaptation cycles. Feedback mechanisms: User advisory groups, health worker feedback platforms, patient experience surveys. Adaptation strategy: AI model continuous improvement, user interface optimization based on field feedback, training program refinement. Knowledge sharing: Open-access publications, implementation toolkit, global community of practice.'
                    }
                ]
            },
            {
                'id': 'budget-impact',
                'title': 'Budget and Value for Money',
                'description': 'Financial planning and cost-effectiveness',
                'questions': [
                    {
                        'id': 'budget-justification',
                        'text': 'Provide detailed budget breakdown and justification',
                        'type': 'textarea',
                        'sample_answer': 'Total 5-year budget: $15M. Technology development (30%): $4.5M (AI development, device engineering, manufacturing setup). Implementation (40%): $6M (field deployment, training, evaluation). Partnerships (20%): $3M (local capacity building, health system integration). Operations (10%): $1.5M (management, monitoring). Cost per beneficiary: $30 vs $200 for traditional approaches.'
                    },
                    {
                        'id': 'cost-effectiveness',
                        'text': 'How does your approach demonstrate exceptional value for money?',
                        'type': 'textarea',
                        'sample_answer': 'Value proposition: $50 cost per DALY averted vs $150 for next-best alternative. Return on investment: $1 invested saves $7 in healthcare costs and productivity gains. Efficiency gains: 95% reduction in laboratory infrastructure needs, 80% reduction in travel costs for patients. Long-term savings: $500M over 10 years through early detection and treatment.'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Wellcome Trust Biomedical Research Grant',
        'description': 'Wellcome Trust investigator award proposal template',
        'category': 'grant',
        'sections': [
            {
                'id': 'research-vision',
                'title': 'Research Vision',
                'description': 'Long-term research goals and vision',
                'questions': [
                    {
                        'id': 'scientific-vision',
                        'text': 'What is your long-term scientific vision and research program?',
                        'type': 'textarea',
                        'sample_answer': 'Vision: Revolutionize cancer immunotherapy by engineering next-generation CAR-T cells with enhanced tumor-targeting specificity and reduced toxicity. Long-term goal: Develop "smart" immune cells that can adapt to tumor evolution, remember cancer signatures, and provide lifelong protection. This paradigm shift from single-target to multi-modal adaptive immunotherapy could transform cancer treatment globally.'
                    },
                    {
                        'id': 'research-questions',
                        'text': 'What are the fundamental research questions you aim to address?',
                        'type': 'textarea',
                        'sample_answer': 'Fundamental questions: (1) How can we engineer T cells with multiple, switchable targeting mechanisms? (2) What molecular circuits enable immune memory formation against evolving tumors? (3) How do we minimize on-target, off-tumor toxicity while maintaining efficacy? (4) Can we create universal CAR-T platforms adaptable across cancer types? (5) How do tumor microenvironments influence engineered immune cell function?'
                    },
                    {
                        'id': 'transformative-potential',
                        'text': 'What is the transformative potential of your research program?',
                        'type': 'textarea',
                        'sample_answer': 'Transformative potential: (1) Scientific: Establishes new field of "Adaptive Cellular Engineering" combining synthetic biology, immunology, and AI, (2) Clinical: CAR-T therapy for 80% of solid tumors (currently <5%), (3) Global health: Affordable cell therapy manufacturing for low-resource settings, (4) Economic: $50B market impact through next-generation immunotherapies, (5) Societal: Cancer as manageable chronic disease.'
                    }
                ]
            },
            {
                'id': 'scientific-approach',
                'title': 'Scientific Approach',
                'description': 'Research methodology and innovation',
                'questions': [
                    {
                        'id': 'innovative-methods',
                        'text': 'What innovative methods and technologies will you develop or apply?',
                        'type': 'textarea',
                        'sample_answer': 'Innovative methods: (1) CRISPR-based synthetic circuits for multi-input CAR activation, (2) AI-designed protein switches responsive to tumor microenvironment, (3) Single-cell genomics for real-time immune cell state monitoring, (4) Organoid-based screening platforms for therapy optimization, (5) Computational modeling of immune-tumor evolution dynamics using game theory and machine learning.'
                    },
                    {
                        'id': 'research-strategy',
                        'text': 'Describe your research strategy and experimental approach',
                        'type': 'textarea',
                        'sample_answer': 'Strategy: Three interconnected research streams over 7 years. Stream 1: Engineer multi-input CAR circuits with AND/OR logic gates (Years 1-3). Stream 2: Develop tumor-adaptive immune memory systems (Years 2-5). Stream 3: Clinical translation and manufacturing optimization (Years 4-7). Iterative design-build-test-learn cycles using high-throughput screening and computational modeling.'
                    },
                    {
                        'id': 'risk-innovation-balance',
                        'text': 'How do you balance scientific risk-taking with delivering innovative outcomes?',
                        'type': 'textarea',
                        'sample_answer': 'Risk management: Portfolio approach with 30% high-risk/high-reward projects, 50% medium-risk innovations, 20% incremental advances ensuring deliverables. Milestone-driven go/no-go decisions at 18-month intervals. Alternative pathways identified for each major objective. Strong preliminary data reduces early-stage risks. International collaborations provide expertise and resource redundancy.'
                    }
                ]
            },
            {
                'id': 'leadership-vision',
                'title': 'Leadership and Vision',
                'description': 'Leadership approach and career development',
                'questions': [
                    {
                        'id': 'leadership-style',
                        'text': 'How will you lead your research team and foster scientific excellence?',
                        'type': 'textarea',
                        'sample_answer': 'Leadership philosophy: Collaborative, inclusive approach fostering creativity and scientific rigor. Team structure: 3 senior postdocs (immunology, synthetic biology, computational), 6 PhD students, 2 research technicians. Leadership practices: Weekly one-on-ones, monthly lab meetings, quarterly strategic reviews. Mentorship: Individual development plans, external rotation opportunities, career development workshops.'
                    },
                    {
                        'id': 'career-development',
                        'text': 'How will this award advance your career and scientific independence?',
                        'type': 'textarea',
                        'sample_answer': 'Career development: Transition from talented researcher to international leader in cellular engineering. Goals: (1) Establish unique research niche combining immunology and synthetic biology, (2) Build world-class research team and infrastructure, (3) Develop clinical translation pipeline, (4) Secure additional funding for program expansion, (5) Mentor next generation of scientist-engineers.'
                    },
                    {
                        'id': 'broader-contribution',
                        'text': 'How will you contribute to the broader scientific community and society?',
                        'type': 'textarea',
                        'sample_answer': 'Community contributions: (1) Open science: Pre-print sharing, open-source computational tools, public datasets, (2) Training: International workshops on cellular engineering, online courses, (3) Diversity: Female scientist role model, underrepresented minority recruitment, (4) Translation: Industry partnerships, patent sharing for global access, (5) Policy: Science advisory roles, regulatory guidance development.'
                    }
                ]
            },
            {
                'id': 'track-record',
                'title': 'Track Record and Environment',
                'description': 'Past achievements and institutional support',
                'questions': [
                    {
                        'id': 'research-achievements',
                        'text': 'What are your key research achievements and scientific contributions?',
                        'type': 'textarea',
                        'sample_answer': 'Key achievements: (1) Pioneered logic-gated CAR-T cells (Nature, 2022), (2) Developed AI-designed protein switches (Science, 2023), (3) 45 publications, h-index 35, 3,000+ citations, (4) 5 patents in cellular engineering, (5) $3M previous funding success, (6) Recipient of prestigious Young Investigator Awards. Research adopted by 20+ labs globally, 2 technologies licensed to biotech companies.'
                    },
                    {
                        'id': 'institutional-environment',
                        'text': 'How does your institutional environment support your research program?',
                        'type': 'textarea',
                        'sample_answer': 'Institutional support: University of Cambridge provides £1M matching funds, dedicated 1000m² GMP facility for cell manufacturing, core facilities (genomics, imaging, flow cytometry), regulatory support for clinical translation. Collaborative environment: Cancer Research UK Cambridge Institute, close ties with Addenbrookes Hospital, 50+ immunology and cancer biology faculty. Administrative support: dedicated grants team, technology transfer office.'
                    },
                    {
                        'id': 'collaborations',
                        'text': 'What key collaborations will enhance your research program?',
                        'type': 'textarea',
                        'sample_answer': 'Strategic collaborations: (1) Clinical: Memorial Sloan Kettering (CAR-T trials), (2) Industry: Novartis (manufacturing), Genentech (target discovery), (3) Academic: MIT (synthetic biology), Stanford (AI/ML), (4) International: University of Tokyo (organoid models), Max Planck (structural biology), (5) Global health: Partners in Health (low-resource implementation).'
                    }
                ]
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Innovation Fund Corporate Grant',
        'description': 'Corporate innovation fund grant proposal template',
        'category': 'grant',
        'sections': [
            {
                'id': 'innovation-opportunity',
                'title': 'Innovation Opportunity',
                'description': 'Market opportunity and innovation potential',
                'questions': [
                    {
                        'id': 'market-opportunity',
                        'text': 'What market opportunity does your innovation address?',
                        'type': 'textarea',
                        'sample_answer': 'Market opportunity: $50B autonomous vehicle sensor market growing 35% annually. Key gap: Current LiDAR systems cost $10,000+ and fail in adverse weather. Our breakthrough: Solid-state LiDAR with 100x cost reduction and all-weather capability. Target market: 100M vehicles annually by 2030, capturing 20% market share equals $2B revenue opportunity.'
                    },
                    {
                        'id': 'competitive-landscape',
                        'text': 'How does your innovation differentiate from existing solutions?',
                        'type': 'textarea',
                        'sample_answer': 'Competitive differentiation: (1) Cost: $100 vs $10,000 for mechanical LiDAR, (2) Performance: 200m range in rain/fog vs 50m for competitors, (3) Size: 1cm³ vs 10cm³ package, (4) Reliability: No moving parts, 10-year lifespan, (5) Manufacturing: Silicon photonics enable mass production using existing semiconductor fabs. Patent portfolio: 15 pending applications creating IP moat.'
                    },
                    {
                        'id': 'strategic-alignment',
                        'text': 'How does this innovation align with corporate strategic priorities?',
                        'type': 'textarea',
                        'sample_answer': 'Strategic alignment with automotive corporate partner: (1) Autonomous driving roadmap: Essential sensor for Level 4/5 autonomy, (2) Cost reduction goals: Enables $30,000 autonomous vehicles vs $100,000 today, (3) Supply chain: Reduces dependence on single LiDAR suppliers, (4) Manufacturing synergies: Leverage existing semiconductor partnerships, (5) Market position: First-mover advantage in affordable autonomous vehicles.'
                    }
                ]
            },
            {
                'id': 'technical-innovation',
                'title': 'Technical Innovation',
                'description': 'Technology description and development plan',
                'questions': [
                    {
                        'id': 'core-technology',
                        'text': 'Describe your core technology and key technical breakthroughs',
                        'type': 'textarea',
                        'sample_answer': 'Core technology: Silicon photonic LiDAR using frequency-modulated continuous wave (FMCW) architecture. Key breakthroughs: (1) Novel integrated laser design achieving 1W output power, (2) AI-enhanced signal processing for sub-millimeter resolution, (3) Metamaterial optical antennas for 120° field of view, (4) Chip-scale packaging withstanding automotive temperature ranges (-40°C to +125°C).'
                    },
                    {
                        'id': 'development-roadmap',
                        'text': 'What is your technology development roadmap and milestones?',
                        'type': 'textarea',
                        'sample_answer': 'Development roadmap: Phase 1 (6 months): Prototype demonstration with 50m range. Phase 2 (12 months): Automotive-grade packaging and testing. Phase 3 (18 months): Pilot production line setup. Phase 4 (24 months): Customer validation and design-for-manufacturing optimization. Key milestones: Range targets (50m→100m→200m), cost reduction (1000x→100x→final target), environmental testing (IP67, vibration, EMC).'
                    },
                    {
                        'id': 'ip-protection',
                        'text': 'What is your intellectual property strategy and protection plan?',
                        'type': 'textarea',
                        'sample_answer': 'IP strategy: Comprehensive patent portfolio covering (1) Silicon photonic architecture, (2) Signal processing algorithms, (3) Packaging and thermal management, (4) Manufacturing processes. Current status: 5 patents filed, 10 in preparation. Geographic coverage: US, EU, China, Japan. Trade secrets: Proprietary algorithms and manufacturing know-how. Licensing strategy: Exclusive automotive license to corporate partner, non-exclusive for other markets.'
                    }
                ]
            },
            {
                'id': 'business-model',
                'title': 'Business Model and Commercialization',
                'description': 'Go-to-market strategy and business planning',
                'questions': [
                    {
                        'id': 'business-model',
                        'text': 'What is your business model and revenue strategy?',
                        'type': 'textarea',
                        'sample_answer': 'Business model: B2B hardware sales with software/service components. Revenue streams: (1) Hardware sales: $100-500 per unit depending on volume, (2) Software licensing: AI algorithms for enhanced processing, (3) Service contracts: Calibration and maintenance, (4) Data analytics: Anonymized driving pattern insights. Pricing strategy: Premium pricing initially, volume discounts for OEM partnerships.'
                    },
                    {
                        'id': 'go-to-market',
                        'text': 'Describe your go-to-market strategy and customer acquisition plan',
                        'type': 'textarea',
                        'sample_answer': 'Go-to-market: (1) Phase 1: Tier-1 automotive suppliers (Bosch, Continental) as channel partners, (2) Phase 2: Direct OEM relationships (Tesla, BMW, Toyota), (3) Phase 3: Adjacent markets (robotics, drones, security). Customer acquisition: Trade show demonstrations, pilot programs, reference customers. Sales strategy: Technical sales team with automotive industry experience, application engineering support.'
                    },
                    {
                        'id': 'financial-projections',
                        'text': 'What are your financial projections and funding requirements?',
                        'type': 'textarea',
                        'sample_answer': 'Financial projections: Year 1: $500K revenue (pilot sales), Year 3: $25M (production ramp), Year 5: $200M (market penetration). Funding requirements: $15M total over 3 years. Series A: $5M (prototype development), Series B: $10M (manufacturing scale-up). Use of funds: R&D (40%), Manufacturing setup (35%), Sales/Marketing (15%), Operations (10%). Break-even: Month 30, positive cash flow: Month 36.'
                    }
                ]
            },
            {
                'id': 'team-execution',
                'title': 'Team and Execution',
                'description': 'Team capabilities and execution plan',
                'questions': [
                    {
                        'id': 'team-qualifications',
                        'text': 'What are the key qualifications of your founding team?',
                        'type': 'textarea',
                        'sample_answer': 'Founding team: CEO Dr. Sarah Kim (15 years automotive sensors, former Velodyne VP), CTO Dr. Michael Chen (PhD Silicon Photonics MIT, 20 patents), VP Engineering Lisa Wong (10 years semiconductor manufacturing, ex-Intel). Advisory board: Former BMW Chief Engineer, Andreessen Horowitz Partner, Stanford Professor (Silicon Photonics pioneer). Team combines deep technical expertise with automotive industry experience and startup scaling knowledge.'
                    },
                    {
                        'id': 'execution-capabilities',
                        'text': 'How will you execute on your development and commercialization plan?',
                        'type': 'textarea',
                        'sample_answer': 'Execution approach: Agile development with monthly sprints and quarterly reviews. Manufacturing strategy: Partnership with tier-1 semiconductor foundry (TSMC) for chip production, contract manufacturer for assembly. Quality systems: ISO/TS 16949 automotive certification, six-sigma processes. Risk mitigation: Multiple supplier relationships, extensive testing protocols, customer co-development agreements reducing market risk.'
                    },
                    {
                        'id': 'scaling-strategy',
                        'text': 'What is your strategy for scaling operations and maintaining quality?',
                        'type': 'textarea',
                        'sample_answer': 'Scaling strategy: (1) Manufacturing: Automated assembly lines capable of 1M units/year by Year 3, (2) Quality: Statistical process control, automated testing, customer feedback loops, (3) Team: Hire experienced automotive executives, expand R&D team to 50+ engineers, (4) Systems: ERP implementation, supply chain management, customer relationship management. Target: 99.9% quality levels required for automotive applications.'
                    }
                ]
            },
            {
                'id': 'partnership-synergies',
                'title': 'Partnership and Synergies',
                'description': 'Corporate partnership benefits and synergies',
                'questions': [
                    {
                        'id': 'mutual-benefits',
                        'text': 'What are the mutual benefits of partnering with the corporate sponsor?',
                        'type': 'textarea',
                        'sample_answer': 'Mutual benefits: Corporate gains: (1) Access to breakthrough sensor technology providing competitive advantage, (2) Cost reduction enabling affordable autonomous vehicles, (3) Supply chain diversification reducing vendor risk, (4) First-mover advantage in next-generation sensing. Startup gains: (1) $50M+ purchase commitment providing revenue visibility, (2) Automotive expertise and validation, (3) Manufacturing scale and supply chain access, (4) Global market reach through OEM relationships.'
                    },
                    {
                        'id': 'collaboration-model',
                        'text': 'What is the proposed collaboration model and governance structure?',
                        'type': 'textarea',
                        'sample_answer': 'Collaboration model: Joint development agreement with milestone-based funding and performance targets. Governance: Quarterly business reviews, joint technical committees, shared IP arrangements for co-developed technologies. Corporate involvement: Observer board seat, technical advisory role, customer introduction facilitation. Exit strategy: Corporate has right-of-first-refusal for acquisition, licensing agreements for technology access.'
                    },
                    {
                        'id': 'long-term-vision',
                        'text': 'What is the long-term vision for the partnership and market expansion?',
                        'type': 'textarea',
                        'sample_answer': 'Long-term vision: Strategic partnership enabling corporate leadership in autonomous vehicle sensors. 5-year goals: (1) 30% market share in automotive LiDAR, (2) Expansion to robotics and industrial automation markets worth additional $10B, (3) Next-generation sensing technologies (4D imaging, AI-integrated sensors), (4) Global manufacturing footprint, (5) Potential acquisition creating vertically integrated sensor capability for corporate partner.'
                    }
                ]
            }
        ]
    }
]

# Helper functions for working with grant templates
def get_template_by_id(template_id):
    """Get a specific template by ID"""
    for template in GRANT_TEMPLATES:
        if template['id'] == template_id:
            return template
    return None

def get_templates_by_category(category):
    """Get all templates in a specific category"""
    return [template for template in GRANT_TEMPLATES if template['category'] == category]

def get_template_names():
    """Get list of all template names"""
    return [template['name'] for template in GRANT_TEMPLATES]

def search_templates(query):
    """Search templates by name, description, or content"""
    query = query.lower()
    results = []
    
    for template in GRANT_TEMPLATES:
        # Search in name and description
        if (query in template['name'].lower() or 
            query in template['description'].lower()):
            results.append(template)
            continue
            
        # Search in section content
        for section in template['sections']:
            if (query in section['title'].lower() or 
                query in section['description'].lower()):
                results.append(template)
                break
                
            # Search in questions
            for question in section['questions']:
                if (query in question['text'].lower() or 
                    query in question.get('sample_answer', '').lower()):
                    results.append(template)
                    break
    
    return results

def validate_template_structure(template):
    """Validate that a template has the required structure"""
    required_fields = ['id', 'name', 'description', 'category', 'sections']
    
    for field in required_fields:
        if field not in template:
            return False, f"Missing required field: {field}"
    
    for section in template['sections']:
        required_section_fields = ['id', 'title', 'description', 'questions']
        for field in required_section_fields:
            if field not in section:
                return False, f"Section missing required field: {field}"
        
        for question in section['questions']:
            required_question_fields = ['id', 'text', 'type']
            for field in required_question_fields:
                if field not in question:
                    return False, f"Question missing required field: {field}"
    
    return True, "Template structure is valid"

# Export template data for use in other modules
__all__ = [
    'GRANT_TEMPLATES',
    'get_template_by_id',
    'get_templates_by_category', 
    'get_template_names',
    'search_templates',
    'validate_template_structure'
]