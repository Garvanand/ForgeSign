"""
Counterparty Intelligence Schemas.
Models the aggregated data moat and output negotiation strategy playbooks.
"""
from pydantic import BaseModel
from typing import List, Literal, Dict, Optional
from datetime import datetime

class ClauseStance(BaseModel):
    acceptance_rate: float            # 0.0 to 1.0 (how often they accept changes)
    typical_counter_offer: str
    is_non_negotiable: bool

class CounterpartyResearch(BaseModel):
    company_size: str
    industry: str
    likely_stance: str
    public_controversies: List[str]

class CounterpartyProfile(BaseModel):
    company_name: str
    company_name_normalized: str
    data_quality: Literal["known_high", "known_low", "inferred", "unknown"]
    negotiation_style: Literal["flexible", "moderate", "firm", "non-negotiable"]

    # Per-clause stance (from aggregated user reports)
    clause_stances: Dict[str, ClauseStance]

    # Recommendations
    recommended_approach: str
    clauses_worth_fighting: List[str]
    clauses_not_worth_fighting: List[str]
    known_dealbreakers: List[str]

    # Data provenance
    reports_count: int              # how many user reports
    last_updated: datetime
    confidence: float               # 0-1

class NegotiationStrategy(BaseModel):
    opening_position: str
    trading_strategy: str
    escalation_triggers: str
    walk_away_point: str
