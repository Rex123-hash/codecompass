# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| 1.0.x | ✅ Yes |

## Reporting a Vulnerability

If you discover a security vulnerability in CodeCompass, please **do not** open a public GitHub issue.

Instead, email the team directly with details of the vulnerability. We will respond within 48 hours and work to patch it promptly.

## Security Practices

- API keys and secrets are loaded from environment variables only (never hardcoded)
- `.env` files are gitignored — use `.env.example` as a template
- Docker container runs as a non-root user (`appuser`)
- GitHub tokens are optional — the app works without them at reduced rate limits
- WATSONX credentials are never logged or exposed in responses

## IBM Cloud Security

This project uses IBM Cloud IAM for authentication with watsonx.ai. Tokens are exchanged per-request and never stored. See [IBM Cloud Security](https://cloud.ibm.com/docs/security) for platform-level security documentation.
