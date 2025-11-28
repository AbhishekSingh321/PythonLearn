from sentence_transformers import SentenceTransformer, util, CrossEncoder

bi_encoder = SentenceTransformer("all-MiniLM-L6-v2")
cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


corpus = [
    "Machine learning is fascinating.",
    "Artificial intelligence is the future.",
    "Python is a great language for data science.",
    "I love playing football.",
    "Ronaldo and Messi both are great player in football",
    "Mbappe is a Emerging player in football",
    "Deep learning models require a lot of data."
]

corpus_embeddings = bi_encoder.encode(corpus, convert_to_tensor=True)

query="Messi"

query_emb = bi_encoder.encode(query, convert_to_tensor=True)
cos_scores = util.cos_sim(query_emb, corpus_embeddings)[0]

top_k = 3
top_results = cos_scores.topk(top_k)

pair_inputs = [(query, corpus[idx]) for idx in top_results.indices]   # Reranker Using Cross-encoder (Acurate)
rerank_scores = cross_encoder.predict(pair_inputs)

# Merged the two result
final_results = list(zip(rerank_scores, [corpus[i] for i in top_results.indices]))
final_results = sorted(final_results, reverse=True)   # sort by score

for score, text in final_results:
    print(f"{score:.4f}  -  {text}")
