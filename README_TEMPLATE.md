<!--
===============================================================================
README TEMPLATE
Version: 1.1.0

Purpose:
Defines the standard structure and writing style for README.md files.

Last Updated:
2026-06-27

===============================================================================

Generation Rules

When generating this document:

- Preserve the structure defined by this template.
- Remove sections that are not applicable.
- Do not invent project features.
- Do not invent roadmap items.
- Do not invent repository URLs.
- Do not invent package publication status.
- Use placeholders whenever information is unknown.
- Only document implemented functionality.
- Commands shown in this README must match the actual project.
- Examples should be executable whenever possible.

Writing Style

- Keep descriptions concise.
- Avoid marketing language.
- Do not exaggerate project capabilities.
- Prefer practical examples.
- Keep sections focused.
- Use Spanish for all documentation.
- Keep a professional and consistent tone.

Badges

Always include badges when applicable.

Preferred order:

1. Python Version
2. Project Type
3. Testing
4. Status
5. License

Only include badges that accurately represent the current project.

===============================================================================

Template History

v1.1.0
- Added generation rules.
- Added writing style guidelines.
- Added badge guidelines.
- Added template metadata.

v1.0.0
- Initial README template.

===============================================================================
-->

# Project Name

<p align="left">
  <!-- Project badges -->
</p>

Short description of the project.

Explain:

- What it does.
- Who it is intended for.
- Why it exists.

---

## Features

### Core

- Feature
- Feature
- Feature

### Additional

- Feature
- Feature

---

## Requirements

- Python x.x+
- Additional requirements if applicable.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<username>/<repository>.git
cd <repository>
```

### Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install the project

```bash
pip install -e .
```

Or:

```bash
pip install .
```

---

## Usage

### Interactive mode

```bash
project-name
```

### Command-line mode

```bash
project-name --help
```

Add additional examples when appropriate.

---

## Project Structure

```text
src/
tests/
README.md
CHANGELOG.md
pyproject.toml
```

Briefly describe the purpose of the most important files and directories.

---

## Running Tests

```bash
pytest
```

---

## Technologies

Only include technologies actually used by the project.

Example:

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- pytest

---

## Roadmap

Only include roadmap items explicitly defined for this project.

Example:

- [ ] Feature
- [ ] Feature

---

## Contributing

Contributions, suggestions and improvements are welcome.

---

## License

This project is licensed under the MIT License.