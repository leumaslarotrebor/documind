import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
index = None
documents = []


def build_index(chunks):
    global index, documents

    documents = chunks

    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    print(f"[INFO] Indexed {index.ntotal} chunks")


def search(query, top_k=3):
    global index

    if index is None:
        return []

    query_vector = model.encode([query])
    query_vector = np.array(query_vector).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = [documents[i] for i in indices[0]]
    return results
