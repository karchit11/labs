import requests


def fetch_issues(owner: str, repo: str) -> list:
    """Fetch open issues from a GitHub repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []


def filter_open(issues: list) -> list:
    """Filter a list of issues to only include those where state is 'open'."""
    return [issue for issue in issues if issue.get("state") == "open"]
