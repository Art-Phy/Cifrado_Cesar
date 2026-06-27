# AGENTS.md

# Development Guidelines

This document defines the conventions and development philosophy for this repository.

Always follow these guidelines unless explicitly instructed otherwise.

---

# Core Principles

- Prioritize readability over clever solutions.
- Keep the code simple, explicit and maintainable.
- Avoid unnecessary abstractions.
- Prefer incremental improvements over large rewrites.
- When in doubt, choose the solution that is easier to understand.
- Long-term maintainability is more important than short-term cleverness.

---

# Project Structure

Unless the project requires otherwise:

- Use the `src/` layout.
- Keep modules focused on a single responsibility.
- Separate business logic from CLI/API layers.
- Avoid large files whenever possible.

Typical layout:

```text
src/
tests/
README.md
CHANGELOG.md
LICENSE
.gitignore
```

---

# Python Style

- Python 3.12+ or the latest stable supported version.
- Follow PEP8.
- Use type hints whenever practical.
- Prefer f-strings.
- Prefer `pathlib` over `os.path` when possible.
- Avoid global variables.
- Raise meaningful exceptions.
- Keep functions reasonably small.

---

# Documentation

Documentation is considered part of the project.

README:

- Written in Spanish.

CHANGELOG:

- Written in English.
- Follow Keep a Changelog.

Release Notes:

- Written in Spanish.

Code comments:

- Written in English.

Docstrings:

- Written in English.

---

# Git Workflow

Use GitFlow.

Typical branches:

```text
feature/*
bugfix/*
hotfix/*
release/*
```

Never work directly on `main`.

Commits must be written in English.

---

# Testing

Testing is mandatory for new functionality whenever practical.

Preferred framework:

```bash
pytest
```

Before considering a task finished:

- Run the test suite.
- Verify CLI behaviour manually if applicable.
- Make sure existing functionality still works.

---

# Dependencies

Keep dependencies to a minimum.

Before adding a new dependency, consider whether the functionality can reasonably be implemented using the standard library.

Do not add dependencies only for convenience if the problem is simple enough to solve without them.

---

# CLI Applications

For CLI projects:

- Use `argparse`.
- Provide helpful `--help` output.
- Return meaningful exit codes.
- Produce clear and user-friendly messages.
- Validate user input whenever necessary.

---

# APIs

For FastAPI projects:

- Use Pydantic models.
- Separate routers, services and models.
- Prefer dependency injection.
- Return appropriate HTTP status codes.
- Validate inputs properly.
- Keep API responses predictable and consistent.

---

# Database

Prefer:

- SQLAlchemy.
- Alembic.
- Versioned migrations.

Never recreate production schemas automatically.

Avoid using `create_all()` as a replacement for proper migrations in real projects.

---

# Docker

When Docker is used:

- Prefer Docker Compose.
- Use named volumes.
- Add healthchecks whenever possible.
- Keep images lightweight.
- Document how to build, start and stop the services.

---

# Documentation Quality

When modifying documentation:

- Keep examples updated.
- Keep version numbers consistent.
- Update `CHANGELOG.md` when needed.
- Update `README.md` if features, commands or setup steps change.
- Prefer clear explanations over overly technical wording.

---

# Agent Behaviour

When making suggestions:

- Explain the reasoning first.
- Then provide the implementation.
- Respect the existing coding style.
- Preserve backwards compatibility whenever possible.
- Avoid introducing new features unless explicitly requested.

When editing code:

- Avoid unnecessary rewrites.
- If only one function needs changing, modify only that function.
- Do not rewrite entire files when only small changes are required.
- Keep changes focused and easy to review.

If multiple solutions exist:

- Present the simplest solution first.
- Explain trade-offs briefly.

If an improvement could be beneficial but was not requested:

- Propose it first.
- Wait for confirmation before implementing it.

Never introduce unnecessary complexity.

---

# Philosophy

This repository is intended both as production-quality software and as a learning resource.

Good code should be:

- Easy to read.
- Easy to maintain.
- Easy to test.
- Easy to extend.

Finished code should feel production-ready whenever reasonably possible.

The project should grow only when there is a real need for it.