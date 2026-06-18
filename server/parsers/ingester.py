"""
Contract Ingester.
Handles multi-format parsing, falling back to LlamaParse for complex PDFs.
"""
from pydantic import BaseModel
from typing import List
from loguru import logger
import re

class ContractSection(BaseModel):
    title: str
    content: str
    section_index: int

class ContractText(BaseModel):
    raw_text: str
    sections: List[ContractSection]

class ContractIngester:

    async def ingest_pdf(self, pdf_path: str) -> ContractText:
        """
        Primary: PyMuPDF (fast, handles most PDFs)
        For complex PDFs (scanned, forms): LlamaParse API
        Extract: clean text with section markers preserved
        """
        logger.info(f"Ingesting PDF: {pdf_path} via PyMuPDF/LlamaParse")
        # MOCK IMPLEMENTATION
        mock_text = "1. TERM AND TERMINATION\nThis agreement lasts for 1 year.\n2. PAYMENT\nPay in 30 days."
        return ContractText(
            raw_text=mock_text,
            sections=self.detect_sections(mock_text)
        )

    async def ingest_docx(self, docx_path: str) -> ContractText:
        """
        python-docx: preserve paragraph structure, heading levels
        Detect: heading styles -> use as section boundaries
        """
        logger.info(f"Ingesting DOCX: {docx_path} via python-docx")
        mock_text = "1. TERM AND TERMINATION\nThis agreement lasts for 1 year.\n2. PAYMENT\nPay in 30 days."
        return ContractText(
            raw_text=mock_text,
            sections=self.detect_sections(mock_text)
        )

    async def ingest_text(self, raw_text: str) -> ContractText:
        """Direct text paste — minimal processing needed"""
        logger.info(f"Ingesting raw text payload.")
        return ContractText(
            raw_text=raw_text,
            sections=self.detect_sections(raw_text)
        )

    def detect_sections(self, text: str) -> List[ContractSection]:
        """
        Identify sections using:
        1. Numbered headers: "1.", "2.", "1.1", "Section 1"
        2. All-caps headers: "TERM AND TERMINATION"
        Returns: list of sections with title + content
        """
        sections = []
        
        # MOCK REGEX LOGIC for finding numbered headers e.g. "1. SOMETHING"
        pattern = r"(?:\n|^)(\d+\.\s+[A-Z\s]+)(.*?)(?=(?:\n\d+\.\s+[A-Z\s]+)|$)"
        matches = re.findall(pattern, text, re.DOTALL)
        
        for idx, match in enumerate(matches):
            title = match[0].strip()
            content = match[1].strip()
            sections.append(ContractSection(title=title, content=content, section_index=idx))
            
        if not sections:
            # Fallback if no clean sections found
            sections.append(ContractSection(title="Full Document", content=text, section_index=0))
            
        return sections
