"""
Contract Ingestion Pipeline.
Extracts clean markdown text from PDFs/DOCX using LlamaParse (mocked).
"""
import asyncio
from loguru import logger
import hashlib
import os

class ContractParser:
    
    async def parse_document(self, file_bytes: bytes, filename: str) -> str:
        """
        Parses a document (PDF/DOCX) into clean markdown text suitable for LLM context.
        Uses a mock LlamaParse implementation.
        """
        logger.info(f"Initiating parsing pipeline for {filename} ({len(file_bytes)} bytes)")
        
        # Simulate processing time (PyMuPDF/LlamaParse OCR)
        await asyncio.sleep(2.0)
        
        # Mock extracted markdown
        extracted_text = f"""
# {filename.upper()}
This Agreement is entered into on this day between UserCompany ("Client") and CounterParty LLC ("Provider").

## 1. Services
Provider agrees to deliver services as outlined in Exhibit A.

## 2. Payment Terms
Client shall pay Provider within sixty (60) days of receipt of invoice. Late payments incur a 5% monthly fee.

## 3. Limitation of Liability
IN NO EVENT SHALL PROVIDER BE LIABLE FOR ANY INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES. PROVIDER'S TOTAL LIABILITY SHALL NOT EXCEED THE AMOUNT PAID BY CLIENT IN THE PRECEDING ONE (1) MONTH.

## 4. Indemnification
Client agrees to indemnify and hold harmless Provider against any and all claims arising out of Client's use of the services.

## 5. Term and Termination
This agreement shall automatically renew for successive 1-year terms unless terminated with 90 days written notice prior to the end of the current term.

## 6. Intellectual Property
Any intellectual property created during the term of this agreement shall become the exclusive property of the Provider, regardless of prior ownership.
"""
        
        logger.success(f"Parsing complete. Extracted {len(extracted_text)} characters.")
        return extracted_text

    def generate_document_id(self, file_bytes: bytes) -> str:
        return hashlib.md5(file_bytes).hexdigest()
