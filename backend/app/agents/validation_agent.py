from backend.app.guardrails.policy import is_safe_response

def validation_agent(answer: str) -> dict:
    ok, reason = is_safe_response(answer)
    return {"valid": ok, "reason": reason, "answer": answer if ok else "Blocked by guardrails."}