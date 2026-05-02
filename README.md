# CodeCompass 🧭
**AI-Powered Repository Intelligence & Developer Onboarding**

> Built for the **IBM Bob Dev Day Hackathon** · Powered by **IBM watsonx.ai** · Model: `ibm/granite-3-8b-instruct`

---

## The Problem

Developers lose hours — sometimes days — trying to understand an unfamiliar codebase before they can contribute. Reading through hundreds of files, deciphering architecture decisions, and figuring out how to even run the project slows everyone down.

**CodeCompass solves this with one GitHub URL.**

---

## System Architecture

```mermaid
graph TB
    subgraph Frontend["🖥️ Frontend (index.html)"]
        UI[IBM Bob Design UI]
        FileExplorer[File Explorer]
        ScoreRing[Animated Score Ring]
        FAQ[FAQ Section]
    end

    subgraph Backend["⚙️ Backend (FastAPI - main.py)"]
        API_Analyze[POST /analyze]
        API_Ask[POST /ask]
        API_File[GET /file]
        API_Health[GET /health]
        IAM[IBM IAM Token Exchange]
        Fallback[Local Fallback Analysis]
    end

    subgraph Analyzer["🔍 Analyzer Engine (analyzer.py)"]
        RepoTree[get_repo_tree]
        FileContent[get_file_content]
        Metadata[get_repo_metadata]
        KeyFiles[get_key_files Priority Scorer]
        BuildCtx[build_context]
        SmartAudit[smart_audit 5-Dimension Scorer]
    end

    subgraph IBM["☁️ IBM Cloud"]
        Granite[ibm/granite-3-8b-instruct]
        WatsonX[watsonx.ai Endpoint]
        IAMService[IBM IAM Service]
    end

    subgraph GitHub["🐙 GitHub REST API"]
        Trees["GET /repos/:owner/:repo/git/trees"]
        Contents["GET /repos/:owner/:repo/contents"]
        RepoMeta["GET /repos/:owner/:repo"]
    end

    UI -->|GitHub URL| API_Analyze
    UI -->|Question| API_Ask
    FileExplorer -->|path| API_File

    API_Analyze --> RepoTree
    API_Analyze --> BuildCtx
    API_Analyze --> SmartAudit
    API_Ask --> BuildCtx

    RepoTree --> Trees
    FileContent --> Contents
    Metadata --> RepoMeta

    BuildCtx --> KeyFiles
    BuildCtx --> FileContent
    BuildCtx --> Metadata

    API_Analyze --> IAM
    API_Ask --> IAM
    IAM --> IAMService
    IAM -->|Bearer token| WatsonX
    WatsonX --> Granite

    Granite -->|Generated analysis| API_Analyze
    Granite -->|Answer| API_Ask
    IAM -->|token fail| Fallback
    Fallback -->|local result| API_Analyze

    API_Analyze -->|scores + summary + files| UI
    API_Ask -->|answer| UI
    API_File -->|file content| FileExplorer
```

---

## Request Flow — Repository Analysis

```mermaid
sequenceDiagram
    actor User
    participant UI as Frontend (index.html)
    participant API as FastAPI (main.py)
    participant GH as GitHub API
    participant Analyzer as analyzer.py
    participant IAM as IBM IAM
    participant WX as watsonx.ai Granite

    User->>UI: Paste GitHub URL + click Analyze
    UI->>UI: Show progress steps (Fetching... Reading... Building...)
    UI->>API: POST /analyze { github_url }

    API->>Analyzer: parse_github_url()
    API->>GH: GET /repos/:owner/:repo/git/trees?recursive=1
    GH-->>API: Full file tree (all paths)

    API->>Analyzer: analyze_file_structure(file_list)
    API->>Analyzer: get_key_files(file_list) — priority scoring
    API->>GH: GET /contents/:path (up to 15 key files)
    GH-->>API: File contents

    API->>Analyzer: build_context() — assembles prompt context
    API->>Analyzer: smart_audit() — 5-dimension scoring

    API->>IAM: POST /identity/token { apikey }
    IAM-->>API: Bearer access_token

    API->>WX: POST /ml/v1/text/generation { model, prompt, params }
    WX-->>API: Generated analysis text

    API-->>UI: { summary, scores, quick_wins, file_tree }
    UI->>UI: Render scores, ring animation, markdown summary
    UI-->>User: Full analysis displayed
```

---

## Code Structure

