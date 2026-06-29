## Cifrado César

<p align="left">
  <img src="https://img.shields.io/badge/python-3.12+-blue.svg" />
  <img src="https://img.shields.io/badge/CLI-Text%20Encryption-orange" />
  <img src="https://img.shields.io/badge/Testing-pytest-green" />
  <img src="https://img.shields.io/badge/Status-v2.0.0%20Stable-success" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

Herramienta **CLI desarrollada en Python** para cifrar y descifrar texto utilizando el clásico **cifrado César**.

El proyecto ha sido completamente refactorizado siguiendo una arquitectura moderna basada en `src/`, incorporando una interfaz de línea de comandos mediante `argparse`, un modo interactivo, tests automatizados y empaquetado con `pyproject.toml`.

Ideal como proyecto educativo para comprender tanto el algoritmo César como una estructura profesional de proyectos Python.

---

### Funcionalidades

#### Core

- Cifrado de texto mediante el algoritmo César.
- Descifrado de texto utilizando un desplazamiento determinado.
- Generación automática de una clave aleatoria cuando no se especifica.
- Conservación de mayúsculas, minúsculas y caracteres no alfabéticos.
- Modo interactivo y modo no interactivo mediante `argparse`.

#### Proyecto

- Arquitectura moderna basada en `src/`.
- Separación entre lógica de negocio e interfaz CLI.
- Empaquetado mediante `pyproject.toml`.
- Comando instalable `cifrado-cesar`.
- Tests automatizados con `pytest`.

---

### Requisitos

- Python 3.12 o superior.

---

### Instalación

#### Clonar el repositorio

```bash
git clone https://github.com/ArtPphy/Cifrado_Cesar.git
cd Cifrado_Cesar
```

#### Crear un entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Instalar el proyecto

```bash
pip install -e .
```

---

### Uso

#### Modo interactivo

```bash
cifrado-cesar
```

Ejecuta la aplicación sin argumentos para acceder al menú interactivo.

#### Modo línea de comandos

##### Cifrar texto

```bash
cifrado-cesar encrypt "Hola Mundo" --shift 3
```

##### Cifrar utilizando una clave aleatoria

```bash
cifrado-cesar encrypt "Hola Mundo"
```

##### Descifrar texto

```bash
cifrado-cesar decrypt "Krod Pxqgr" --shift 3
```

#### Ayuda

```bash
cifrado-cesar --help
```

---

### Estructura del proyecto

```text
src/
└── cifrado_cesar/
    ├── __init__.py
    ├── __main__.py
    ├── cli.py
    └── core.py

tests/
└── test_core.py

README.md
CHANGELOG.md
pyproject.toml
LICENSE
```

| Archivo / Directorio | Descripción |
|----------------------|-------------|
| `core.py` | Implementa la lógica del cifrado y descifrado. |
| `cli.py` | Gestiona la interfaz interactiva y los argumentos de línea de comandos. |
| `tests/` | Contiene la suite de pruebas automatizadas. |

---

### Ejecutar los tests

```bash
pytest
```

---

### Tecnologías

- Python
- argparse
- pytest
- hatchling

---

### Roadmap

Mejoras previstas para futuras versiones:

- [ ] Soporte para cifrado y descifrado de archivos.
- [ ] Posibilidad de utilizar alfabetos personalizados.
- [ ] Mejoras adicionales en la experiencia del modo interactivo.

---

### Licencia

Este proyecto está licenciado bajo la licencia MIT.