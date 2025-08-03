from fastapi import APIRouter, Request
from app.agent import run_agent

router = APIRouter()

@router.post("/generate")
async def generate(request: Request):
    data = await request.json()
    query = data.get("query")
    response = run_agent(query)
    return {"query": query, "response": response}
