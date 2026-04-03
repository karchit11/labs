def json_to_toon(data: list) -> str:
    """Convert a list of dictionaries into a TOON-like pipe-separated format."""
    if not data:
        return ""
    
    keys = list(data[0].keys())
    header = "# fields: " + "|".join(keys)
    
    rows = [header]
    for item in data:
        row = "|".join(str(item.get(k, "")) for k in keys)
        rows.append(row)
        
    return "\n".join(rows)

def count_tokens(text: str) -> int:
    """Count tokens (words) in a text."""
    if not text:
        return 0
    return len(text.split())

def to_toon(data: dict) -> str:
    """As described in README"""
    pairs = [f"{k}:{v}" for k, v in data.items()]
    return "[" + "|".join(pairs) + "]"

def from_toon(toon_str: str) -> dict:
    """As described in README"""
    toon_str = toon_str.strip("[]")
    result = {}
    for pair in toon_str.split("|"):
        if ":" in pair:
            k, v = pair.split(":", 1)
            # Try to infer type
            if v.isdigit():
                v = int(v)
            result[k] = v
    return result
