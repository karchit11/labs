"""Tests for Lab 04: Vehicle Detection"""
import pytest
from solution import count_by_class, filter_by_confidence, get_top_detection

DETECTIONS = [
    {"class_name": "car",   "confidence": 0.95, "bbox": [10, 10, 100, 60]},
    {"class_name": "truck", "confidence": 0.83, "bbox": [20, 20, 200, 80]},
    {"class_name": "car",   "confidence": 0.70, "bbox": [50, 30, 150, 90]},
    {"class_name": "car",   "confidence": 0.60, "bbox": [90, 10, 180, 70]},
]


def test_count_by_class_returns_dict():
    result = count_by_class(DETECTIONS)
    assert isinstance(result, dict), "Must return a dict"


def test_count_by_class_accuracy():
    result = count_by_class(DETECTIONS)
    assert result.get("car") == 3, "Should count 3 cars"
    assert result.get("truck") == 1, "Should count 1 truck"


def test_filter_by_confidence_returns_list():
    result = filter_by_confidence(DETECTIONS, 0.80)
    assert isinstance(result, list), "Must return a list"


def test_filter_by_confidence_accuracy():
    result = filter_by_confidence(DETECTIONS, 0.80)
    assert all(d["confidence"] > 0.80 for d in result), "All results must exceed threshold"
    assert len(result) == 2, "Should return 2 detections above 0.80"


def test_get_top_detection():
    top = get_top_detection(DETECTIONS)
    assert top is not None, "Should not return None for a non-empty list"
    assert top["confidence"] == 0.95, "Should return the highest confidence detection"


def test_get_top_detection_empty():
    result = get_top_detection([])
    assert result is None, "Should return None for empty list"
