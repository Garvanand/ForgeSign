"""
ForgeSign Prompts.
The core instructions driving the Claude LLM engine.
"""

# This is the most important prompt in ForgeSign. It generates the
# real-world scenarios that make abstract clauses concrete and actionable.
PRACTICAL_IMPLICATION_PROMPT = """
You are analyzing a contract clause for a business owner who needs to
understand how this clause would actually play out in real disputes.

Contract type: {contract_type}
Clause type: {clause_type}
Clause text: {verbatim_text}

Generate exactly 3 specific real-world scenarios where this clause would
be invoked. For each scenario:
1. Describe a specific, realistic business situation (2-3 sentences)
2. Explain what happens under the CURRENT clause wording
3. State clearly who benefits (the clause reviewer or the counterparty)
4. Rate the severity of the outcome for the clause reviewer (low/medium/high)

Rules for scenarios:
- Make them specific and realistic (not theoretical)
- Each scenario should be DIFFERENT (don't repeat similar situations)
- At least one scenario should be the most common real-world trigger
- At least one scenario should be the worst-case trigger
- Use specific numbers where appropriate ("$50,000 dispute", "3-month delay")

After the 3 scenarios, add:
- ONE sentence: "The current wording is [neutral/slightly favorable to reviewer/
  significantly favorable to counterparty/extremely risky for reviewer]"
- ONE sentence: what a better version of this clause would look like conceptually

Format: JSON with fields: scenario_1, scenario_2, scenario_3, overall_assessment, better_version_concept
"""
