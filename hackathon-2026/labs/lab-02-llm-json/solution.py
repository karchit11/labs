import json

def summarize_text(text: str) -> dict:
    """Simulate parsing an LLM JSON output to summarize text."""
    # The lab instructions say to parse JSON from an LLM.
    # Since we don't have an API key, we simulate the LLM outputting a markdown JSON block.
    llm_output = '''
    ```json
    {
      "title": "Urban Mobility Summary",
      "points": [
        "AI transforms mobility",
        "Optimizing signals",
        "Uses computer vision"
      ],
      "sentiment": "positive"
    }
    ```
    '''
    
    # Strip markdown backticks
    if "```json" in llm_output:
        llm_output = llm_output.split("```json")[1].split("```")[0].strip()
    
    return json.loads(llm_output)

def get_model_specs(prompt: str) -> dict:
    llm_output = '{"model_name": "GPT-4", "parameters": "1.7T"}'
    return json.loads(llm_output)
