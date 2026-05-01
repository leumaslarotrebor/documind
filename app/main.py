from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from app.pdf_utils import read_pdf
from app.vector_store import build_index, search

app = FastAPI()

stored_chunks = []


class QueryRequest(BaseModel):
    question: str


def split_text(text, chunk_size=1000):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks


@app.get("/")
def home():
    return {"status": "DocuMind running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global stored_chunks

    if not file.filename.endswith(".pdf"):
        return {"error": "Upload PDF only"}

    text = read_pdf(file.file)

    if not text.strip():
        return {"error": "Empty PDF"}

    stored_chunks = split_text(text)
    build_index(stored_chunks)

    return {
        "message": "PDF processed",
        "chunks": len(stored_chunks)
    }


@app.post("/ask")
def ask_question(request: QueryRequest):
    if not stored_chunks:
        return {"error": "Upload PDF first"}

    results = search(request.question)

    if not results:
        return {"answer": "No relevant info found"}

    return {"answer": results[0]}
