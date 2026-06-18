"""
Long-Context Contract Intelligence Pipeline.
Analyzes full parsed contracts in a single LLM pass to preserve cross-references.
"""
import asyncio
from loguru import logger
from ..core.schemas import ContractBrief, ClauseAnalysis, PracticalImplication
import json

class ContractIntelligenceEngine:
    
    async def analyze_full_contract(self, raw_markdown: str, user_role: str = "Client") -> ContractBrief:
        """
        Takes the full markdown of a contract.
        In production, this is sent to Claude 3.5 Sonnet / Opus (200k context) 
        using forced Pydantic structured output mapping to `ContractBrief`.
        """
        logger.info("Initializing 200K Long-Context Analysis...")
        await asyncio.sleep(2.0) # Simulate API latency (normally ~15-30s for a full contract)
        
        logger.info("Extracting clauses, scoring risk, and generating practical implications...")
        
        # MOCK Implementation of the Claude JSON output
        mock_brief = ContractBrief(
            contract_title="Master Service Agreement",
            parties=["UserCompany (Client)", "CounterParty LLC (Provider)"],
            effective_date="Upon Signature",
            term_length="1 Year (Auto-Renewing)",
            key_obligations=[
                "Pay invoices within 60 days",
                "Indemnify provider against all claims"
            ],
            key_rights=[
                "Receive services as outlined in Exhibit A"
            ],
            critical_risks=[
                "Unlimited liability for user, capped liability for provider",
                "Automatic assignment of all IP to provider",
                "Automatic 1-year renewal trap"
            ],
            financial_exposure="Uncapped indemnification. Provider liability capped at 1 month fees.",
            exit_conditions="Requires 90 days written notice before term expiration.",
            analyzed_clauses=[
                ClauseAnalysis(
                    original_text="IN NO EVENT SHALL PROVIDER BE LIABLE FOR ANY INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES. PROVIDER'S TOTAL LIABILITY SHALL NOT EXCEED THE AMOUNT PAID BY CLIENT IN THE PRECEDING ONE (1) MONTH.",
                    clause_category="Limitation of Liability",
                    plain_english_summary="If something goes wrong and costs you money, the Provider will only pay you back up to 1 month of fees. They will not cover lost profits.",
                    risk_score=9,
                    favorability="strongly_favors_counterparty",
                    practical_implications=[
                        PracticalImplication(
                            scenario="A bug in their software brings down your site for 3 days.",
                            impact="You lose $50,000 in sales, but can only sue them for the $1,000 monthly fee you paid them."
                        ),
                        PracticalImplication(
                            scenario="They accidentally delete your customer database.",
                            impact="You face regulatory fines and rebuild costs, but they cap their liability at 1 month's fee."
                        )
                    ],
                    is_negotiable=True,
                    redline_strategy="Push for a cap equal to 12 months of fees, and mutual carve-outs for gross negligence.",
                    proposed_redline_text="Neither party shall be liable for indirect damages. Each party's total aggregate liability shall not exceed the total amounts paid or payable under this Agreement in the twelve (12) months preceding the claim."
                ),
                ClauseAnalysis(
                    original_text="Any intellectual property created during the term of this agreement shall become the exclusive property of the Provider, regardless of prior ownership.",
                    clause_category="Intellectual Property",
                    plain_english_summary="They own everything you create, even if you owned it before signing this contract.",
                    risk_score=10,
                    favorability="strongly_favors_counterparty",
                    practical_implications=[
                        PracticalImplication(
                            scenario="You integrate your proprietary codebase into their system.",
                            impact="They legally own your core proprietary codebase and can sell it to your competitors."
                        )
                    ],
                    is_negotiable=True,
                    redline_strategy="Reject outright. IP must remain with the creator, only granting a license to use.",
                    proposed_redline_text="Client retains all rights, title, and interest in and to its pre-existing intellectual property. Provider is granted a limited, non-exclusive license to use Client IP solely to perform the Services."
                )
            ]
        )
        
        logger.success(f"Analysis complete. Extracted {len(mock_brief.analyzed_clauses)} critical clauses.")
        return mock_brief
