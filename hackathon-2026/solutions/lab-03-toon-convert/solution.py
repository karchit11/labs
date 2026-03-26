def json_to_toon(data: list[dict]) -> str:
    """
    Convert a list of uniform dicts to TOON format.

    Example:
        Input:  [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        Output:
            # fields: id, name
            1 | Alice
            2 | Bob

    Returns:
        A single TOON-format string.
    """
    if not data:
        return ""

    fields = list(data[0].keys())
    header = "# fields: " + ", ".join(fields)

    rows = []
    for record in data:
        row = " | ".join(str(record[f]) for f in fields)
        rows.append(row)

    return "\n".join([header] + rows)


def count_tokens(text: str) -> int:
    """
    A simple proxy for token count: split on whitespace and count words.
    
    Args:
        text: Any string.

    Returns:
        Integer word count.
    """
    if not text:
        return 0
    return len(text.split())
