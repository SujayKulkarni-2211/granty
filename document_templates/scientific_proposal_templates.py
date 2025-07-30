# document_templates/scientific_proposal_templates.py
import uuid

SCIENTIFIC_PROPOSAL_TEMPLATES = [
    {
        'id': str(uuid.uuid4()),
        'name': 'Academic Research Proposal',
        'description': 'Comprehensive academic research proposal template',
        'category': 'scientific_proposal',
        'sections': [
            {
                'id': 'title-abstract',
                'title': 'Title and Abstract',
                'description': 'Project title and executive summary',
                'questions': [
                    {
                        'id': 'project-title',
                        'text': 'What is your research project title?',
                        'type': 'text',
                        'sample_answer': 'Novel Approaches to Machine Learning in Climate Change Prediction'
                    },
                    {
                        'id': 'abstract',
                        'text': 'Provide a concise abstract (250-300 words) summarizing your research objectives, methodology, and expected outcomes.',
                        'type': 'textarea',
                        'sample_answer': 'This research investigates the application of advanced machine learning algorithms to improve climate change prediction models. The study aims to develop hybrid neural network architectures that integrate satellite data, ground-based measurements, and historical climate records to enhance prediction accuracy by 15-20%. Using a combination of convolutional neural networks and transformer models, we will process multi-modal climate data from the past 50 years. The methodology includes data preprocessing, feature engineering, model development, and validation against existing climate models. Expected outcomes include improved prediction accuracy, reduced computational costs, and novel insights into climate pattern recognition. This research contributes to climate science by providing more reliable forecasting tools for policy makers and environmental scientists.'
                    }
                ]
            },
            {
                'id': 'literature-review',
                'title': 'Literature Review and Research Gap',
                'description': 'Current research landscape and identified gaps',
                'questions': [
                    {
                        'id': 'current-state',
                        'text': 'What is the current state of research in your field? Cite key studies and their limitations.',
                        'type': 'textarea',
                        'sample_answer': 'Current climate prediction models primarily rely on physical simulation approaches (Smith et al., 2022) and traditional statistical methods (Johnson & Lee, 2021). Recent studies by Chen et al. (2023) demonstrated that ensemble methods improve accuracy by 8-12%. However, existing approaches face limitations: (1) insufficient integration of multi-modal data sources, (2) computational complexity limiting real-time applications, and (3) poor performance in extreme weather event prediction. Zhang et al. (2022) identified that current models struggle with non-linear climate interactions, while Rodriguez & Kim (2023) highlighted the need for better temporal pattern recognition in long-term forecasting.'
                    },
                    {
                        'id': 'research-gap',
                        'text': 'What specific gap in knowledge does your research address?',
                        'type': 'textarea',
                        'sample_answer': 'This research addresses three critical gaps: (1) Limited application of transformer architectures to climate data processing, (2) Lack of unified frameworks combining satellite imagery with temporal climate data, and (3) Insufficient attention to computational efficiency in real-time climate prediction systems. No previous studies have systematically explored hybrid CNN-transformer architectures specifically designed for multi-temporal climate data integration.'
                    }
                ]
            },
            {
                'id': 'objectives-hypotheses',
                'title': 'Research Objectives and Hypotheses',
                'description': 'Specific research aims and testable hypotheses',
                'questions': [
                    {
                        'id': 'primary-objective',
                        'text': 'What is your primary research objective?',
                        'type': 'textarea',
                        'sample_answer': 'To develop and validate a hybrid neural network architecture that improves climate change prediction accuracy by at least 15% compared to current state-of-the-art models, while reducing computational time by 30%.'
                    },
                    {
                        'id': 'secondary-objectives',
                        'text': 'List 3-5 secondary objectives that support your primary goal.',
                        'type': 'textarea',
                        'sample_answer': '1. Design a novel CNN-transformer hybrid architecture optimized for multi-modal climate data processing\n2. Create a comprehensive dataset integrating satellite imagery, weather station data, and oceanic measurements from 1970-2024\n3. Develop preprocessing pipelines for handling missing data and temporal inconsistencies in climate records\n4. Establish benchmark comparisons with existing climate prediction models (GCMs, statistical models)\n5. Assess model performance across different geographical regions and climate zones'
                    },
                    {
                        'id': 'hypotheses',
                        'text': 'State your testable research hypotheses.',
                        'type': 'textarea',
                        'sample_answer': 'H1: Hybrid CNN-transformer architectures will demonstrate superior performance in climate prediction tasks compared to individual CNN or transformer models alone.\nH2: Integration of multi-modal data sources (satellite, ground-based, oceanic) will improve prediction accuracy more than single-source approaches.\nH3: Attention mechanisms in transformer components will effectively capture long-term temporal dependencies in climate data spanning 50+ years.\nH4: The proposed model will maintain prediction accuracy while reducing computational requirements by at least 30% compared to ensemble methods.'
                    }
                ]
            },
            {
                'id': 'methodology',
                'title': 'Methodology and Research Design',
                'description': 'Detailed research approach and methods',
                'questions': [
                    {
                        'id': 'research-design',
                        'text': 'Describe your overall research design and approach.',
                        'type': 'textarea',
                        'sample_answer': 'This study employs a mixed-methods approach combining quantitative modeling with comparative analysis. The research design includes: (1) Data collection and preprocessing phase (6 months), (2) Model development and architecture optimization (8 months), (3) Training and validation phase (4 months), (4) Comparative evaluation and benchmarking (3 months), and (5) Analysis and interpretation (3 months). The study uses both retrospective data analysis and prospective model validation approaches.'
                    },
                    {
                        'id': 'data-collection',
                        'text': 'Detail your data collection methods, sources, and sampling strategy.',
                        'type': 'textarea',
                        'sample_answer': 'Data sources include: NASA MODIS satellite imagery (2000-2024), NOAA weather station records (1970-2024), ECMWF reanalysis data, and oceanic measurements from ARGO floats. Sampling strategy: stratified random sampling across 12 climate zones, ensuring representation of tropical, temperate, arctic, and arid regions. Data preprocessing includes quality control checks, missing value imputation using temporal interpolation, and standardization across different measurement scales and temporal resolutions.'
                    },
                    {
                        'id': 'analysis-methods',
                        'text': 'Specify your analytical methods and statistical approaches.',
                        'type': 'textarea',
                        'sample_answer': 'Analytical methods include: (1) Deep learning model development using PyTorch framework, (2) Cross-validation using temporal splitting (70% training, 15% validation, 15% testing), (3) Performance metrics: RMSE, MAE, correlation coefficients, and skill scores, (4) Statistical significance testing using t-tests and ANOVA for model comparisons, (5) Ablation studies to assess individual component contributions, (6) Uncertainty quantification using ensemble prediction intervals.'
                    }
                ]
            },
            {
                'id': 'timeline-resources',
                'title': 'Timeline and Resources',
                'description': 'Project schedule and resource requirements',
                'questions': [
                    {
                        'id': 'project-timeline',
                        'text': 'Provide a detailed timeline with major milestones.',
                        'type': 'textarea',
                        'sample_answer': 'Months 1-6: Data collection, cleaning, and preprocessing; literature review completion\nMonths 7-14: Model architecture development, hyperparameter optimization, initial training\nMonths 15-18: Model validation, performance evaluation, comparative analysis\nMonths 19-21: Results analysis, statistical testing, uncertainty assessment\nMonths 22-24: Manuscript preparation, peer review, dissemination activities\nKey milestones: M6 (Dataset ready), M14 (Model trained), M18 (Validation complete), M21 (Analysis complete), M24 (Publication submitted)'
                    },
                    {
                        'id': 'budget-resources',
                        'text': 'Outline your budget requirements and resource needs.',
                        'type': 'textarea',
                        'sample_answer': 'Total budget: $150,000 over 24 months\nPersonnel (60%): PI (25% effort), PhD student (100% effort), Research programmer (50% effort)\nEquipment (25%): GPU cluster access, cloud computing resources (AWS/Google Cloud)\nData acquisition (10%): Satellite data licenses, computing infrastructure\nTravel (3%): Conference presentations, collaboration visits\nOther (2%): Software licenses, publication fees'
                    }
                ]
            },
            {
                'id': 'expected-outcomes',
                'title': 'Expected Outcomes and Impact',
                'description': 'Anticipated results and broader implications',
                'questions': [
                    {
                        'id': 'deliverables',
                        'text': 'List specific deliverables and expected outcomes.',
                        'type': 'textarea',
                        'sample_answer': '1. Novel hybrid CNN-transformer architecture for climate prediction\n2. Comprehensive climate dataset with 50+ years of multi-modal data\n3. 3-5 peer-reviewed publications in high-impact journals\n4. Open-source software package for climate prediction\n5. Trained models achieving 15-20% improved accuracy\n6. Technical reports and documentation\n7. Conference presentations at major climate science meetings\n8. PhD dissertation completion'
                    },
                    {
                        'id': 'broader-impact',
                        'text': 'Describe the broader scientific and societal impact of your research.',
                        'type': 'textarea',
                        'sample_answer': 'This research will advance climate science by providing more accurate prediction tools, enabling better policy decisions for climate adaptation and mitigation. Societal benefits include improved disaster preparedness, agricultural planning, and water resource management. The open-source nature ensures global accessibility, particularly benefiting developing nations with limited computational resources. Scientific impact includes advancing machine learning applications in Earth sciences and establishing new benchmarks for climate model evaluation.'
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
                'id': 'trial-overview',
                'title': 'Trial Overview and Rationale',
                'description': 'Study background and justification',
                'questions': [
                    {
                        'id': 'study-title',
                        'text': 'What is your clinical trial title?',
                        'type': 'text',
                        'sample_answer': 'A Randomized, Double-Blind, Placebo-Controlled Phase II Trial of Novel Drug X in Patients with Advanced Heart Failure'
                    },
                    {
                        'id': 'medical-rationale',
                        'text': 'Provide the medical and scientific rationale for this trial.',
                        'type': 'textarea',
                        'sample_answer': 'Heart failure affects 6.2 million Americans with 5-year mortality rates exceeding 50%. Current treatments provide limited benefit for advanced stages (NYHA Class III-IV). Preclinical studies demonstrate that Drug X targets the novel SGLT2-independent pathway, showing 40% improvement in cardiac output in animal models (Johnson et al., 2023). Phase I trials confirmed safety with dose-dependent efficacy signals. This Phase II trial addresses the critical need for effective treatments in advanced heart failure, where current therapies have reached therapeutic limits.'
                    },
                    {
                        'id': 'primary-endpoint',
                        'text': 'Define your primary endpoint and justification.',
                        'type': 'textarea',
                        'sample_answer': 'Primary endpoint: Change in 6-minute walk distance (6MWD) from baseline to 12 weeks. Justification: 6MWD is a validated, clinically meaningful outcome measure in heart failure trials, correlating with quality of life and survival. A 30-meter improvement is considered clinically significant (AHA/ACC guidelines). This endpoint is objective, reproducible, and has regulatory acceptance for heart failure drug approval.'
                    }
                ]
            },
            {
                'id': 'study-design',
                'title': 'Study Design and Methodology',
                'description': 'Trial design, randomization, and procedures',
                'questions': [
                    {
                        'id': 'trial-design',
                        'text': 'Describe your trial design, including phase, randomization, and blinding.',
                        'type': 'textarea',
                        'sample_answer': 'Phase II, randomized, double-blind, placebo-controlled, parallel-group trial. Randomization: 2:1 ratio (Drug X:Placebo) using permuted block randomization (block size 6) stratified by baseline NYHA class (III vs IV) and ejection fraction (<30% vs ≥30%). Blinding: Identical capsules manufactured by certified pharmacy. Emergency unblinding procedures established with sealed envelopes. Placebo-controlled design essential for regulatory approval and eliminating bias in subjective endpoints.'
                    },
                    {
                        'id': 'participant-criteria',
                        'text': 'List detailed inclusion and exclusion criteria.',
                        'type': 'textarea',
                        'sample_answer': 'Inclusion: Age 18-80 years; NYHA Class III-IV heart failure for ≥3 months; LVEF ≤40%; stable medical therapy for ≥4 weeks; 6MWD 100-400 meters; signed informed consent.\n\nExclusion: Acute MI within 3 months; planned cardiac procedures; eGFR <30 mL/min/1.73m²; severe hepatic impairment; pregnancy/nursing; participation in other trials; inability to perform 6MWD test; severe psychiatric disorders; life expectancy <6 months due to non-cardiac causes; known hypersensitivity to study drug.'
                    },
                    {
                        'id': 'intervention-protocol',
                        'text': 'Detail the intervention protocol, dosing, and administration.',
                        'type': 'textarea',
                        'sample_answer': 'Intervention: Drug X 10mg orally twice daily vs matching placebo. Dose escalation: Start 5mg BID for 1 week, then 10mg BID if tolerated. Duration: 12 weeks treatment + 4 weeks safety follow-up. Administration: with meals to enhance absorption. Compliance monitoring: pill counts and patient diaries. Permitted co-medications: stable heart failure medications (ACE inhibitors, beta-blockers, diuretics). Prohibited: other investigational drugs, chronic steroid use >10mg/day prednisone equivalent.'
                    }
                ]
            },
            {
                'id': 'endpoints-assessments',
                'title': 'Endpoints and Assessments',
                'description': 'Outcome measures and evaluation methods',
                'questions': [
                    {
                        'id': 'secondary-endpoints',
                        'text': 'List and justify your secondary endpoints.',
                        'type': 'textarea',
                        'sample_answer': 'Secondary endpoints:\n1. Change in NYHA functional class (clinical relevance, regulatory acceptance)\n2. Kansas City Cardiomyopathy Questionnaire score (quality of life, patient-reported outcome)\n3. NT-proBNP levels (biomarker of heart failure severity, treatment response)\n4. Echocardiographic parameters: LVEF, LV volumes (cardiac function assessment)\n5. Time to first heart failure hospitalization (clinical events, healthcare utilization)\n6. Composite endpoint: death, hospitalization, or worsening heart failure (comprehensive clinical assessment)'
                    },
                    {
                        'id': 'safety-monitoring',
                        'text': 'Describe safety endpoints and monitoring procedures.',
                        'type': 'textarea',
                        'sample_answer': 'Safety endpoints: Treatment-emergent adverse events (TEAEs), serious adverse events (SAEs), laboratory abnormalities, vital signs, ECG changes, treatment discontinuations.\n\nMonitoring: Clinical visits at weeks 1, 2, 4, 8, 12, 16; laboratory tests (CBC, CMP, liver function) at each visit; ECGs at baseline, weeks 4, 12; echocardiograms at baseline and week 12. Data Safety Monitoring Board (DSMB) reviews safety data every 4 weeks. Stopping rules: >20% difference in serious cardiac events, significant hepatotoxicity (ALT >3x ULN in >10% patients), or DSMB recommendation.'
                    },
                    {
                        'id': 'assessment-schedule',
                        'text': 'Provide detailed visit schedule and assessment timeline.',
                        'type': 'textarea',
                        'sample_answer': 'Screening (Day -14 to -1): Informed consent, medical history, physical exam, labs, ECG, echo, 6MWD\nBaseline (Day 0): Randomization, vital signs, NYHA class, KCCQ, first dose\nWeek 1: Safety assessment, compliance check, dose escalation\nWeek 2: Clinical assessment, labs, adverse events\nWeek 4: Complete assessment (all endpoints), ECG, labs\nWeek 8: Clinical assessment, labs, 6MWD, KCCQ\nWeek 12: Final efficacy assessment (all endpoints), echo, labs, ECG\nWeek 16: Safety follow-up, final adverse event collection'
                    }
                ]
            },
            {
                'id': 'statistical-analysis',
                'title': 'Statistical Analysis Plan',
                'description': 'Statistical methods and sample size calculation',
                'questions': [
                    {
                        'id': 'sample-size',
                        'text': 'Provide sample size calculation with assumptions.',
                        'type': 'textarea',
                        'sample_answer': 'Sample size calculation: Detecting 30-meter difference in 6MWD change (Drug X vs Placebo)\nAssumptions: Standard deviation = 60 meters (based on literature), Power = 80%, Alpha = 0.05 (two-sided)\nCalculation: n = 64 per group (total 128)\nAdjustments: 20% dropout rate → 160 patients; 2:1 randomization → 107 Drug X, 53 Placebo\nFinal sample size: 160 patients (stratified by site to ensure adequate enrollment)'
                    },
                    {
                        'id': 'analysis-populations',
                        'text': 'Define analysis populations and statistical methods.',
                        'type': 'textarea',
                        'sample_answer': 'Analysis populations:\n- Intent-to-treat (ITT): All randomized patients (primary efficacy analysis)\n- Per-protocol (PP): Patients completing ≥80% treatment with no major protocol violations\n- Safety: All patients receiving ≥1 dose\n\nStatistical methods:\n- Primary: ANCOVA adjusting for baseline 6MWD, NYHA class, site\n- Secondary: Mixed-effects models for repeated measures, Fisher\'s exact test for categorical outcomes\n- Missing data: Multiple imputation for efficacy, no imputation for safety\n- Interim analysis: One planned at 50% enrollment for futility'
                    }
                ]
            },
            {
                'id': 'regulatory-ethics',
                'title': 'Regulatory and Ethical Considerations',
                'description': 'IRB approval, informed consent, and regulatory compliance',
                'questions': [
                    {
                        'id': 'regulatory-status',
                        'text': 'Describe FDA IND status and regulatory pathway.',
                        'type': 'textarea',
                        'sample_answer': 'FDA IND Status: IND #12345 approved (effective date: MM/DD/YYYY). Fast Track designation requested based on unmet medical need. Regulatory pathway: 505(b)(1) NDA submission planned. ICH-GCP compliance ensured. Regular FDA communications planned including End-of-Phase II meeting. Chemistry, Manufacturing, and Controls (CMC) package supports Phase II dosing and duration.'
                    },
                    {
                        'id': 'ethics-consent',
                        'text': 'Detail IRB approval process and informed consent procedures.',
                        'type': 'textarea',
                        'sample_answer': 'IRB/Ethics: Central IRB approval required before site activation. Local IRB approval for sites requiring it. Annual continuing reviews and safety reporting per IRB requirements.\n\nInformed Consent: Written informed consent required before any study procedures. Consent form includes: study purpose, procedures, risks/benefits, alternatives, confidentiality, voluntary participation, contact information. Special populations consent considerations for patients with limited decision-making capacity. Re-consent for protocol amendments affecting risk/benefit.'
                    },
                    {
                        'id': 'risk-benefit',
                        'text': 'Provide risk-benefit analysis and patient safety measures.',
                        'type': 'textarea',
                        'sample_answer': 'Risk-Benefit Analysis:\nRisks: Potential drug-related AEs (GI upset, headache based on Phase I), unknown long-term effects, study procedures (blood draws, time commitment)\nBenefits: Potential improvement in functional capacity, quality of life; contribution to medical knowledge; close medical monitoring\nRisk minimization: Experienced investigators, careful inclusion/exclusion criteria, frequent monitoring, DSMB oversight, emergency procedures, clear stopping rules. Benefits justify risks given limited treatment options for advanced heart failure.'
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
                'id': 'research-background',
                'title': 'Research Background and Significance',
                'description': 'Scientific context and importance',
                'questions': [
                    {
                        'id': 'research-problem',
                        'text': 'Define the research problem and its significance.',
                        'type': 'textarea',
                        'sample_answer': 'Antibiotic resistance represents a critical global health threat, with carbapenem-resistant Enterobacteriaceae (CRE) causing >9,000 deaths annually in the US. Current resistance mechanisms are incompletely understood, particularly the role of efflux pumps in multidrug resistance. This research investigates novel efflux pump inhibitors that could restore antibiotic efficacy, addressing the urgent need for new therapeutic strategies against resistant pathogens.'
                    },
                    {
                        'id': 'literature-context',
                        'text': 'Summarize relevant literature and identify knowledge gaps.',
                        'type': 'textarea',
                        'sample_answer': 'Recent studies identified AcrAB-TolC as the primary efflux system in E. coli (Smith et al., 2023), while genomic analyses revealed novel resistance genes in clinical isolates (Johnson & Lee, 2022). However, current efflux pump inhibitors show limited clinical efficacy and significant toxicity (Chen et al., 2023). Knowledge gaps include: (1) Structure-activity relationships of next-generation inhibitors, (2) Synergistic effects with existing antibiotics, (3) Resistance development mechanisms. This study addresses these gaps through systematic compound screening and mechanistic analysis.'
                    }
                ]
            },
            {
                'id': 'experimental-design',
                'title': 'Experimental Design and Methodology',
                'description': 'Detailed experimental approach and procedures',
                'questions': [
                    {
                        'id': 'experimental-approach',
                        'text': 'Describe your overall experimental strategy and specific aims.',
                        'type': 'textarea',
                        'sample_answer': 'Experimental Strategy: Three-phase approach combining chemical synthesis, microbiological testing, and mechanistic studies.\n\nSpecific Aims:\n1. Synthesize and characterize 50 novel efflux pump inhibitor compounds based on quinoline scaffolds\n2. Evaluate antimicrobial activity using standardized susceptibility testing against MDR bacterial strains\n3. Investigate inhibition mechanisms using fluorescence-based efflux assays and protein-ligand binding studies\n4. Assess compound toxicity using mammalian cell culture models\n5. Determine lead compounds for further development based on efficacy and safety profiles'
                    },
                    {
                        'id': 'materials-methods',
                        'text': 'Detail materials, equipment, and experimental protocols.',
                        'type': 'textarea',
                        'sample_answer': 'Materials: Clinical bacterial isolates (E. coli, K. pneumoniae, P. aeruginosa) from hospital partners; chemical synthesis reagents (Sigma-Aldrich); mammalian cell lines (HEK293, HepG2).\n\nEquipment: HPLC-MS for compound characterization, microplate readers for growth assays, fluorescence microscopy for efflux studies, NMR spectroscopy for structure confirmation.\n\nProtocols: Compound synthesis using established quinoline chemistry; MIC determination per CLSI guidelines; efflux assays using ethidium bromide accumulation; cytotoxicity via MTT assays; protein expression and purification using E. coli systems; binding affinity determination by surface plasmon resonance.'
                    },
                    {
                        'id': 'experimental-controls',
                        'text': 'Specify experimental controls and validation approaches.',
                        'type': 'textarea',
                        'sample_answer': 'Positive controls: Known efflux pump inhibitors (PA βN, CCCP); reference antibiotics (ciprofloxacin, meropenem)\nNegative controls: DMSO vehicle, inactive compound analogs, efflux pump knockout strains\nValidation approaches: Compound purity >95% by HPLC-MS; bacterial strain authentication by 16S sequencing; efflux pump expression confirmation by qRT-PCR; reproducibility testing with n≥3 independent experiments; inter-laboratory validation with collaborating sites'
                    }
                ]
            },
            {
                'id': 'data-analysis',
                'title': 'Data Collection and Analysis',
                'description': 'Data management and statistical analysis methods',
                'questions': [
                    {
                        'id': 'data-collection',
                        'text': 'Describe data collection procedures and quality control measures.',
                        'type': 'textarea',
                        'sample_answer': 'Data Collection: Electronic laboratory notebooks (ELN) for real-time documentation; automated data capture from plate readers and analytical instruments; standardized data forms for each experimental procedure; regular backup to secure servers.\n\nQuality Control: Duplicate measurements for all critical assays; positive/negative controls in each experimental run; instrument calibration before each use; personnel training and competency assessment; regular equipment maintenance and validation; chain-of-custody documentation for samples.'
                    },
                    {
                        'id': 'statistical-analysis',
                        'text': 'Outline statistical methods and analysis plan.',
                        'type': 'textarea',
                        'sample_answer': 'Statistical Methods: Descriptive statistics for compound characterization; ANOVA for comparing treatment groups; IC50 calculations using nonlinear regression; correlation analysis for structure-activity relationships; survival analysis for time-kill studies.\n\nAnalysis Plan: Primary endpoint - fold-change in MIC with inhibitor vs without; Secondary endpoints - efflux pump activity reduction, cytotoxicity indices; Sample size: n≥6 per group based on power analysis (80% power, α=0.05); Multiple comparison corrections using Bonferroni method; Statistical software: R/GraphPad Prism.'
                    },
                    {
                        'id': 'data-management',
                        'text': 'Detail data management, storage, and sharing plans.',
                        'type': 'textarea',
                        'sample_answer': 'Data Management: REDCap database for structured data entry; version control for all analysis scripts; automated data validation rules; regular database backups; access controls and audit trails.\n\nStorage: Secure institutional servers with daily backups; retention period: 7 years post-publication; compliance with institutional data governance policies; de-identification procedures for shared data.\n\nSharing: Data sharing plan per NIH requirements; public repository deposition (ChEMBL for compound data); collaboration agreements for shared datasets; open access publication with supplementary data files.'
                    }
                ]
            },
            {
                'id': 'laboratory-safety',
                'title': 'Laboratory Safety and Compliance',
                'description': 'Safety protocols and regulatory compliance',
                'questions': [
                    {
                        'id': 'safety-protocols',
                        'text': 'Describe laboratory safety measures and risk mitigation.',
                        'type': 'textarea',
                        'sample_answer': 'Biosafety Level: BSL-2 containment for MDR bacterial work; trained personnel with annual safety updates; biological safety cabinet use for all bacterial manipulations; appropriate PPE (lab coats, gloves, safety glasses); waste decontamination by autoclaving.\n\nChemical Safety: Fume hood use for organic synthesis; chemical inventory management; SDS availability; emergency procedures; spill response kits; proper disposal of hazardous waste.\n\nRisk Mitigation: Institutional Biosafety Committee approval; regular safety inspections; incident reporting system; emergency contact procedures; first aid training for all personnel.'
                    },
                    {
                        'id': 'regulatory-compliance',
                        'text': 'Address regulatory requirements and institutional approvals.',
                        'type': 'textarea',
                        'sample_answer': 'Institutional Approvals: IRB approval (if human samples involved); Institutional Biosafety Committee (IBC) approval for recombinant DNA work; Animal Care and Use Committee (IACUC) approval if animal studies included.\n\nRegulatory Compliance: FDA regulations for potential therapeutic compounds; DEA registration for controlled substances; EPA regulations for waste disposal; state and local laboratory regulations.\n\nDocumentation: Standard Operating Procedures (SOPs) for all methods; training records; safety inspection reports; waste disposal manifests; equipment maintenance logs.'
                    }
                ]
            },
            {
                'id': 'timeline-deliverables',
                'title': 'Project Timeline and Expected Deliverables',
                'description': 'Project schedule and anticipated outcomes',
                'questions': [
                    {
                        'id': 'project-timeline',
                        'text': 'Provide detailed project timeline with milestones.',
                        'type': 'textarea',
                        'sample_answer': 'Year 1: Months 1-3: Literature review, method optimization, initial compound synthesis\nMonths 4-9: Compound library expansion (target: 30 compounds), preliminary screening\nMonths 10-12: Initial hit identification, structure-activity analysis\n\nYear 2: Months 13-18: Lead optimization, mechanism of action studies\nMonths 19-21: Toxicity evaluation, selectivity testing\nMonths 22-24: Data analysis, manuscript preparation\n\nMilestones: M3 (Methods established), M12 (Hit compounds identified), M18 (Lead compounds optimized), M21 (Safety profile complete), M24 (Manuscripts submitted)'
                    },
                    {
                        'id': 'expected-deliverables',
                        'text': 'List specific deliverables and expected outcomes.',
                        'type': 'textarea',
                        'sample_answer': 'Primary Deliverables:\n1. Chemical library of 50 novel efflux pump inhibitor compounds with full characterization data\n2. Comprehensive antimicrobial activity database against 20+ MDR bacterial strains\n3. Mechanism of action profiles for top 10 lead compounds\n4. Structure-activity relationship analysis and predictive models\n5. Toxicity and selectivity profiles for lead compounds\n\nPublications: 2-3 peer-reviewed articles in high-impact journals (target: Nature Microbiology, ACS Infectious Diseases)\nIntellectual Property: 1-2 patent applications for lead compounds\nPersonnel Training: 2 PhD students, 1 postdoc trained in antimicrobial research\nData Sharing: Public chemical database entries, protocols shared via protocols.io'
                    },
                    {
                        'id': 'budget-justification',
                        'text': 'Provide budget breakdown and justification.',
                        'type': 'textarea',
                        'sample_answer': 'Total Budget: $380,000 over 24 months\n\nPersonnel (65% - $247,000):\n- Principal Investigator (15% effort): $45,000\n- Postdoctoral Fellow (100% effort): $120,000\n- Graduate Student (100% effort): $82,000\n\nSupplies (25% - $95,000):\n- Chemical synthesis reagents: $40,000\n- Bacterial culture media and supplies: $15,000\n- Cell culture reagents: $20,000\n- Analytical consumables: $20,000\n\nEquipment (8% - $30,400):\n- Microplate reader upgrade: $15,000\n- Synthesis equipment: $15,400\n\nOther (2% - $7,600):\n- Publication fees: $4,000\n- Conference travel: $3,600'
                    }
                ]
            },
            {
                'id': 'collaboration-dissemination',
                'title': 'Collaborations and Dissemination Plan',
                'description': 'Partnership strategy and knowledge sharing',
                'questions': [
                    {
                        'id': 'collaborations',
                        'text': 'Describe key collaborations and their contributions.',
                        'type': 'textarea',
                        'sample_answer': 'Key Collaborations:\n1. Dr. Sarah Johnson (University Medical Center) - Clinical isolate collection and resistance profiling expertise\n2. Prof. Michael Chen (State University Chemistry Dept) - Advanced organic synthesis and compound optimization\n3. Dr. Lisa Rodriguez (Pharma Corp) - Industrial perspective on drug development and scale-up\n4. International Antimicrobial Resistance Consortium - Cross-validation of results and global strain collection access\n\nCollaboration Benefits: Enhanced expertise, resource sharing, validation of results, accelerated translation, global impact assessment'
                    },
                    {
                        'id': 'dissemination-plan',
                        'text': 'Outline your strategy for sharing results and impact.',
                        'type': 'textarea',
                        'sample_answer': 'Dissemination Strategy:\nAcademic: Peer-reviewed publications in high-impact journals; presentations at ASM Microbe, ICAAC conferences; invited seminars at partner institutions\n\nPublic Engagement: Press releases for significant findings; social media updates; university news articles; public health blog posts\n\nIndustry: Industry partnership meetings; technology transfer office engagement; patent disclosures; pharmaceutical company presentations\n\nPolicy: CDC/FDA briefings if clinically relevant; WHO consultation participation; antimicrobial stewardship program integration\n\nEducation: Graduate course integration; undergraduate research opportunities; high school outreach programs'
                    }
                ]
            }
        ]
    }
]