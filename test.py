from edgar import Company, set_identity
import anthropic
import json
import re

set_identity("Research test@uni.edu")

# Pull HTLD debt note
c = Company("HTLD")
f = c.get_filings(form="10-K").latest(1).obj()
notes = f.notes
debt_keywords = ["debt", "credit", "borrowing", "loan", "revolving", "financing"]
debt_notes = [n for n in notes if any(kw in n.title.lower() for kw in debt_keywords)]

print("Debt notes found:", len(debt_notes))
for n in debt_notes:
    print(" -", n.title)

# Get the actual long-term debt note (index 1 since index 0 is credit risk)
debt_text = str(debt_notes[1].text)[:3000]
print("\nDEBT NOTE PREVIEW:")
print(debt_text[:500])

# Get balance sheet
bs_text = str(f.balance_sheet)[:1000]
print("\nBALANCE SHEET PREVIEW:")
print(bs_text[:300])

# Now send to Claude
from config import ANTHROPIC_API_KEY
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

prompt = f"""
Does this 10-K text mention any debt, loans or credit facilities?
Return ONLY this JSON, nothing else:
{{"has_debt": true or false, "lender_name": "name or None", "key_finding": "one sentence"}}

TEXT:
{debt_text[:2000]}
"""

print("\nSENDING TO CLAUDE...")
resp = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=[{"role": "user", "content": prompt}]
)
raw = resp.content[0].text.strip()
print("CLAUDE RAW RESPONSE:")
print(raw)

# Try to parse
try:
    # Strip markdown code fences
    clean = raw.replace("```json", "").replace("```", "").strip()
    print("CLEANED:", clean[:200])
    parsed = json.loads(clean)
    print("PARSED OK:", parsed)
except Exception as e:
    print("PARSE ERROR:", e)