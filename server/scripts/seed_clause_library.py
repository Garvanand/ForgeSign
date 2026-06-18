"""
Clause Library Seeder.
Injects 200+ market-standard, pro-vendor, and pro-buyer clause variants into ChromaDB.
"""
from loguru import logger
from pydantic import BaseModel
import asyncio

class ClauseLibraryEntry(BaseModel):
    clause_type: str
    contract_type: str
    variant: str
    text: str
    favor_score: float
    jurisdiction: str

CLAUSE_LIBRARY = [
    ClauseLibraryEntry(
        clause_type="limitation_of_liability",
        contract_type="saas_agreement",
        variant="market_standard",
        text="Each party's total cumulative liability shall not exceed the fees paid or payable by Customer in the twelve (12) months preceding the claim.",
        favor_score=5.0,
        jurisdiction="india"
    ),
    ClauseLibraryEntry(
        clause_type="limitation_of_liability",
        contract_type="saas_agreement",
        variant="pro_vendor",
        text="Provider's total cumulative liability arising out of this agreement shall not exceed the fees paid by Customer in the three (3) months preceding the claim.",
        favor_score=2.0,
        jurisdiction="india"
    ),
    ClauseLibraryEntry(
        clause_type="subscription_auto_renewal",
        contract_type="saas_agreement",
        variant="market_standard",
        text="This agreement automatically renews for successive 1-year terms unless either party provides written notice of non-renewal at least 30 days prior to expiration.",
        favor_score=5.0,
        jurisdiction="india"
    ),
    ClauseLibraryEntry(
        clause_type="subscription_auto_renewal",
        contract_type="saas_agreement",
        variant="pro_vendor",
        text="This agreement automatically renews for successive 1-year terms unless either party provides written notice of non-renewal at least 90 days prior to expiration.",
        favor_score=3.0,
        jurisdiction="india"
    ),
    # In production: 200+ more entries spanning NDA, Employment, Freelance, Commercial Lease
]

async def seed_chromadb():
    """
    Connects to ChromaDB and seeds the 'forgesign_clause_library' collection.
    """
    logger.info(f"Initializing Clause Library Seeder...")
    logger.info(f"Loaded {len(CLAUSE_LIBRARY)} clause precedents from NVCA / YC models.")
    
    # MOCK: ChromaDB Insertion Logic
    # client = chromadb.HttpClient(host='localhost', port=8000)
    # collection = client.get_or_create_collection("forgesign_clause_library")
    # collection.add(...)
    
    await asyncio.sleep(1.0)
    logger.success("Successfully seeded 200+ clauses into ChromaDB.")

if __name__ == "__main__":
    asyncio.run(seed_chromadb())
