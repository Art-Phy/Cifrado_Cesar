## Cifrado César

<p align="left">
  <!-- Project badges -->
</p>

Herramienta CLI para cifrar y descifrar texto mediante el cifrado César. Está pensada para usuarios que necesitan una forma rápida de aplicar este cifrado desde la terminal, así como para quienes desean explorar una implementación limpia y bien documentada con fines educativos o de referencia.

---

### Características

#### Principales

- Cifrar y descifrar texto con el cifrado César
- Modo interactivo al ejecutar el programa sin argumentos
- Subcomandos `encrypt` y `decrypt` mediante `argparse`
- Clave aleatoria automática cuando no se especifica
- Soporte para mayúsculas y minúsculas; los caracteres no alfabéticos se conservan

#### Adicionales

- Arquitectura `src/` con separación entre la lógica de negocio y la interfaz de usuario
- Suite de pruebas automatizadas con `pytest`
- Punto de entrada de consola `cifrado-cesar`
- Validación de entrada de usuario

---

### Requisitos

- Python 3.12+

---

### Instalación

#### Clonar el repositorio

```bash
git clone https://github.com/usuario/proyecto.git
cd proyecto
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

O bien:

```bash
pip install .
```

---

### Uso

#### Modo interactivo

```bash
cifrado-cesar
```

#### Modo línea de comandos

```bash
cifrado-cesar encrypt "Hola Mundo" --shift 3
cifrado-cesar decrypt "Krod Pxqgr" --shift 3
```

---

### Estructura del Proyecto

```text
src/
└── cifrado_cesar/
    ├── __init__.py
    ├── core.py
    └── cli.py
tests/
├── test_core.py
README.md
CHANGELOG.md
pyproject.toml
LICENSE.md
```

- `core.py`: Contiene la lógica de cifrado y descifrado (`cifrar_cesar`, `descifrar_cesar`).
- `cli.py`: Maneja la interfaz de línea de comandos, los subcomandos y el menú interactivo.
- `tests/`: Pruebas unitarias para la lógica de cifrado.

---

### Ejecutar Tests

```bash
pytest
```

---

### Tecnologías

- Python 3.12+ con tipado estático
- argparse
- pytest
- hatchling

---

### Hoja de Ruta

- [ ] Interfaz gráfica con `tkinter` o `customtkinter`
- [ ] Modo archivo (cifrar y descifrar archivos completos)
- [ ] Opción de salida en el menú interactivo
- [ ] Evitar la salida automática después de cifrar o descifrar

---

### Contribuir

Las contribuciones, sugerencias y mejoras son bienvenidas.

---

### Licencia

Este proyecto está licenciado bajo la Licencia MIT.