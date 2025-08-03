from transformers import pipeline
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

def generate_response(context, query, request_model):
    if request_model == "gpt":
        try:
            prompt = f"Reviews:\n{context}\n\nQuery: {query}\nAnswer:"
            print(f"prompt: {prompt}")
            gen_pipeline = pipeline("text-generation", model="gpt2")
            result = gen_pipeline(prompt, max_length=100, do_sample=True)

            if not result or not isinstance(result, list):
                return "GPT2 did not return a valid response."

            return result[0].get("generated_text", "").strip()

        except Exception as e:
            return f"GPT2 Error: {str(e)}"

    elif request_model == "llama":
        try:
            prompt = PromptTemplate.from_template("""
            Based on these reviews:
            {context}

            Answer this query: {query}
            """)
            print(f"prompt: {prompt}")
            llm = Ollama(model="mistral")
            response = llm(prompt.format(context=context, query=query))
            return response if response else "LLaMA returned no answer."
        except Exception as e:
            return f"LLaMA Error: {str(e)}"

    else:
        return "Unsupported model type."
