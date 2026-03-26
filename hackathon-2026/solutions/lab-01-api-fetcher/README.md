# Lab 01: API Fetcher 🌐

**Difficulty**: Easy (Beginner)

## Objective
Learn how to interact with real-world REST APIs and parse JSON data using Python.

## Task
Implement the following functions in `solution.py`:
- `fetch_issues(owner, repo)`: Fetch open issues from a GitHub repository.
- `filter_open(issues)`: Filter a list of issues to keep only "open" ones.

## Function Signatures
```python
def fetch_issues(owner: str, repo: str) -> list:
    pass

def filter_open(issues: list) -> list:
    pass
```

## Step-by-Step
1. **Import `requests`**: Use the requests library to make HTTP calls.
2. **Format URL**: The API endpoint is `https://api.github.com/repos/{owner}/{repo}/issues`.
3. **Handle Response**: Check `response.status_code == 200` before parsing JSON.
4. **Filter**: Use a list comprehension to filter the list based on the `state` key.

## Example
**Input**: `owner="psf", repo="requests"`
**Expected Output**: A list of dictionaries representing open issues.

## Common Mistakes
- Not handling network timeouts.
- Hardcoding the `state=open` parameter in the URL and the filter (double check!).
- Forgetting to return a list (empty list if no issues found).
