## Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

### [2.0.0] - 2026-06-26

#### Added

- `src/` layout with clean separation between core logic and CLI.
- `pyproject.toml` replacing `requirements.txt`.
- CLI via `argparse` with `encrypt` and `decrypt` subcommands.
- Interactive menu mode when no arguments are provided.
- Automated test suite with `pytest`.
- Console entry point `cifrado-cesar`.

#### Changed

- Moved core logic (`cifrar_cesar`, `descifrar_cesar`) to `src/cifrado_cesar/core.py`.
- Moved CLI logic to `src/cifrado_cesar/cli.py`.
- Rewrote README in Spanish with installation and usage examples.
- Rewrote CHANGELOG in English following Keep a Changelog format.

#### Removed

- Removed `maincc.py` (replaced by `src/cifrado_cesar/` package).
- Removed `requirements.txt` (replaced by `pyproject.toml`).

---

### [1.0.0] - 2025-10-26

#### Added

- Core Caesar cipher functionality: encrypt and decrypt text.
- Automatic random key generation for encryption.
- Support for uppercase and lowercase letters; non-alphabetic characters remain unchanged.
- Modular structure with separate functions (`cifrar_cesar`, `descifrar_cesar`, `mostrar_menu`).
- Detailed comments and docstrings to ease maintenance.
- `requirements.txt` (no external dependencies).

#### Changed

- Reorganized all code into `maincc.py` for better readability and scalability.
- Input validation for user entries (numeric key and menu options).
- Added `if __name__ == "__main__":` guard for future integration (CLI or GUI).

#### In progress

- GUI interface with `tkinter` or `customtkinter`.
- Support for custom encryption (manual key and file mode).
- Add an "exit" option to the terminal menu.
- Prevent automatic exit after encryption or decryption.
