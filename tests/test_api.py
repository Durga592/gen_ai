import requests

gpt_resp = requests.post("http://localhost:8000/generate", json={"query": "Is this product trustworthy?", "request_model": "gpt"})
print("GPT - ", gpt_resp.json()["response"])

llama_resp = requests.post("http://localhost:8000/generate", json={"query": "Is this product reliable for travel?", "request_model": "llama"})
print("LLAMA - ", llama_resp.json()["response"])
