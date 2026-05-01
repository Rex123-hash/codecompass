import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

def get_repo_tree(owner: str, repo: str) -> list:
    """Fetch the full file tree of a GitHub repository."""
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/HEAD?recursive=1"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []
    tree = response.json().get("tree", [])
    return [item["path"] for item in tree if item["type"] == "blob"]

def get_file_content(owner: str, repo: str, path: str) -> str:
    """Fetch content of a specific file from GitHub."""
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return ""
    import base64
    content = response.json().get("content", "")
    try:
        return base64.b64decode(content).decode("utf-8", errors="ignore")
    except:
        return ""

def get_key_files(file_list: list) -> list:
    """Pick the most important files to analyze."""
    priority = ["README", "main", "app", "index", "server", "config", "requirements", "package.json", "Dockerfile"]
    key = []
    for p in priority:
        for f in file_list:
            if p.lower() in f.lower() and f not in key:
                key.append(f)
    extras = [f for f in file_list if f not in key and f.endswith(".py")][:5]
    return (key + extras)[:10]

def build_context(owner: str, repo: str, file_list: list) -> str:
    """Build a context string from key files for LLM analysis."""
    key_files = get_key_files(file_list)
    context = f"Repository: {owner}/{repo}\n\nFiles in repo:\n"
    context += "\n".join(file_list[:50])
    context += "\n\n--- KEY FILE CONTENTS ---\n"
    for f in key_files:
        content = get_file_content(owner, repo, f)
        if content:
            context += f"\n\n### {f}\n{content[:1500]}"
    return context

def parse_github_url(url: str) -> tuple:
    """Extract owner and repo from a GitHub URL."""
    url = url.rstrip("/").replace("https://github.com/", "")
    parts = url.split("/")
    if len(parts) >= 2:
        return parts[0], parts[1]
    return None, None