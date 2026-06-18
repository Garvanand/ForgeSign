"""
ForgeSign Primary Endpoints.
"""
from fastapi import APIRouter, File, UploadFile, BackgroundTasks
from ..core.schemas import ContractBrief, ContractUploadResponse
from ..ingestion.parser import ContractParser
from ..intelligence.analysis import ContractIntelligenceEngine
from ..redline.generator import RedlineGenerator
import os

api_router = APIRouter(prefix="/v1/forgesign", tags=["Contract Intelligence"])

parser = ContractParser()
analyzer = ContractIntelligenceEngine()
redliner = RedlineGenerator()

MANDATORY_DISCLAIMER = "This analysis is for informational purposes only and does not constitute legal advice. For legally binding matters, consult a qualified advocate."

@api_router.post("/upload", response_model=ContractUploadResponse)
async def upload_contract(file: UploadFile = File(...)):
    """
    Ingests a PDF/DOCX file and initiates the parsing pipeline.
    """
    file_bytes = await file.read()
    doc_id = parser.generate_document_id(file_bytes)
    
    # In production, this saves to object storage (MinIO) and triggers background processing
    return ContractUploadResponse(
        document_id=doc_id,
        status="processing",
        message="Contract ingested successfully. Polling analysis..."
    )

@api_router.get("/analysis/{document_id}", response_model=ContractBrief)
async def get_contract_analysis(document_id: str):
    """
    Returns the deeply analyzed contract brief.
    Appends the mandatory legal disclaimer.
    """
    # MOCK: In production, fetch parsed text from DB
    mock_text = "MOCK_CONTRACT_TEXT"
    
    brief = await analyzer.analyze_full_contract(mock_text)
    
    # Mandatory Constraint Check
    if MANDATORY_DISCLAIMER not in brief.exit_conditions: # Just appending somewhere visible
        brief.exit_conditions += f"\n\nDISCLAIMER: {MANDATORY_DISCLAIMER}"
        
    return brief

@api_router.post("/generate_redline/{document_id}")
async def generate_redline(document_id: str):
    """
    Takes the analyzed contract and returns a URL to download the .docx
    file with native MS Word Track Changes applied.
    """
    mock_text = "MOCK_CONTRACT_TEXT"
    brief = await analyzer.analyze_full_contract(mock_text)
    
    output_path = f"/tmp/redlines/{document_id}_redline.docx"
    os.makedirs("/tmp/redlines/", exist_ok=True)
    
    final_path = redliner.generate_redline_docx(mock_text, brief, output_path)
    
    return {"status": "success", "download_url": f"/v1/forgesign/download/{document_id}"}
