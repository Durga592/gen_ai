from app.vector_db import search_reviews
from app.llm_service import generate_response

def run_agent(query):
    docs = search_reviews(query)
    joined = " ".join(docs)
    answer = generate_response(joined, query)
    return answer
