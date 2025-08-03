from app.vector_db import search_reviews
from app.llm_service import generate_response


def run_agent(query, request_model):
    if request_model == "llama":
        docs = search_reviews(query)
        context = "\n".join(docs)
        if not context:
            return "No relevant context found from reviews."
        return generate_response(context, query, request_model)

    elif request_model == "gpt":
        # Static context or default fallback
        context = "Users have shared mixed opinions on the product. Some found it helpful, others reported issues."
        return generate_response(context, query, request_model)

    else:
        return "Invalid model type."
