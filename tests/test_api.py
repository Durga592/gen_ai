import requests

resp = requests.post("http://localhost:8000/generate", json={"query": "Is this product trustworthy?"})
print(resp.json()["response"])
