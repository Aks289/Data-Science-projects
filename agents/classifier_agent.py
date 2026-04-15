from tools.llm import call_llm

def classify_document(text: str) -> str:
    prompt = f"""
You are a logistics document classifier.

Classify into ONLY ONE:
- Invoice
- Bill of Lading
- Rate Sheet
- Unknown

Return ONLY the label.

TEXT:
{text[:1500]}
"""

    result = call_llm(prompt).strip()

    valid = ["Invoice", "Bill of Lading", "Rate Sheet"]

    for v in valid:
        if v.lower() in result.lower():
            return v

    return "Unknown"