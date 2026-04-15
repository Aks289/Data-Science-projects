import json

from tools.input_selector import choose_input_source
from tools.pdf_reader import read_pdf

from agents.loader_agent import load_from_email, load_from_local, load_from_gdrive
from agents.classifier_agent import classify_document
from agents.extractor_agent import extract_data
from agents.dedupe_agent import save_if_not_exists
from agents.pricing_agent import compute_avg_cost
from agents.market_agent import fetch_market
from agents.report_agent import generate_report
from agents.feedback_agent import feedback


def run():

    print("\n🚀 Starting Logistics Agent System...\n")

    # 1️⃣ Select input source
    choice = choose_input_source()

    if choice == "1":
        pdfs = load_from_email()
    elif choice == "2":
        pdfs = load_from_gdrive()
    elif choice == "3":
        pdfs = load_from_local()
    else:
        print("❌ Invalid choice")
        return

    if not pdfs:
        print("⚠️ No PDFs found!")
        return

    extracted_records = []

    # 2️⃣ Process PDFs
    for pdf in pdfs:
        print(f"\n📄 Processing: {pdf}")

        try:
            text = read_pdf(pdf)

            if not text:
                print("⚠️ Empty PDF text, skipping")
                continue

            # 🔍 Classification
            doc_type = classify_document(text)
            print("📌 Type:", doc_type)

            # 🧠 Extraction
            data = extract_data(text)

            if not data:
                print("⚠️ Extraction failed, skipping")
                continue

            print("📦 Extracted:", data)

            # 💾 Save (dedupe handled inside)
            saved = save_if_not_exists(data)

            if saved:
                extracted_records.append(data)

        except Exception as e:
            print(f"❌ Error processing {pdf}: {e}")
            continue

    # 3️⃣ Compute analytics
    print("\n📊 Computing analytics...")

    try:
        avg_cost = compute_avg_cost()
    except Exception as e:
        print("⚠️ Avg cost error:", e)
        avg_cost = 0

    try:
        market = fetch_market()
    except Exception as e:
        print("⚠️ Market API error:", e)
        market = {"rate": 2500}

    # 4️⃣ Generate report
    report = generate_report(avg_cost, market)

    print("\n📊 FINAL REPORT")
    print(json.dumps(report, indent=2))

    # 5️⃣ Feedback loop
    try:
        fb = feedback(report)
        print("\n🔁 Feedback:", fb)
    except Exception as e:
        print("⚠️ Feedback error:", e)


if __name__ == "__main__":
    run()