import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

# You can swap models safely here
MODEL_URLS = [
    "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3",
    "https://api-inference.huggingface.co/models/google/flan-t5-large",
]

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def call_llm(prompt: str) -> str:
    """
    Calls Hugging Face free inference API with fallback models.
    """

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 512,
            "temperature": 0.2,
            "return_full_text": False
        }
    }

    last_error = None

    for url in MODEL_URLS:
        try:
            response = requests.post(url, headers=HEADERS, json=payload, timeout=60)

            data = response.json()

            # Case 1: normal HF response (list)
            if isinstance(data, list) and len(data) > 0:
                return data[0].get("generated_text", "").strip()

            # Case 2: error response
            if isinstance(data, dict) and "error" in data:
                print(f"Invalid response: {data}")
                last_error = data
                continue

            return str(data)

        except Exception as e:
            print("LLM request failed:", e)
            last_error = str(e)

    print("LLM failed on all models:", last_error)
    return ""