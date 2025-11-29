from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

corpus = [
    "Airplanes stay in the air because their wings create lift.",
    "The capital of France is Paris.",
    "Machine learning models learn patterns from data.",
    "The Wright brothers flew the first powered airplane in 1903.",
    "An airfoil shape creates a pressure difference that lifts an aircraft.",
    "Neural networks are composed of layers of interconnected nodes.",
    "The sky appears blue due to Rayleigh scattering.",
    "Jet engines produce thrust by expelling high-speed exhaust.",
    "Birds achieve lift using wings and flapping motion.",
    "Physics explains how forces act on objects."
]    # Add thousands/millions of documents here

corpus_embeddings = model.encode(corpus, convert_to_numpy=True)
d = corpus_embeddings.shape[1]   # vector dimension

index = faiss.IndexFlatL2(d)
index.add(corpus_embeddings)

query = "How do airplanes stay in the air?"
query_emb = model.encode([query], convert_to_numpy=True)

k = 5
D, I = index.search(query_emb, k)

for idx in I[0]:
    print(corpus[idx])