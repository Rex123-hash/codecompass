from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
import os
from analyzer import get_repo_tree, build_context, parse_github_url
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="CodeCompass API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

WATSONX_API_KEY = os.getenv("WATSONX_API_KEY", "")
WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID", "")
WATSONX_URL = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"

class RepoRequest(BaseModel):
    github_url: str

class QuestionRequest(BaseModel):
    github_url: str
    question: str

async def get_iam_token():
    """Exchange IBM API key for IAM access token."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://iam.cloud.ibm.com/identity/token",
            data={
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                "apikey": WATSONX_API_KEY
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        return response.json().get("access_token", "")

async def ask_watsonx(prompt: str) -> str:
    """Send prompt to watsonx.ai and return response."""
    token = await get_iam_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "model_id": "ibm/granite-13b-chat-v2",
        "input": prompt,
        "parameters": {
            "max_new_tokens": 800,
            "temperature": 0.3
        },
        "project_id": WATSONX_PROJECT_ID
    }
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(WATSONX_URL, json=payload, headers=headers)
        result = response.json()
        return result.get("results", [{}])[0].get("generated_text", "No response generated.")

@app.post("/analyze")
async def analyze_repo(request: RepoRequest):
    """Analyze a GitHub repository and return architecture summary."""
    owner, repo = parse_github_url(request.github_url)
    if not owner:
        return {"error": "Invalid GitHub URL"}
    
    file_list = get_repo_tree(owner, repo)
    if not file_list:
        return {"error": "Could not fetch repository. Check URL or token."}
    
    context = build_context(owner, repo, file_list)
    
    prompt = f"""You are CodeCompass, an expert software architect.
Analyze this repository and provide:
1. ARCHITECTURE SUMMARY: What this project does in 2-3 sentences
2. KEY COMPONENTS: List the 5 most important files/modules and their purpose
3. TECH STACK: Languages, frameworks, and tools used
4. ONBOARDING GUIDE: Top 3 things a new developer should understand first
5. COMPLEXITY SCORE: Rate 1-10 and explain why

{context}

Provide a clear, structured analysis:"""

    summary = await ask_watsonx(prompt)
    
    return {
        "owner": owner,
        "repo": repo,
        "total_files": len(file_list),
        "file_tree": file_list[:30],
        "summary": summary
    }

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """Answer a specific question about the repository."""
    owner, repo = parse_github_url(request.github_url)
    if not owner:
        return {"error": "Invalid GitHub URL"}
    
    file_list = get_repo_tree(owner, repo)
    context = build_context(owner, repo, file_list)
    
    prompt = f"""You are CodeCompass, an expert software architect.
Based on this repository, answer the following question clearly and concisely.

{context}

Question: {request.question}

Answer:"""

    answer = await ask_watsonx(prompt)
    return {"answer": answer}

@app.get("/health")
def health():
    return {"status": "CodeCompass is running"}