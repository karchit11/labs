# Lab 03: TOON Converter 🎨

**Difficulty**: Medium

## Objective
Convert standard JSON data into the **TOON (Text Object Oriented Notation)** format to save token costs.

## Task
Implement `to_toon(data)` and `from_toon(toon_str)` in `solution.py`.

## TOON Logic
- **JSON**: `{"name": "Alice", "age": 25}`
- **TOON**: `[name:Alice|age:25]`

## Instructions
1. **to_toon**: Join key-value pairs with `:`, and items with `|`. Wrap in `[]`.
2. **from_toon**: Split by `|`, then by `:`, and reconstruct the dictionary.

## Example
**Input**: `{"id": 1, "status": "active"}`
**Output**: `[id:1|status:active]`

## Common Mistakes
- Leaving trailing `|` characters inside the brackets.
- Forgetting to convert non-string values (like integers) to strings.
