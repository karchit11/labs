# Lab 04: Vehicle Detection 🚗

**Difficulty**: Medium

## Objective
Use a computer vision model (YOLOv8) to filter and count vehicles in an image metadata list.

## Task
Implement `detect_vehicles(detections)` in `solution.py`.

## Instructions
1. **Classes**: Filter classes to only include `car`, `truck`, `bus`, `motorcycle`.
2. **Confidence**: Only keep detections with `confidence > 0.5`.
3. **Output**: Return a count of the valid vehicles.

## Example
**Input**: `[{"class": "car", "conf": 0.9}, {"class": "person", "conf": 0.8}]`
**Output**: `1`

## Common Mistakes
- Misspelling the vehicle classes.
- Inclusive vs Exclusive confidence thresholds (use `>`).