```mermaid
graph LR
    subgraph main.py["main.py — API Layer"]
        direction TB
        M1[get_iam_token]
        M2[ask_watsonx]
        M3[generate_local_analysis]
        M4[strip_emojis]
        M5[POST /analyze]
        M6[POST /ask]
        M7[GET /file]
        M8[GET /health]
        M9[GET /]
        M5 --> M1
        M5 --> M2
        M2 --> M1
        M2 --> M3
        M6 --> M2
    end

    subgraph analyzer.py["analyzer.py — Intelligence Engine"]
        direction TB
        A1[get_repo_tree]
        A2[get_repo_metadata]
        A3[get_file_content]
        A4[analyze_file_structure]
        A5[extract_dependencies]
        A6[get_key_files]
        A7[build_context]
        A8[parse_github_url]
        A9[smart_audit]
        A7 --> A2
        A7 --> A4
        A7 --> A5
        A7 --> A6
        A7 --> A3
        A9 --> A4
    end

    subgraph index.html["index.html — Frontend"]
        direction TB
        F1[handleAnalyze]
        F2[handleAsk]
        F3[displayResults]
        F4[renderFileTree]
        F5[viewFile]
        F6[setScore + ring animation]
        F7[renderMarkdown]
        F8[filterFiles]
        F1 --> F3
        F3 --> F4
        F3 --> F6
        F3 --> F7
        F2 --> F7
        F4 --> F8
        F5 --> F7
    end

    M5 --> A1
    M5 --> A7
    M5 --> A9
    M6 --> A7
    M7 --> A3
```

---

## Scoring System

```mermaid
graph TD
    Repo[GitHub Repository] --> S1
    Repo --> S2
    Repo --> S3
    Repo --> S4
    Repo --> S5

    S1["📁 Structure Score /10
    +10 base
    -2 missing tests
    -2 missing README
    -2 missing CI/CD
    -2 missing Docker
    -2 missing LICENSE"]

    S2["🧪 Test Score /10
    test files / total files × 10
    capped at 10"]

    S3["📄 Docs Score /10
    +4 README.md
    +3 /docs folder
    +2 CHANGELOG
    +1 CONTRIBUTING"]

    S4["🚀 DevOps Score /10
    +2.5 Dockerfile
    +2.5 CI/CD pipeline
    +2.5 .env.example
    +2.5 Makefile"]

    S5["🔒 Security Score /10
    -3.0 committed .env
    -2.5 missing .gitignore
    -2.0 secret files found
    -1.0 no SECURITY.md
    +0.5 bonuses"]

    S1 -->|"× 0.30"| CALC
    S2 -->|"× 0.25"| CALC
    S3 -->|"× 0.20"| CALC
    S4 -->|"× 0.15"| CALC
    S5 -->|"× 0.10"| CALC

    CALC["⚡ Weighted Formula
    structure×0.30 + tests×0.25
    + docs×0.20 + devops×0.15
    + security×0.10"] --> SCORE

    SCORE["🎯 Overall Score /10
    Displayed as animated SVG ring"]
```

---

## IBM Bob Integration Flow

```mermaid
flowchart LR
    subgraph Bob["IBM Bob - Development Partner"]
        B1[Bob reads codebase context]
        B2[Bob explains architecture]
        B3[Bob generates tests]
        B4[Bob reviews security]
        B5[Bob writes deployment config]
    end

    subgraph Built["What Bob Built"]
        C1[watsonx.ai API integration]
        C2[5-dimension scoring engine]
        C3[Priority file ranking algorithm]
        C4[Fallback analysis system]
        C5[IBM Cloud deployment setup]
        C6[38 unit tests]
    end

    B1 --> C1
    B2 --> C2
    B2 --> C3
    B3 --> C6
    B4 --> C4
    B5 --> C5
```

---

## What It Does

Paste any public GitHub repository URL and CodeCompass, powered by IBM watsonx.ai (Bob), instantly delivers:

| Feature | Description |
|---|---|
| **Architecture Analysis** | Identifies the pattern (MVC, microservices, monolithic) and explains how components interact |
| **Technology Stack Breakdown** | Languages, frameworks, dependencies, DevOps tooling |
| **Developer Onboarding Roadmap** | Step-by-step guide: first 30 minutes → first day → first week |
| **Code Quality Scoring** | 5-dimensional score across structure, tests, docs, DevOps, and security |
| **Overall Rating** | Weighted composite score with animated SVG ring |
| **Ask Anything** | Natural language Q&A about any aspect of the repository |
| **File Explorer** | Browse, view, copy, and download any file in the repo |

