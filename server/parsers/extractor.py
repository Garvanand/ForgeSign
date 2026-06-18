"""
Clause Extractor Engine.
Uses Long-Context LLMs to extract verbatim clauses according to the Taxonomy.
"""
from pydantic import BaseModel
from typing import List, Optional
from loguru import logger
import asyncio
from .taxonomy import ClauseTaxonomy

class ExtractedClause(BaseModel):
    clause_id: str
    clause_type: str            # from taxonomy
    section_reference: str      # "Section 12.3" or "Page 7, Para 2"
    verbatim_text: str          # exact text from contract
    word_count: int
    is_standard: bool           # is this typical boilerplate?
    is_unusual: bool            # deviates significantly from market standard?
    is_missing: bool = False    # expected clause that isn't present

class ContractClassification(BaseModel):
    contract_type: str
    parties: List[str]
    user_role: str
    governing_law: Optional[str]
    effective_date: Optional[str]
    term_length: Optional[str]
    is_template: bool
    counterparty_name: Optional[str]

class ClauseExtractor:

    async def extract_all_clauses(
        self,
        contract_text: str,
        contract_type: str
    ) -> List[ExtractedClause]:
        """
        Use Claude (full contract in context) to extract all clauses.
        One LLM call for full extraction (not one per clause — too slow).
        Return structured JSON with all clauses.
        """
        logger.info(f"Initiating Claude Opus long-context extraction for {contract_type}")
        await asyncio.sleep(2.0) # Simulate 200k token processing
        
        # Determine taxonomy targets
        targets = ClauseTaxonomy.UNIVERSAL_CLAUSES.copy()
        targets.extend(ClauseTaxonomy.CONTRACT_SPECIFIC.get(contract_type, []))
        
        logger.debug(f"Targeting {len(targets)} distinct clause types.")
        
        # MOCK RESPONSE
        return [
            ExtractedClause(
                clause_id="cl_1",
                clause_type="limitation_of_liability",
                section_reference="Section 3.1",
                verbatim_text="IN NO EVENT SHALL PROVIDER BE LIABLE...",
                word_count=45,
                is_standard=False,
                is_unusual=True,
                is_missing=False
            ),
            ExtractedClause(
                clause_id="cl_2",
                clause_type="indemnification",
                section_reference="Section 4",
                verbatim_text="Client agrees to indemnify...",
                word_count=12,
                is_standard=False,
                is_unusual=True,
                is_missing=False
            )
        ]

    async def classify_contract(
        self,
        contract_text: str
    ) -> ContractClassification:
        """
        Determine contract metadata.
        Use first 3000 tokens only (header + recitals contain this info)
        Use Groq for speed (classification is simpler than analysis)
        """
        logger.info("Classifying contract via Groq (fast-path)")
        await asyncio.sleep(0.5) # Simulate fast LLM
        
        # MOCK RESPONSE
        return ContractClassification(
            contract_type="saas_agreement",
            parties=["Acme Corp", "Beta LLC"],
            user_role="Client",
            governing_law="Delaware",
            effective_date="2025-01-01",
            term_length="1 Year",
            is_template=True,
            counterparty_name="Acme Corp"
        )
