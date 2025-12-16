from typing import Literal

def route_query(query: str) -> Literal["policy", "ops", "unknown"]:
    q = query.lower()
    if any(k in q for k in ["policy", "guidance", "sop", "procedure", "compliance"]):
        return "policy"
    if any(k in q for k in ["incident", "case", "report", "risk", "assessment"]):
        return "ops"
    return "unknown"