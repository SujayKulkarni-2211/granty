import uuid

FINANCIAL_REPORT_TEMPLATES = [
    {
        'id': str(uuid.uuid4()),
        'name': 'Monthly Management Financial Report',
        'description': 'Standard report including income statement, balance sheet, cash flow and KPIs',
        'category': 'financial_report',
        'sections': [
            {
                'id': 'exec-summary',
                'title': 'Executive Summary',
                'description': 'Overview of monthly financial performance',
                'questions': [
                    {
                        'id': 'summary-text',
                        'text': 'Provide a snapshot of performance and key highlights.',
                        'type': 'textarea',
                        'sample_answer': (
                            "July 2025: Revenue ₹90 L (+10% MoM), gross profit ₹56 L, net margin 17%. Operating expenses controlled at ₹38 L. "
                            "Cash flow from operations ₹12 L. Key drivers: increased subscription sales, cost optimisations."
                        )
                    }
                ]
            },
            {
                'id': 'income-statement',
                'title': 'Income Statement',
                'description': 'Revenue, expenses, and profitability',
                'questions': [
                    {
                        'id': 'income-text',
                        'text': 'Summarize revenue streams, costs, and net income.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Revenue: ₹90 L (Product ₹65 L; Services ₹25 L). COGS ₹34 L → gross profit ₹56 L (62%). "
                            "OpEx ₹39 L; net profit ₹17 L (≈18.9% net margin)."
                        )
                    }
                ]
            },
            {
                'id': 'balance-sheet',
                'title': 'Balance Sheet',
                'description': 'Assets, liabilities, equity position',
                'questions': [
                    {
                        'id': 'balance-text',
                        'text': 'Detail financial position as of month end.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Assets ₹130 L (Current ₹50 L, Fixed ₹80 L). Liabilities ₹75 L (Current ₹35 L, Long-term ₹40 L). "
                            "Equity ₹55 L. Current ratio 1.43×, debt-to-equity ratio ≈1.36."
                        )
                    }
                ]
            },
            {
                'id': 'cash-flow',
                'title': 'Cash Flow Statement',
                'description': 'Operating, investing and financing cash flows',
                'questions': [
                    {
                        'id': 'cashflow-text',
                        'text': 'Describe cash flow movements.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Operating cash inflow ₹12 L. Capex ₹4 L for new hardware. Financing: ₹3 L equity injection. "
                            "Net cash increase ₹11 L."
                        )
                    }
                ]
            },
            {
                'id': 'forecast-proforma',
                'title': 'Financial Projection / Forecast',
                'description': 'Rolling 3‑year projections including sales forecast and break‑even analysis',
                'questions': [
                    {
                        'id': 'forecast-text',
                        'text': 'Provide high-level projections and assumptions.',
                        'type': 'textarea',
                        'sample_answer': (
                            "Projected revenue CAGR 20% over 3 years; break-even expected in 14 months. "
                            "Assumptions: sales growth 10% monthly first year, 5% thereafter; stable 60% gross margin; "
                            "capex year 1 ₹20 L then ₹5 L/year."
                        )
                    }
                ]
            }
        ]
    }
]
