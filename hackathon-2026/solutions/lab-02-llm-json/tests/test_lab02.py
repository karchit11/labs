"""Tests for Lab 02: LLM JSON Output"""
import pytest
from solution import summarize_text

SAMPLE = "AI is transforming urban mobility by optimizing traffic signals using computer vision."


def test_returns_dict():
    result = summarize_text(SAMPLE)
    assert isinstance(result, dict), "Must return a dict"


def test_has_title_key():
    result = summarize_text(SAMPLE)
    assert "title" in result, "Dict must contain 'title'"
    assert isinstance(result["title"], str), "'title' must be a string"


def test_has_points_key():
    result = summarize_text(SAMPLE)
    assert "points" in result, "Dict must contain 'points'"
    assert isinstance(result["points"], list), "'points' must be a list"
    assert len(result["points"]) == 3, "'points' must have exactly 3 items"


def test_has_sentiment_key():
    result = summarize_text(SAMPLE)
    assert "sentiment" in result, "Dict must contain 'sentiment'"
    assert result["sentiment"] in {"positive", "neutral", "negative"}, \
        "'sentiment' must be 'positive', 'neutral', or 'negative'"
