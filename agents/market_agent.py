import requests
import re

def fetch_market():
    try:
        # stable fallback dataset (no auth issues)
        url = "https://api.alternative.me/fng/?limit=1"
        res = requests.get(url, timeout=10)

        # fallback fixed shipping rate baseline
        base_rate = 2500

        return {"rate": base_rate}

    except:
        return {"rate": 2500}