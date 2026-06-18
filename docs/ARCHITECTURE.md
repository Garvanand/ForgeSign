# ForgeSign: System Architecture

ForgeSign translates dense legal text into actionable business intelligence. It does this by bypassing traditional keyword search and RAG-chunking in favor of **Long-Context Structured Extraction**.

## 1. The Full-Context Imperative
Contracts rely heavily on cross-references (e.g., *"Subject to the limitations in Section 4(b)(ii)"*). Standard RAG chunking destroys this context. 
ForgeSign leverages Claude 3.5 Sonnet / Opus's 200,000 token context window. By feeding the entire document (up to ~100 pages) into the LLM in a single pass, we guarantee that the LLM understands the interplay between clauses.

## 2. The 3-Layer Extraction
For every flagged clause, ForgeSign generates three distinct layers:
- **Layer 1 (Legal Meaning)**: Plain English summary (e.g., "Liability is capped at 3 months of fees").
- **Layer 2 (Practical Implication)**: Mathematical/Operational scenarios (e.g., "If an outage loses you ₹50L, you can only sue for ₹2L").
- **Layer 3 (Negotiation Stance)**: Favorability scoring and priority mapping (e.g., "This strongly favors the vendor. Push back.").

## 3. The 1-Page Business Brief
Lawyers read linearly; business owners read for risk. The `ContractBrief` schema forces the LLM to distill 50 pages into 5 bullet points:
1. What you must DO.
2. What you GET.
3. What could HURT you.
4. Total FINANCIAL EXPOSURE.
5. How to EXIT.

## 4. AgentOS Mesh Routing
ForgeSign acts as the legal intelligence node in the 30-agent OS:
- **GhostCFO (Day 02)**: Auto-renewal clauses instantly trigger calendar alerts via the mesh API to prevent unwanted contract roll-overs.
- **RiteOfWay (Day 06)**: Upon user dispute, ForgeSign packages the violated clause and sends it to RiteOfWay to draft a legal demand letter.
- **NexusOps (Day 29)**: Triggers auto-analysis when a contract is detected in an incoming email.
