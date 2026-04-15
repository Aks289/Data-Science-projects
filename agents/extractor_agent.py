import json
from tools.llm import call_llm

def extract_data(text: str):
    prompt = f"""
Extract structured JSON ONLY:

{{
  "shipment_id": "string",
  "origin": "string",
  "destination": "string",
  "cost": number,
  "date": "string"
}}

Rules:
- If missing use "UNKNOWN"
- cost must be number only
- return ONLY JSON

TEXT:
{text[:2000]}
"""

    result = call_llm(prompt)

    try:
        start = result.find("{")
        end = result.rfind("}") + 1

        json_str = result[start:end]
        return json.loads(json_str)

    except Exception:
        print("LLM failed → using fallback extraction")
        return {
            "shipment_id": "UNKNOWN",
            "origin": "UNKNOWN",
            "destination": "UNKNOWN",
            "cost": 0,
            "date": "UNKNOWN"
        }