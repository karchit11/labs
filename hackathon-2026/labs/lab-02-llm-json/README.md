# Lab 02: LLM JSON Output 🤖

**Difficulty**: Easy (Beginner)

## Objective
Ensuring an LLM returns raw JSON that can be parsed by code, not just conversational text.

## Task
Implement `get_model_specs(prompt)` in `solution.py`.

## Instructions
1. **System Prompt**: Tell the model "Return ONLY raw JSON. No markdown backticks."
2. **Schema**: The output must have `{"model_name": str, "parameters": str}`.
3. **Parsing**: Try to parse the model output using `json.loads()`.

## Example
**Input**: "Tell me about GPT-4"
**Expected Output**: `{"model_name": "GPT-4", "parameters": "1.7T"}` (values may vary).

## Common Mistakes
- Not stripping extra text (like "Here is the JSON:") from the model output.
- Forgetting to handle cases where the LLM hallucinates bad JSON syntax.
