from agents.classifier_agent import classify_document
from agents.extractor_agent import extract_data
import json

sample_text = """
Invoice
Order ID: 10248
Customer Name: Paul Henriot
Ship City: Reims
Ship Country: France
Order Date: 2016-07-04
Total Price: 440.0
"""

doc_type = classify_document(sample_text)
print("TYPE:", doc_type)

extracted = extract_data(sample_text)

try:
    data = json.loads(extracted)
    print("EXTRACTED DATA:", data)
except:
    print("RAW OUTPUT:", extracted)