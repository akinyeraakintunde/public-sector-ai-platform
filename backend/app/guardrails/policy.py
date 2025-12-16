def is_safe_response(text: str) -> tuple[bool, str]:
    # Simple placeholder guardrails (expand later)
    blocked_terms = ["password", "secret key", "exploit"]
    if any(t in text.lower() for t in blocked_terms):
        return False, "Contains potentially sensitive or unsafe content."
    return True, "OK"