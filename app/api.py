from fastapi import APIRouter, Request
from app.agent import run_agent

router = APIRouter()

@router.post("/generate")
async def generate(request: Request):
    data = await request.json()
    query = data.get("query")
    request_model = data.get("request_model")

    if not query or not request_model:
        return {"error": "Missing required fields: 'query' and 'request_model'"}

    response = run_agent(query, request_model)
    return {"query": query, "response": response}
