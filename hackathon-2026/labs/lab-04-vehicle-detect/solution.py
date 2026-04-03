def count_by_class(detections: list) -> dict:
    """Return a dictionary counting the number of detections per class."""
    counts = {}
    for d in detections:
        c = d.get("class_name")
        counts[c] = counts.get(c, 0) + 1
    return counts

def filter_by_confidence(detections: list, threshold: float) -> list:
    """Return a list of detections with confidence strictly greater than the threshold."""
    return [d for d in detections if d.get("confidence", 0) > threshold]

def get_top_detection(detections: list):
    """Return the detection with the highest confidence, or None if empty."""
    if not detections:
        return None
    return max(detections, key=lambda d: d.get("confidence", 0))
