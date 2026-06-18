# ForgeSign: Native Redline Mechanics

Telling a user "this clause is dangerous" is not a product. Generating a commercially reasonable alternative is.

## The Redline Philosophy
A ForgeSign redline must be:
1. Legally sound.
2. Commercially reasonable (narrowing scope rather than outright deleting).
3. Highly specific (inserting specific market-standard caps rather than vague "fair" wording).

## Track Changes Injection (`python-docx`)
When a user approves a redline, ForgeSign does not just output a text snippet. It exports a fully functional Microsoft Word `.docx` file.

1. **Reconstruction**: ForgeSign maps the original text block to the paragraph object inside the DOCX XML.
2. **Deletion Markup**: It wraps the original text in `<w:del>` XML tags.
3. **Insertion Markup**: It wraps the LLM's proposed replacement in `<w:ins>` XML tags.

**Result**: When the user's counterparty opens the document in Microsoft Word, it natively appears as a standard tracked change made by a human lawyer. They can simply click "Accept" or "Reject". This minimizes friction and makes ForgeSign virtually invisible to the counterparty.
