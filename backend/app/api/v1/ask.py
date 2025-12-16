from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.router import route_query
from app.agents.retrieval_agent import retrieval_agent
from app.agents.reasoning_agent import reasoning_agent
from app.agents.validation_agent import validation_agent
from app.audit.logger import log_event

router = APIRouter()

class AskRequest(BaseModel):
    query: str

@router.post("/ask")
def ask(req: AskRequest):
    route = route_query(req.query)
    pack = retrieval_agent(req.query)
    draft = reasoning_agent(req.query, pack["contexts"])
    validated = validation_agent(draft)

    log_event(
        "ask_request",
        {
            "route": route,
            "sources_count": len(pack["contexts"]),
        },
    )

    return {
        "route": route,
        "sources": pack["contexts"],
        **validated,
    }