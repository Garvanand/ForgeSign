from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class PracticalImplication(BaseModel):
    scenario: str = Field(..., description="A real-world 1-sentence scenario where this clause matters")
    impact: str = Field(..., description="The financial or operational impact in that scenario")

class ClauseAnalysis(BaseModel):
    original_text: str = Field(..., description="The exact text of the clause")
    clause_category: str = Field(..., description="e.g., Liability, Auto-Renewal, IP Ownership")
    plain_english_summary: str = Field(..., description="1-2 sentences explaining what this means simply")
    
    risk_score: int = Field(..., ge=1, le=10, description="1=Balanced/Low Risk, 10=Bet the Company")
    favorability: Literal["strongly_favors_counterparty", "favors_counterparty", "balanced", "favors_you", "strongly_favors_you"]
    
    practical_implications: List[PracticalImplication] = Field(..., min_length=1, max_length=3)
    
    is_negotiable: bool = Field(..., description="Whether this is standard boilerplate or typically negotiable")
    redline_strategy: Optional[str] = Field(None, description="How to frame the pushback")
    proposed_redline_text: Optional[str] = Field(None, description="Exact alternative legal language to replace this clause")

class ContractBrief(BaseModel):
    contract_title: str
    parties: List[str]
    effective_date: Optional[str]
    term_length: Optional[str]
    
    key_obligations: List[str]
    key_rights: List[str]
    critical_risks: List[str]
    financial_exposure: str
    exit_conditions: str
    
    analyzed_clauses: List[ClauseAnalysis]

class ContractUploadResponse(BaseModel):
    document_id: str
    status: str
    message: str
