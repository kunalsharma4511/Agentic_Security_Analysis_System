# Agentic Security Analysis System

An end-to-end **agentic AI system** that analyzes unstructured security reports and generates risk assessments and actionable remediation recommendations.

## 🚀 Features
- Multi-agent architecture using **LangGraph**
- Retrieval-Augmented Generation (RAG) with **FAISS**
- LLM-based risk classification and decision-making
- Conditional tool invocation (e.g., CVE lookup)
- Interactive **Streamlit UI**
- End-to-end latency: ~7–10 seconds

## 🧠 System Architecture
Agents involved:
1. **Ingestion Agent** – Parses and normalizes security reports
2. **Retrieval Agent** – Fetches relevant security context using FAISS
3. **Analysis Agent** – Determines risk severity using LLM reasoning
4. **Recommendation Agent** – Generates mitigation steps

## 🛠 Tech Stack
- Python
- LangGraph
- LangChain
- FAISS
- Hugging Face / Gemini LLMs
- Streamlit

## 🖥 Running Locally
```bash
pip install -r requirements.txt
streamlit run ui/app.py
