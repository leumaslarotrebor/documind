# DocuMind — AI Document Intelligence System

## 🚀 Overview

DocuMind is a Retrieval-Augmented Generation (RAG) system that enables semantic querying over document corpora using LLMs.

Unlike traditional keyword search, DocuMind retrieves contextually relevant information using embeddings and generates accurate responses using an LLM.

---

## ⚙️ Problem

Standard document search systems rely on keyword matching, which fails when context and meaning matter across large documents.

---

## 🧠 Solution

Designed a semantic retrieval pipeline using embeddings + vector search + LLM synthesis.

---

## 🏗 System Architecture

1. Document ingestion (PDF upload)
2. Text extraction and chunking
3. Embedding generation
4. Vector storage (FAISS / in-memory)
5. Semantic retrieval (top-k similarity)
6. LLM-based response generation
7. FastAPI backend for API access

---

## 🧪 Tech Stack

* Python
* FastAPI
* LangChain (if used)
* FAISS (if used — add only if true)
* OpenAI API / LLM integration
* PyPDF

---

## ⚡ Key Features

* Semantic document search (not keyword-based)
* Context-aware LLM responses
* Modular pipeline architecture
* API-first design

---

## 🔌 API Endpoints

### Upload Document

POST /upload

### Ask Question

POST /ask

---

## ▶️ How to Run

```bash
git clone https://github.com/leumaslarotrebor/documind
cd documind
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
http://127.0.0.1:8000/docs

---

## 📌 Future Improvements

* Streaming responses
* Better ranking (reranking models)
* UI dashboard
* Persistent vector DB

---

