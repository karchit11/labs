def is_anomaly(vitals: dict) -> bool:
    """Return True if any vital is outside the normal range."""
    hr = vitals.get("heart_rate", 80)
    sys = vitals.get("blood_pressure_sys", 120)
    dia = vitals.get("blood_pressure_dia", 80)
    ox = vitals.get("oxygen_saturation", 98)
    
    if not (60 <= hr <= 100):
        return True
    if not (90 <= sys <= 140):
        return True
    if not (60 <= dia <= 90):
        return True
    if ox < 95:
        return True
        
    return False

def recommend_intervention(vitals: dict) -> str:
    """Recommend action based on anomalies."""
    if is_anomaly(vitals):
        return "Immediate Physician Review"
    return "Continue Observation"
