"""
Counterparty Intelligence DB.
Connects to ChromaDB + Postgres to pull aggregated historical negotiation outcomes.
Falls back to Tavily web-search for unknown counterparties.
"""
from loguru import logger
import asyncio
from datetime import datetime
from .schemas import CounterpartyProfile, CounterpartyResearch, ClauseStance

class CounterpartyIntelligenceDB:
    """
    Stored in ChromaDB (for semantic search) + PostgreSQL (structured)
    Sources:
    1. Crowd-sourced: ForgeSign users report negotiation outcomes
       (anonymized: "Counterparty accepted / rejected / countered this redline")
    2. Public sources: published contract templates, SEC filings (US),
       press reports about company practices
    3. Known patterns: common practices for industry/company type
    """

    async def get_counterparty_profile(
        self,
        company_name: str,
        contract_type: str
    ) -> CounterpartyProfile:
        """
        Returns:
        - Is this company known to ForgeSign?
        - Their typical negotiation stance per clause type
        - Historical acceptance rates for common redlines
        - Known non-negotiable positions
        - Recommended approach (collaborative vs firm)
        - Typical response time for contract negotiations
        """
        logger.info(f"Querying ChromaDB/Postgres for Counterparty Profile: {company_name}")
        await asyncio.sleep(0.5) # Simulate DB lookup
        
        # MOCK IMPLEMENTATION showing a highly rigid SaaS provider
        if company_name.lower() in ["salesforce", "aws", "microsoft"]:
            return CounterpartyProfile(
                company_name=company_name,
                company_name_normalized=company_name.lower().strip(),
                data_quality="known_high",
                negotiation_style="non-negotiable",
                clause_stances={
                    "limitation_of_liability": ClauseStance(
                        acceptance_rate=0.02, 
                        typical_counter_offer="Will not increase cap above 12 months.", 
                        is_non_negotiable=True
                    ),
                    "auto_renewal": ClauseStance(
                        acceptance_rate=0.45, 
                        typical_counter_offer="Will agree to 30-day notice instead of 90-day.", 
                        is_non_negotiable=False
                    )
                },
                recommended_approach="Take it or leave it on liability. Push on operational clauses only.",
                clauses_worth_fighting=["auto_renewal", "payment_terms", "sla_credits"],
                clauses_not_worth_fighting=["limitation_of_liability", "indemnification", "governing_law"],
                known_dealbreakers=["unlimited_liability", "ip_assignment"],
                reports_count=1450,
                last_updated=datetime.now(),
                confidence=0.95
            )
            
        # Fallback for unknown
        return CounterpartyProfile(
            company_name=company_name,
            company_name_normalized=company_name.lower().strip(),
            data_quality="unknown",
            negotiation_style="moderate",
            clause_stances={},
            recommended_approach="Standard collaborative negotiation.",
            clauses_worth_fighting=[],
            clauses_not_worth_fighting=[],
            known_dealbreakers=[],
            reports_count=0,
            last_updated=datetime.now(),
            confidence=0.1
        )

    async def research_counterparty(
        self,
        company_name: str
    ) -> CounterpartyResearch:
        """
        For unknown companies: web research using Tavily API
        Look for:
        - Company size, funding, reputation
        - Any public controversy about contracts
        - Industry: informs likely contract stance
        - Whether they're likely using a template or custom agreement
        Returns: high-level assessment of likely negotiation approach
        """
        logger.info(f"Initiating Tavily web-search for unknown counterparty: {company_name}")
        await asyncio.sleep(1.0) # Simulate API call
        
        return CounterpartyResearch(
            company_size="Mid-Market (500-1000 employees)",
            industry="B2B FinTech",
            likely_stance="Firm on Data Privacy, flexible on commercial terms.",
            public_controversies=["2023 lawsuit regarding SLA uptime failures"]
        )
