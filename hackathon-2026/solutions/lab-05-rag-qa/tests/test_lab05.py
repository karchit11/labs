"""Tests for Lab 05: RAG Q&A"""
import pytest
from solution import retrieve, answer

CHUNKS = [
    "YOLO is a real-time object detection algorithm used for identifying vehicles.",
    "RAG stands for Retrieval Augmented Generation and reduces hallucinations.",
    "MCP is the Model Context Protocol by Anthropic for connecting AI to tools.",
]


def test_retrieve_returns_string():
    result = retrieve(CHUNKS, "What is YOLO?")
    assert isinstance(result, str), "retrieve() must return a string"


def test_retrieve_finds_correct_chunk():
    result = retrieve(CHUNKS, "What is YOLO detection?")
    assert "YOLO" in result, "Should retrieve the YOLO chunk for a YOLO question"


def test_retrieve_finds_rag_chunk():
    result = retrieve(CHUNKS, "How does RAG reduce hallucinations?")
    assert "RAG" in result, "Should retrieve the RAG chunk"


def test_answer_returns_dict():
    result = answer(CHUNKS, "What is YOLO?")
    assert isinstance(result, dict), "answer() must return a dict"


def test_answer_has_correct_keys():
    result = answer(CHUNKS, "What is YOLO?")
    assert "context" in result, "Dict must have 'context' key"
    assert "answer" in result, "Dict must have 'answer' key"


def test_answer_is_non_empty():
    result = answer(CHUNKS, "What is MCP?")
    assert isinstance(result["answer"], str) and len(result["answer"]) > 0, \
        "'answer' must be a non-empty string"
