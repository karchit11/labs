def retrieve(chunks: list[str], question: str) -> str:
    """
    Retrieve the most relevant chunk using simple word overlap.

    Args:
        chunks:   List of text strings (the knowledge base).
        question: The user's question.

    Returns:
        The single chunk string with the highest word overlap score.
    """
    question_words = set(question.lower().split())

    best_chunk = chunks[0]
    best_score = -1

    for chunk in chunks:
        chunk_lower = chunk.lower()
        score = sum(1 for word in question_words if word in chunk_lower)
        if score > best_score:
            best_score = score
            best_chunk = chunk

    return best_chunk


def answer(chunks: list[str], question: str) -> dict:
    """
    Retrieve the best context and build a simple answer.

    Args:
        chunks:   The knowledge base.
        question: The user's question.

    Returns:
        A dict with keys: 'context' (str) and 'answer' (str).
        'answer' must be a non-empty string.
    """
    context = retrieve(chunks, question)
    return {
        "context": context,
        "answer": f"Based on the context: {context}",
    }
