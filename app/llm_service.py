from transformers import pipeline

gen_pipeline = pipeline("text-generation", model="gpt2")

def generate_response(context, query):
    prompt = f"Reviews:\n{context}\n\nQuery: {query}\nAnswer:"
    result = gen_pipeline(prompt, max_length=100, do_sample=True)[0]["generated_text"]
    return result
