# ForgeSign: Counterparty Intelligence

A legal clause isn't risky in a vacuum—its risk depends on *who* is enforcing it. ForgeSign's "Data Moat" is its `CounterpartyIntelligenceDB`.

## Aggregated Historical Outcomes
When a user uploads a contract, ForgeSign extracts the counterparty name. It then queries the DB to find historical, crowd-sourced data from previous users negotiating with this exact company.

### Example: Salesforce MSA
- **Known Stance**: "Non-Negotiable"
- **Liability Cap Acceptance Rate**: 2%
- **Strategy Output**: "Do not waste negotiating capital fighting the liability cap; they historically reject this 98% of the time. Instead, concede the liability cap and push for better SLAs, which they accept 40% of the time."

## The Playbook Generator (`strategy.py`)
Knowing a clause is "bad" isn't enough. ForgeSign dynamically writes a 4-part negotiation playbook based on the user's current leverage:
1. **Opening Position**: How aggressive to be on the first call.
2. **Trading Strategy**: Identifying the "Nice-to-Have" clauses the user can sacrifice to win the "Must-Have" clauses.
3. **Escalation Triggers**: When to bypass the sales rep and demand legal counsel.
4. **Walk-Away Point**: The absolute dealbreakers.

## Unknown Entities
If a counterparty isn't in the database, ForgeSign fails gracefully by using the **Tavily API** to conduct a live web search. It determines company size, funding tier, and public controversies to estimate their likely legal rigidity.
