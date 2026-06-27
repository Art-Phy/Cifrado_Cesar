# PROJECT.md

# Project Context

This document describes the purpose, current status and technical context of this repository.

It is intended to help developers and AI agents understand the project before making changes.

---

# Overview

Short description of what this project does.

Example:

This project is a Python CLI application for generating secure passwords.

---

# Goal

Main purpose of the project.

Example:

The goal of this project is to provide a simple, maintainable and user-friendly tool while following good Python development practices.

---

# Current Status

Current project status:

```text
Planning / Development / Stable / Maintenance
```

Current version:

```text
v0.1.0
```

---

# Tech Stack

Main technologies used in this project:

- Python
- pytest

Add or remove items depending on the project:

- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Docker
- Docker Compose
- Nginx
- systemd

---

# Architecture

Brief explanation of how the project is organized.

Example:

```text
src/
├── package_name/
│   ├── __init__.py
│   ├── cli.py
│   └── core.py
tests/
├── test_core.py
README.md
CHANGELOG.md
pyproject.toml
```

Explain the responsibility of the main modules:

- `cli.py`: Handles command-line arguments and user interaction.
- `core.py`: Contains the main business logic.
- `tests/`: Contains automated tests.

---

# Main Commands

Useful commands for development.

Create virtual environment:

```bash
python3 -m venv .venv
```

Activate virtual environment:

```bash
source .venv/bin/activate
```

Install project in editable mode:

```bash
pip install -e .
```

Run tests:

```bash
pytest
```

Run the application:

```bash
python -m package_name
```

---

# Development Notes

Important decisions, constraints or conventions specific to this project.

Examples:

- This project uses the `src/` layout.
- The CLI layer should stay separated from the core logic.
- New features should include tests whenever practical.
- Documentation must be updated when commands or behaviour change.
- Avoid adding dependencies unless they provide clear value.

---

# Roadmap

## Planned

- Add future task here.

## In Progress

- Add current task here.

## Completed

- Initial project structure.
- Basic documentation.

---

# Known Issues

Known limitations or pending fixes.

- No known issues yet.

---

# Release Notes Context

Use this section to keep track of important changes that may be useful when preparing a release.

Example:

- Added CLI argument support.
- Refactored project to `src/` layout.
- Added pytest test suite.

---

# Notes for Future Agents

Before making changes:

- Read `AGENTS.md`.
- Read this file.
- Check the current project status.
- Prefer small, focused changes.
- Keep the roadmap updated when relevant.