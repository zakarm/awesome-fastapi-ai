from fastapi import FastAPI, Body
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

app = FastAPI(title="FAISS Search API")

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)

docs = ["AI is the future", "FastAPI is great", "We love Python"]
doc_embeddings = model.encode(docs)
index.add(np.array(doc_embeddings))

@app.post("/search")
def search(query: str = Body(...)):
    query_vector = model.encode([query])
    D, I = index.search(np.array(query_vector), k=3)
    return {"matches": [docs[i] for i in I[0]]}