---

## How IBM Bob Powers It

CodeCompass is built entirely on the **IBM watsonx.ai stack**:

- **Model**: `ibm/granite-3-8b-instruct` — IBM's enterprise-grade code-fluent model
- **Platform**: IBM Cloud · watsonx.ai inference endpoint (`us-south.ml.cloud.ibm.com`)
- **Auth**: IBM IAM token exchange (`iam.cloud.ibm.com/identity/token`)
- **Deployment**: IBM Cloud Code Engine · Docker

The entire AI reasoning pipeline — architecture detection, quality scoring, onboarding generation, and Q&A — runs through IBM Granite. No other AI provider is used.

---

## Hackathon Theme Alignment

**"Turn idea into impact faster"**

CodeCompass directly addresses the challenge:

- ✅ **Get up to speed on existing code quickly** — full repo analysis in one click
- ✅ **Generate documentation** — produces architecture docs, component maps, onboarding guides on demand
- ✅ **Reduce repetitive effort** — no more manual code archaeology before every new project
- ✅ **Any skill level** — junior devs get the same insight as senior architects

---

## Quality Scoring System

| Dimension | Weight | What It Checks |
|---|---|---|
| Structure | 30% | File organization, separation of concerns, key files present |
| Tests | 25% | Test files ratio, coverage setup, test frameworks |
| Documentation | 20% | README, /docs folder, CHANGELOG, CONTRIBUTING |
| DevOps | 15% | Docker, CI/CD pipeline, .env.example, Makefile |
| Security | 10% | .env handling, secrets management, SECURITY.md |

**Overall Score** = `structure×0.30 + tests×0.25 + docs×0.20 + devops×0.15 + security×0.10`

---

## Tech Stack

| Layer | Technology |
|---|---|
| AI / LLM | IBM watsonx.ai · `ibm/granite-3-8b-instruct` |
| Backend | Python 3.11 · FastAPI · uvicorn |
| Frontend | Vanilla HTML/CSS/JS · IBM Bob design language |
| Deployment | IBM Cloud Code Engine · Docker |
| Source Data | GitHub REST API v3 |
| Testing | pytest · pytest-asyncio · pytest-cov |

---

## Project Structure

```
codecompass/
├── main.py              # FastAPI app — watsonx.ai integration, all API routes
├── analyzer.py          # GitHub API client, repo tree builder, smart audit engine
├── index.html           # Full frontend — IBM Bob design language, single-page app
├── test_main.py         # API endpoint tests (18 tests)
├── test_analyzer.py     # Analyzer unit tests (20 tests)
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── Dockerfile           # Container setup for IBM Cloud Code Engine
├── manifest.yml         # IBM Cloud Foundry deployment config
├── Procfile             # Process definition for Cloud Foundry
├── runtime.txt          # Python version specification
├── pytest.ini           # Test configuration
├── bob-report/          # IBM Bob session export (proof of Bob usage)
│   └── bob-session-report.md
└── IBM_CLOUD_DEPLOYMENT.md  # Step-by-step IBM Cloud deployment guide
```

---

## Running Locally

### Prerequisites
- Python 3.11+
- IBM watsonx.ai API Key + Project ID ([get one here](https://cloud.ibm.com))
- GitHub Personal Access Token (optional — increases rate limit from 60 → 5,000 req/hr)

### Setup

```bash
git clone https://github.com/Rex123-hash/codecompass.git
cd codecompass

pip install -r requirements.txt

# Copy env template and fill in your values
cp .env.example .env
# Edit .env with your WATSONX_API_KEY, WATSONX_PROJECT_ID, GITHUB_TOKEN

uvicorn main:app --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000`

### Running Tests

```bash
pytest --tb=short -v
```

---

## Deploying to IBM Cloud

See [`IBM_CLOUD_DEPLOYMENT.md`](./IBM_CLOUD_DEPLOYMENT.md) for full instructions.

**Docker / Code Engine:**
```bash
docker build -t codecompass .
docker run -p 8000:8000 --env-file .env codecompass
```

---

## Team

Built for the **IBM Bob Dev Day Hackathon**
Powered by **IBM watsonx.ai (Bob)** · `ibm/granite-3-8b-instruct`
IBM Bob Dev Day · 2026
