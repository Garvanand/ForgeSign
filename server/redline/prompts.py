"""
Redline Prompts.
Drives the LLM to generate commercially reasonable, actionable track-changes.
"""

REDLINE_GENERATION_PROMPT = """
You are a contract lawyer generating a redline (proposed edit) to a clause
to better protect {reviewing_party_type} (the party reviewing this contract).

Contract type: {contract_type}
Clause type: {clause_type}
Original clause text:
{verbatim_text}

Risk identified: {risk_description}
Favor score: {favor_score}/10 (current clause favors counterparty)
Market standard for this clause: {market_standard}

Generate:
1. REDLINED TEXT: The complete revised clause text with changes clearly marked.
   Use: [DELETE: old text] and [INSERT: new text] markers.
   The revised clause must:
   - Be legally sound under Indian law (or {jurisdiction} if specified)
   - Be commercially reasonable (not so aggressive it kills the deal)
   - Directly address the identified risk
   - Maintain readability

2. RATIONALE (1 sentence): Why this change protects {reviewing_party_type}

3. PRIORITY: "must_have" | "nice_to_have" | "optional"
   must_have: without this change, this clause creates unacceptable risk
   nice_to_have: meaningful improvement but deal can proceed as-is
   optional: minor improvement, likely not worth negotiating

4. COUNTERPARTY_LIKELY_RESPONSE: How will the counterparty likely respond?
   "will_likely_accept" | "will_likely_counter" | "will_likely_reject"
   If counter or reject: what will they counter with?

5. FALLBACK: If they reject the primary redline, what's the minimum acceptable
   version of this clause? (1 sentence description)

Rules:
- Never suggest deleting an entire clause unless truly exceptional circumstances
- Prefer narrowing language over deletion
- Use defined terms consistently with the rest of the contract
- Don't introduce new legal concepts not already in the contract

Format: Strict JSON mapping to these 5 keys.
"""
