if __name__ == "__main__":
    query = "Why do users love this product?"
    response = run_agent(query, "gpt")
    print("GPT2 Response:", response)

    response = run_agent(query, "llama")
    print("LLaMA Response:", response)
