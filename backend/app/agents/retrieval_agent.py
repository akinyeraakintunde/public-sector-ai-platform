from app.rag.retriever import retrieve_context

def retrieval_agent(query: str) -> dict:
    contexts = retrieve_context(query)
    return {"query": query, "contexts": contexts}