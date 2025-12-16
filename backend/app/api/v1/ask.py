from fastapi import APIRouter
from pydantic import BaseModel
from backend.app.agents.router import route_query
from backend.app.agents.retrieval_agent import retrieval_agent
from backend.app.agents.reasoning_agent import reasoning_agent
from backend.app.agents.validation_agent import validation_agent

router = APIRouter()

class AskRequest(BaseModel):
    query: str

@router.post("/ask")
def ask(req: AskRequest):
    route = route_query(req.query)
    pack = retrieval_agent(req.query)
    draft = reasoning_agent(req.query, pack["contexts"])
    validated = validation_agent(draft)
    return {"route": route, "sources": pack["contexts"], **validated}