from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from qdrant_client.http.models import SearchParams

client = QdrantClient(host="localhost", port=6333)
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def search_reviews(query, collection="reviews_demo", limit=5):
    query_vec = embed_model.encode(query).tolist()
    try:
        results = client.search(
            collection_name=collection,
            query_vector=query_vec,
            limit=limit,
            search_params=SearchParams(hnsw_ef=128)
        )
        return [r.payload.get("text", "") for r in results]
    except Exception as e:
        return [f"Error searching Qdrant: {str(e)}"]
