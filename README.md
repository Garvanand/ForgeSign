# ⚖️ ForgeSign (Day 13)

**ForgeSign** is the Contract Intelligence and Negotiation module for AgentOS. It provides SMEs and freelancers with the intelligence of an elite in-house legal team by translating complex legal text into practical business implications, scoring counterparty risk, and generating native MS Word redlines.

## 🚀 Core Features
- **Practical Implication Engine**: Instead of translating legalese into simpler legalese, ForgeSign translates clauses into concrete financial scenarios ("If this goes wrong, you lose ₹50L but can only recover ₹2L").
- **Native DOCX Redlining**: Uses `python-docx` XML manipulation to output standard "Track Changes", making the AI invisible to the counterparty.
- **Counterparty Intelligence Moat**: Analyzes historical negotiation data to predict whether a specific company (e.g., Salesforce) will accept or reject a specific redline.
- **AgentOS Mesh Integration**: Seamlessly routes Auto-Renewal dates to **GhostCFO (Day 02)** and compiles contract dispute packages for **RiteOfWay (Day 06)**.

## 📚 Documentation
- **[System Architecture](docs/ARCHITECTURE.md)**: Details on the 200K Long-Context extraction pipeline and AgentOS mesh routing.
- **[Negotiation Intelligence](docs/NEGOTIATION_INTELLIGENCE.md)**: How the ChromaDB data moat predicts counterparty behavior.
- **[Redline Mechanics](docs/REDLINE_MECHANICS.md)**: The technical breakdown of generating native `<w:ins>` and `<w:del>` Track Changes in Word.

## 🏗️ Tech Stack
- **AI**: Claude 3.5 Sonnet / Opus (200k context), Groq (Fast classification)
- **Backend**: FastAPI, Pydantic v2
- **Data**: PostgreSQL, ChromaDB (Vector Precedents)
- **Document Processing**: LlamaParse, PyMuPDF, python-docx
- **Frontend**: React 18, Tailwind CSS (Single-file `app.html`)

## 🏃‍♂️ Getting Started

```bash
cd Day13_ForgeSign

# Install dependencies
pip install -r requirements.txt

# Seed the Clause Precedents (ChromaDB)
python server/scripts/seed_clause_library.py

# Run the backend
uvicorn server.api.routes:api_router --host 0.0.0.0 --port 8012

# Open the UI
# Open frontend/app.html in any modern browser
```

> **Mandatory Disclaimer**: *ForgeSign analysis is for informational purposes only and does not constitute legal advice. For legally binding matters, consult a qualified advocate.*
