def reasoning_agent(query: str, contexts: list[str]) -> str:
    # Placeholder "reasoning" until we integrate an LLM
    if not contexts:
        return "I could not find relevant sources. Please provide more details or upload related documents."
    return "Answer drafted from sources: " + " | ".join(contexts[:3])