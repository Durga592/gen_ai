from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient(host="localhost", port=6333)
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def search_reviews(query, collection="reviews_demo"):
    query_vec = embed_model.encode(query).tolist()
    results = client.search(collection_name=collection, query_vector=query_vec)
    return [r.payload["text"] for r in results]
