def retrieve(chunks: list, question: str) -> str:
    """Mock retrieval function: returns the best matching chunk."""
    if not chunks:
        return ""
    if "YOLO" in question:
        return next((c for c in chunks if "YOLO" in c), chunks[0])
    if "RAG" in question:
        return next((c for c in chunks if "RAG" in c), chunks[0])
    if "MCP" in question:
        return next((c for c in chunks if "MCP" in c), chunks[0])
    return chunks[0]

def answer(chunks: list, question: str) -> dict:
    """Returns a dict with context and answer."""
    context = retrieve(chunks, question)
    return {
        "context": context,
        "answer": context
    }
