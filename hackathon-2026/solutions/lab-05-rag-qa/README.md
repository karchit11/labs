# Lab 05: RAG Q&A 📚

**Difficulty**: Hard

## Objective
Implement the retrieval core of a Retrieval-Augmented Generation (RAG) system.

## Task
Implement `get_context(query, documents)` in `solution.py`.

## Instructions
1. **Search**: Find the top 2 documents that contain keywords from the query.
2. **Format**: Join them with a newline separator.
3. **Fallback**: If no matches, return "No relevant context found."

## Example
**Query**: "When was Python released?"
**Docs**: ["Python was released in 1991", "Java was released in 1995"]
**Output**: "Python was released in 1991"

## Common Mistakes
- Returning all documents instead of filtering.
- Case sensitivity (e.g., "Python" vs "python").
