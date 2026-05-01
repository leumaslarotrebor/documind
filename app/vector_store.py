documents = []

def build_index(chunks):
    global documents
    documents = chunks
    print(f"[INFO] Stored {len(documents)} chunks")


def search(query, top_k=3):
    results = []

    for chunk in documents:
        if query.lower() in chunk.lower():
            results.append(chunk)

    return results[:top_k]
