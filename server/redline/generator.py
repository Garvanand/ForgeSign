"""
Track Changes Generator.
Injects LLM-generated redlines natively into MS Word XML or PDF.
"""
from pydantic import BaseModel
from typing import List, Optional
from loguru import logger
import os

class ClauseRedline(BaseModel):
    clause_id: str
    original_text: str
    redlined_text: str
    rationale: str
    priority: str

class TrackChangesGenerator:

    def apply_redlines_to_docx(
        self,
        original_docx_path: str,
        redlines: List[ClauseRedline],
        output_path: str
    ) -> str:
        """
        Generate a DOCX with proper Track Changes markup.
        python-docx doesn't natively support Track Changes XML.
        Strategy:
        1. Load original DOCX with python-docx
        2. For each redlined clause: find text, apply deletion/insertion markup
        3. Use python-docx's low-level XML manipulation to insert
           w:del and w:ins elements (Track Changes XML)
        4. Save to new file

        Track Changes XML structure:
        <w:del w:id="1" w:author="ForgeSign" w:date="...">
            <w:r><w:delText>deleted text</w:delText></w:r>
        </w:del>
        <w:ins w:id="2" w:author="ForgeSign" w:date="...">
            <w:r><w:t>inserted text</w:t></w:r>
        </w:ins>
        """
        logger.info(f"Injecting {len(redlines)} redlines into native DOCX XML.")
        
        # MOCK IMPLEMENTATION of XML injection:
        # In production, we iterate over document.paragraphs, regex match the original_text,
        # clear the paragraph.p element, and append OxmlElements for w:del and w:ins.
        
        # simulated docx save
        with open(output_path, "w") as f:
            f.write("MOCK DOCX BINARY WITH NATIVE TRACK CHANGES XML")
            
        logger.success(f"DOCX Track Changes saved to {output_path}")
        return output_path

    def generate_redline_pdf(
        self,
        contract_text: str,
        redlines: List[ClauseRedline],
        output_path: str
    ) -> str:
        """
        Alternative: generate a PDF showing changes in colored text.
        Red strikethrough = deleted text
        Green underline = inserted text
        Use ReportLab for generation.
        """
        logger.info(f"Generating colored PDF redline output.")
        
        # MOCK IMPLEMENTATION using ReportLab
        with open(output_path, "w") as f:
            f.write("MOCK PDF BINARY WITH STRIKETHROUGH AND UNDERLINE")
            
        logger.success(f"PDF Redlines saved to {output_path}")
        return output_path
