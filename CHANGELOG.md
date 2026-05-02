# Changelog

All notable changes to CodeCompass are documented here.

## [1.0.0] - 2026-05-02

### Added
- Full GitHub repository analysis via IBM watsonx.ai Granite model
- 5-dimension code quality scoring (structure, tests, docs, devops, security)
- Animated SVG overall score ring with weighted composite formula
- Natural language Q&A about any repository
- File explorer with view, copy, and download
- IBM Bob design language UI (glass cards, dot-matrix hero, IBM badge)
- Fallback analysis when watsonx.ai is unavailable
- Priority-based key file ranking algorithm (`get_key_files`)
- GitHub rate limit / 404 / 403 error handling with user-facing messages
- Loading progress steps during analysis
- Docker + IBM Cloud Code Engine deployment configuration
- CI/CD pipeline via GitHub Actions
- 38 unit tests across API endpoints and analyzer engine
- IBM Bob session report included for hackathon verification

### Fixed
- `strip_emojis()` malformed regex character ranges
- Silent failure on GitHub API rate limit exceeded
- URL persistence between analyze and ask flows

### Infrastructure
- Dockerfile optimized with non-root user and health check
- manifest.yml for IBM Cloud Foundry
- Procfile for Cloud Foundry process management
- Python 3.13 compatible dependency versions
