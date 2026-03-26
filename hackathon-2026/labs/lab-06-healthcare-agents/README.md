# Lab 06: Healthcare Agents 🏥

**Difficulty**: Medium (Intermediate)

## Objective
Build a simple agentic logic for monitoring patient vitals and flagging anomalies that require immediate physician intervention.

## Task
Implement the following in `solution.py`:
- `is_anomaly(vitals)`: A function that checks heart rate and blood pressure against safe thresholds.
- `recommend_intervention(vitals, history)`: An LLM-inspired (mocked) function that suggests an action based on the vitals.

## Data Structure
Vitals are provided as a dictionary:
```python
{
    "heart_rate": 85,
    "blood_pressure_sys": 120,
    "blood_pressure_dia": 80,
    "oxygen_saturation": 98
}
```

## Thresholds (for this lab)
- **Heart Rate**: Normal (60-100), Anomaly (<60 or >100)
- **BP Systolic**: Normal (90-140), Anomaly (<90 or >140)
- **BP Diastolic**: Normal (60-90), Anomaly (<60 or >90)
- **Oxygen**: Normal (>=95), Anomaly (<95)

## Step-by-Step
1. **Anomaly Check**: Logic to return `True` if *any* vital is outside the normal range.
2. **Recommendation**: If it's an anomaly, suggest "Immediate Physician Review". If normal, suggest "Continue Observation".
