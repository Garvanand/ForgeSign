"""
Contract Brief Prompts.
Drives the LLM to extract business logic from legal logic.
"""

CONTRACT_BRIEF_PROMPT = """
You are generating a 1-page contract briefing for a business owner who
needs to understand what they're signing without reading the full contract.

Contract type: {contract_type}
Reviewing party: {reviewing_party} (the person/company reading ForgeSign)
Full contract text: {full_contract_text}

Generate a structured contract brief with exactly these sections:

WHAT YOU MUST DO (your obligations):
List 3-5 most significant obligations. Format: "You must [specific obligation]
[by when / how often / under what conditions]"
Example: "You must pay ₹15,000/month, due on the 1st of each month, via bank transfer"

WHAT YOU GET (your rights):
List 3-5 most significant rights. Format: "You have the right to [specific right]"

WHAT COULD HURT YOU (key risks):
List the TOP 3 risks only. Each: [risk description] -> [potential consequence]
Order by severity: worst first.

HOW TO EXIT:
Describe all exit pathways with their conditions and costs.
Include: notice period required, penalties for early exit, what triggers termination.

FINANCIAL EXPOSURE:
- What you pay: [amount and schedule]
- Maximum you can be sued for: [cap amount or "unlimited"]
- Other financial penalties: [list specific amounts]
- Worst-case total exposure: [your assessment]

AUTO-RENEWAL WARNING (if applicable):
If the contract auto-renews, state clearly: "This contract auto-renews [when].
To cancel, you must give notice by [date]. Missing this date commits you to
another [term]."

OVERALL ASSESSMENT (1 sentence):
State clearly whether this contract is: standard, somewhat favorable to one
party, or significantly imbalanced — and which party.

Rules:
- Use specific numbers from the contract (₹ amounts, days, percentages)
- Never say "consult a lawyer" (user knows this — forgesign.ai already says it)
- Be direct: "This clause is dangerous because..." not "You may want to consider..."
- Translate legal jargon: "indemnify" -> "pay the other party's legal costs"
- Flag any clause that has "unlimited" or "sole discretion" language

Format: Strict JSON mapping to the ContractBrief schema fields.
"""
