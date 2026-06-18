"""
Risk Scoring Engine.
Computes a weighted risk score across 5 dimensions for every clause.
"""
from typing import Dict
from loguru import logger
import re
from ..parsers.extractor import ExtractedClause

class ClauseRiskScore:
    def __init__(self, total_score: int, breakdown: Dict[str, int], critical_flags: list[str]):
        self.total_score = total_score
        self.breakdown = breakdown
        self.critical_flags = critical_flags

class RiskScorer:

    RISK_DIMENSIONS = {
        "financial_exposure": {
            "weight": 0.30,
            "description": "Maximum financial impact if clause invoked",
            "scoring": {
                10: "Unlimited liability or catastrophic exposure",
                7: "Significant liability above contract value",
                4: "Moderate financial exposure",
                1: "Minimal or zero financial exposure"
            }
        },
        "operational_restriction": {
            "weight": 0.20,
            "description": "How much does this restrict business operations?",
            "scoring": {
                10: "Severely restricts core business activities",
                7: "Materially limits how business operates",
                4: "Some operational constraints",
                1: "Minor or no operational restrictions"
            }
        },
        "exit_difficulty": {
            "weight": 0.20,
            "description": "How hard is it to get out of this commitment?",
            "scoring": {
                10: "Locked in with no exit or extremely costly exit",
                7: "Exit possible but expensive/complex",
                4: "Exit possible with reasonable notice",
                1: "Easy exit with minimal consequences"
            }
        },
        "ip_risk": {
            "weight": 0.15,
            "description": "Does this affect intellectual property rights?",
            "scoring": {
                10: "Transfers all IP to counterparty",
                7: "Broad license to counterparty",
                4: "Limited IP implications",
                1: "No IP implications"
            }
        },
        "enforcement_probability": {
            "weight": 0.15,
            "description": "How likely is this clause to be enforced?",
            "scoring": {
                10: "Clearly enforceable, commonly enforced",
                7: "Likely enforceable",
                4: "Might be enforceable depending on circumstances",
                1: "Unlikely to be enforceable as written"
            }
        }
    }
    
    ALWAYS_FLAG_PATTERNS = [
        {
            "pattern": r"unlimited liability",
            "risk_level": 10,
            "reason": "No cap on financial exposure — catastrophic risk"
        },
        {
            "pattern": r"assign.*without.*consent",
            "risk_level": 8,
            "reason": "Counterparty can transfer your contract to anyone"
        },
        {
            "pattern": r"work.*for.*hire",
            "risk_level": 9,
            "reason": "All IP you create belongs to counterparty by default"
        },
        {
            "pattern": r"non-compete.*worldwide",
            "risk_level": 9,
            "reason": "Global non-compete is usually unenforceable but creates risk"
        },
        {
            "pattern": r"sole.*discretion",
            "risk_level": 7,
            "reason": "Counterparty can make arbitrary decisions with no appeal"
        },
        {
            "pattern": r"perpetual.*irrevocable.*license",
            "risk_level": 8,
            "reason": "You grant rights that can never be revoked"
        },
        {
            "pattern": r"automatic.*renewal.*without.*notice",
            "risk_level": 8,
            "reason": "Contract renews silently — easy to be locked in"
        }
    ]

    def compute_risk_score(
        self,
        clause: ExtractedClause,
        dimension_scores: Dict[str, int]
    ) -> ClauseRiskScore:
        """
        Weighted average of all dimensions + regex override for critical patterns.
        Risk score: 1-10 (10 = highest risk to reviewing party)
        """
        critical_flags = []
        base_score = 0.0
        
        # Calculate weighted base score
        for dim, config in self.RISK_DIMENSIONS.items():
            weight = config["weight"]
            score = dimension_scores.get(dim, 1)
            base_score += (score * weight)
            
        final_score = int(round(base_score))
        
        # Apply regex override
        text_lower = clause.verbatim_text.lower()
        for flag in self.ALWAYS_FLAG_PATTERNS:
            if re.search(flag["pattern"], text_lower):
                critical_flags.append(flag["reason"])
                if flag["risk_level"] > final_score:
                    final_score = flag["risk_level"]
                    
        return ClauseRiskScore(total_score=final_score, breakdown=dimension_scores, critical_flags=critical_flags)
