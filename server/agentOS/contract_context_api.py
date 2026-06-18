"""
ForgeSign AgentOS Mesh Integration.
Handles cross-agent context sharing, specifically memory updates, GhostCFO calendar hooks,
and NexusOps proactive analysis routes.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime
from loguru import logger

router = APIRouter(prefix="/v1/agentOS/contracts", tags=["AgentOS Mesh - Contracts"])

# --- Shared Memory Schema ---
class AutoRenewalAlert(BaseModel):
    contract_name: str
    cancel_by_date: str
    days_remaining: int

class SharedContractMemory(BaseModel):
    updated_at: str
    active_contracts: int
    contracts_pending_review: int
    contracts_pending_signature: int
    auto_renewal_alerts: List[AutoRenewalAlert]
    total_financial_exposure: float
    uncapped_liability_contracts: int
    high_risk_unsigned_contracts: int
    last_review_at: str

# --- API Payloads ---
class AnalyzeContractRequest(BaseModel):
    user_id: str
    contract_text_or_url: str
    contract_type: Optional[str] = None
    reviewing_party: Optional[str] = None

class DisputePackageRequest(BaseModel):
    user_id: str
    contract_id: str
    dispute_description: str

class DisputePackageResponse(BaseModel):
    status: str
    routed_to: str
    evidence_payload: Any


# --- Endpoints ---

@router.post("/analyze")
async def analyze_contract(request: AnalyzeContractRequest):
    """
    Triggers the full contract analysis pipeline.
    Used by: NexusOps (Day 29) to auto-analyze contracts found in email/calendar.
    """
    logger.info(f"[MESH] NexusOps triggered analysis for User: {request.user_id}")
    
    # MOCK: Trigger internal pipeline
    
    # MOCK GHOSTCFO ESCALATION LOGIC (injected during pipeline)
    # if clause.clause_type == "subscription_auto_renewal":
    #     await ghostcfo_client.add_financial_calendar_event(
    #         user_id=request.user_id,
    #         event_type="contract_renewal_deadline",
    #         event_date=renewal_deadline,
    #         description=f"Cancel {contract.counterparty_name} contract by this date",
    #         financial_impact=annual_contract_value
    #     )
    
    return {
        "contract_id": "cont_mock_123",
        "analysis_summary": "Heavily vendor-favorable MSA with critical liability gaps.",
        "critical_clause_count": 2
    }

@router.get("/context/{user_id}", response_model=SharedContractMemory)
async def get_contract_context(user_id: str):
    """
    Returns the shared memory object.
    Used by: GhostCFO (financial exposure tracking) & NexusOps (pre-signing review).
    """
    logger.info(f"[MESH] Context requested for User: {user_id}")
    # MOCK: Retrieve from Redis/Postgres "agentOS:memory:contracts:{user_id}"
    return SharedContractMemory(
        updated_at=datetime.now().isoformat(),
        active_contracts=3,
        contracts_pending_review=1,
        contracts_pending_signature=2,
        auto_renewal_alerts=[
            AutoRenewalAlert(
                contract_name="Salesforce MSA",
                cancel_by_date="2025-12-15",
                days_remaining=67
            )
        ],
        total_financial_exposure=4500000.0,
        uncapped_liability_contracts=1,
        high_risk_unsigned_contracts=1,
        last_review_at="2025-06-09T14:30:00+05:30"
    )

@router.get("/auto_renewals/{user_id}")
async def get_auto_renewals(user_id: str):
    """
    Returns contracts with upcoming auto-renewal deadlines.
    Used by: GhostCFO (calendar integration) & NexusOps (proactive reminder workflow).
    """
    logger.info(f"[MESH] Pulling auto-renewals for User: {user_id}")
    return {
        "user_id": user_id,
        "upcoming_renewals": [
            {
                "contract_name": "Salesforce MSA",
                "cancel_by_date": "2025-12-15",
                "days_remaining": 67
            }
        ]
    }

@router.post("/dispute_package", response_model=DisputePackageResponse)
async def package_dispute(request: DisputePackageRequest):
    """
    Compiles relevant contract clauses + timeline + evidence.
    Routes to RiteOfWay (Day 06) for legal demand generation.
    """
    logger.info(f"[MESH ESCALATION] Compiling dispute package for {request.contract_id}")
    
    # MOCK: Assemble the dispute payload from the extracted clauses
    evidence_payload = {
        "contract_id": request.contract_id,
        "violated_clause_text": "Vendor agrees to maintain 99.9% SLA...",
        "user_dispute_context": request.dispute_description,
        "legal_disclaimer": "This analysis is for informational purposes only and does not constitute legal advice."
    }
    
    # MOCK POST to RiteOfWay's /v1/riteofway/demand/generate endpoint
    logger.success(f"[MESH ESCALATION] Routed to RiteOfWay.")
    
    return DisputePackageResponse(
        status="success",
        routed_to="RiteOfWay",
        evidence_payload=evidence_payload
    )
