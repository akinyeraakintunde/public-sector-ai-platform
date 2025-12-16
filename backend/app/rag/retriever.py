from backend.app.rag.vector_store import DOCUMENTS

def retrieve_context(query: str) -> list[str]:
    q = query.lower()
    hits = [d for d in DOCUMENTS if any(w in d.lower() for w in q.split())]
    return hits[:5]