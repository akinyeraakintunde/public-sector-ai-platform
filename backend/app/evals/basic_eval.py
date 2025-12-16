def basic_grounding_score(answer: str, contexts: list[str]) -> float:
    if not contexts:
        return 0.0
    # crude score: how many context words appear in answer
    ctx_words = set(" ".join(contexts).lower().split())
    ans_words = set(answer.lower().split())
    overlap = len(ctx_words.intersection(ans_words))
    return min(1.0, overlap / 30.0)