from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

corpus = [
    "Machine learning is fascinating.",
    "Artificial intelligence is the future.",
    "Python is a great language for data science.",
    "I love playing football.",
    "Ronaldo and Messi both are great player in football",
    "Mbappe is a Emerging player in football",
    "Deep learning models require a lot of data."
]

corpus_embeddings = model.encode(corpus)

def semantic_search(query, top_k=3):
    query_emb = model.encode(query, convert_to_tensor=True)
    scores = util.cos_sim(query_emb, corpus_embeddings)[0]
    results = scores.topk(top_k)

    for idx, score in zip(results.indices, results.values):
        print(f"{score:.4f}  -  {corpus[idx]}")

semantic_search("Messi",3)
