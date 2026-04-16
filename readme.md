# 🚚 Logistics Agent System

An intelligent multi-agent backend system designed to automate logistics operations such as document ingestion, data extraction, deduplication, cost analysis, and market insights using AI agents.

---

## 📌 Overview

The Logistics Agent System leverages an agent-based architecture to process logistics data from multiple sources (email, PDFs, APIs), extract structured insights, and support decision-making for cost optimization and operational efficiency.

---

## 🎯 Key Features

- 📩 **Email Integration**
  - Fetch unread emails
  - Extract PDF attachments automatically

- 📄 **Document Processing**
  - Parse logistics-related PDFs (invoices, shipping docs)
  - Classify document types

- 🤖 **Multi-Agent Architecture**
  - Extraction Agent → Extracts structured data
  - Classification Agent → Identifies document types
  - Deduplication Agent → Removes duplicate entries
  - Analytics Agent → Computes cost insights
  - Research Agent → Fetches market data (e.g., Freight Index)

- 🧠 **AI-Powered Processing**
  - Uses LLMs (via OpenRouter or similar)
  - Structured data extraction from unstructured documents

- 📊 **Analytics & Insights**
  - Average freight cost calculation
  - Trend analysis
  - Decision support for logistics optimization

---

## 🏗️ System Architecture
Email / GDrive → Fetch Agent → PDF Loader
↓
Extractor Agent → Classifier Agent
↓
Deduplication Agent
↓
Database
↓
Analytics Agent → Insights / Reports
↓
Research Agent → External Data (e.g., Freight Index)

---

## ⚙️ Tech Stack

- **Language:** Python  
- **Framework:** Agent-based (Hermes / custom agents)  
- **LLM Provider:** OpenRouter (or any supported LLM API)  
- **Libraries:**
  - `imapclient` – Email fetching
  - `pdfplumber` / `PyMuPDF` – PDF parsing
  - `pandas` – Data processing
  - `sqlite3` / `PostgreSQL` – Database
- **Optional:**
  - Apify – Web scraping
  - FastAPI – API layer

---


