"""
Favor Analysis Engine.
Determines if a clause is market-standard, or leans heavily towards one party.
"""
from typing import Literal
from loguru import logger
from ..parsers.extractor import ExtractedClause

FavorScore = Literal[
    "strongly_favors_counterparty",
    "favors_counterparty",
    "balanced",
    "favors_you",
    "strongly_favors_you"
]

class FavorAnalyzer:

    MARKET_STANDARDS = {
        "limitation_of_liability": {
            "saas_agreement": {
                "standard": "Cap at 12 months of fees paid",
                "pro_vendor": "Cap at 3 months or lower",
                "pro_customer": "Uncapped or cap above annual contract value",
                "common_in_india": "Cap at 3-6 months (vendor-heavy market)"
            }
        },
        "subscription_auto_renewal": {
            "saas_agreement": {
                "standard": "30-day notice to cancel before renewal",
                "pro_vendor": "60-90 day notice required (easy to miss)",
                "pro_customer": "Auto-renewal requires affirmative consent",
            }
        },
        "payment_terms": {
            "freelance_service": {
                "standard": "Net 30 days",
                "pro_vendor": "Net 15 days or upon receipt",
                "pro_customer": "Net 60 or Net 90 days"
            }
        }
        # ... expands for all major clause types
    }

    def score_clause_favor(
        self,
        clause: ExtractedClause,
        contract_type: str,
        market_standard: str  # Context passed from LLM regarding the specific clause terms
    ) -> FavorScore:
        """
        Maps a 0-10 numerical alignment to a strict categorical favorability score.
        0 = entirely favors counterparty
        5 = balanced / market standard
        10 = entirely favors user
        """
        logger.debug(f"Analyzing favorability for {clause.clause_type} in {contract_type}")
        
        # MOCK LOGIC: In production, the LLM maps the `verbatim_text` against `MARKET_STANDARDS`
        # to produce an integer between 0 and 10.
        
        simulated_llm_score = 2 # e.g. "Net 90 days" strongly favors the customer/counterparty
        
        if simulated_llm_score <= 2:
            return "strongly_favors_counterparty"
        elif simulated_llm_score <= 4:
            return "favors_counterparty"
        elif simulated_llm_score <= 6:
            return "balanced"
        elif simulated_llm_score <= 8:
            return "favors_you"
        else:
            return "strongly_favors_you"
