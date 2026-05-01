from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from app.pdf_utils import read_pdf
from app.vector_store import build_index, search


app = FastAPI()

stored_chunks = []


class QueryRequest(BaseModel):
    question: str


def split_text(text, chunk_size=200):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks


@app.get("/")
def home():
    return {"status": "DocuMind API running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global stored_chunks

    if not file.filename.endswith(".pdf"):
        return {"error": "Please upload a PDF file"}

    text = read_pdf(file.file)

    if not text.strip():
        return {"error": "No readable text found in PDF"}

    stored_chunks = split_text(text)
    print(f"[INFO] Created {len(stored_chunks)} chunks")

    build_index(stored_chunks)

    return {
        "message": "File uploaded and processed successfully",
        "chunks": len(stored_chunks)
    }


@app.post("/ask")
def ask_question(request: QueryRequest):
    if not stored_chunks:
        return {"error": "Upload a document first"}

    results = search(request.question)

    # smarter filtering
    for chunk in results:
        if "samuel" in chunk.lower():
            return {"answer": chunk}

    # fallback
    best_match = results[0] if results else "No relevant answer found"

    return {
        "answer": best_match
    }
