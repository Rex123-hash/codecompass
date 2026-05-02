# Contributing to CodeCompass

Thank you for your interest in contributing to CodeCompass!

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/codecompass.git`
3. Copy the env template: `cp .env.example .env`
4. Fill in your `WATSONX_API_KEY` and `WATSONX_PROJECT_ID`
5. Install dependencies: `pip install -r requirements.txt`
6. Run the app: `uvicorn main:app --reload --port 8000`

## Running Tests

```bash
pytest --tb=short -v
```

## Project Structure

| File | Purpose |
|---|---|
| `main.py` | FastAPI routes + watsonx.ai integration |
| `analyzer.py` | GitHub API client + scoring engine |
| `index.html` | Full frontend (IBM Bob design language) |
| `test_main.py` | API endpoint tests |
| `test_analyzer.py` | Analyzer unit tests |

## Guidelines

- Keep IBM watsonx.ai (Granite) as the sole AI provider
- All new features should include tests in `test_*.py`
- Follow the existing IBM Bob design language in `index.html`
- Do not commit `.env` files or API keys

## Powered By

IBM watsonx.ai · `ibm/granite-3-8b-instruct` · IBM Bob Dev Day Hackathon
