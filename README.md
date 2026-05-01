# DocuMind 📄

DocuMind is a document-based question answering backend built using FastAPI.

## Features
- Upload PDF documents
- Extract text from documents
- Ask questions based on document content
- Simple and fast API-based system

## Tech Stack
- Python
- FastAPI
- PyPDF
- REST APIs

## API Endpoints

### Upload PDF
POST /upload

### Ask Question
POST /ask

## Screenshots

### API Docs
![Docs](screenshots/api_docs.png)

### Upload
![Upload](screenshots/upload_success.png)

### Ask
![Ask](screenshots/ask_response.png)

## How to Run

```bash
pip3 install -r requirements.txt
uvicorn app.main:app --reload

Open:
http://127.0.0.1:8000/docs


Save.

---

# 🚀 STEP 3 — ADD .gitignore (IMPORTANT)

```bash
nano .gitignore

Paste:

__pycache__/
*.pyc
.DS_Store
venv/
.env
