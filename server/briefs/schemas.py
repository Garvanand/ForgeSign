"""
Contract Brief Schemas.
Translates a 50-page legal document into a strict 1-page business summary.
"""
from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime, date
from decimal import Decimal

class ContractParties(BaseModel):
    reviewing_party: str
    counterparty: str

class Obligation(BaseModel):
    description: str

class Right(BaseModel):
    description: str

class Risk(BaseModel):
    description: str
    potential_consequence: str

class ExitAnalysis(BaseModel):
    notice_period: str
    early_exit_penalties: str
    termination_triggers: List[str]

class PenaltyClause(BaseModel):
    trigger: str
    amount_or_description: str

class FinancialExposure(BaseModel):
    contract_value: Optional[Decimal]      # what you're paying
    liability_cap: Optional[str]           # max you can be sued for
    uncapped_liability_items: List[str]    # items excluded from cap
    penalty_clauses: List[PenaltyClause]   # specific penalties
    total_worst_case_exposure: str         # human-readable worst case

class ContractBrief(BaseModel):
    brief_id: str
    contract_id: str
    generated_at: datetime

    # Header context
    contract_type: str
    parties: ContractParties
    effective_date: Optional[date]
    term: str                       # "12 months, auto-renews annually"
    governing_law: str

    # The 5 key sections
    key_obligations: List[Obligation]     # what YOU must do
    key_rights: List[Right]               # what YOU get
    key_risks: List[Risk]                 # what could hurt you
    exit_conditions: ExitAnalysis         # how to get out
    financial_exposure: FinancialExposure # total money at risk

    # Summary verdict
    overall_risk_rating: Literal["low", "medium", "high", "critical"]
    one_sentence_verdict: str      # "This is a heavily vendor-favorable agreement..."
    recommended_action: str        # "Review redlines before proceeding"

    # Auto-renewal alert (special case)
    has_auto_renewal: bool
    auto_renewal_deadline: Optional[date]  # when notice must be given
