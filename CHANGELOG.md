# 📜 CHANGELOG
Todas las modificaciones importantes de este proyecto se documentarán en este archivo.

El formato sigue las convenciones de [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/)
y este proyecto utiliza [Versionado Semántico](https://semver.org/lang/es/).

---

## [v1.0.0] - 2025-10-26
### ✨ Añadido
- Funcionalidad principal del **Cifrado César**, permitiendo cifrar y descifrar texto.
- Opción de generar automáticamente una **clave aleatoria** al cifrar.
- Soporte para **mayúsculas y minúsculas**, manteniendo caracteres no alfabéticos intactos.
- **Estructura modularizada** con funciones separadas (`cifrar_cesar`, `descifrar_cesar`, `mostrar_menu`).
- Comentarios y **docstrings detallados** para facilitar el mantenimiento.
- Archivo `requirements.txt` (sin dependencias externas).

### 🔧 Mejorado
- Reorganización completa del código en `maincc.py` para hacerlo más legible y escalable.
- Validación de entradas de usuario (clave numérica y opciones del menú).
- Implementación de estructura `if __name__ == "__main__":` para futuras integraciones (CLI o GUI).

### 📂 Estructura actual del repositorio
Cifrado_Cesar/
├── LICENSE.md
├── README.md
├── CHANGELOG.md
├── maincc.py
├── requirements.txt
└── cifrado_cesar.code-workspace


---

## [Sin publicar]
### 🚧 En desarrollo
- Añadir pruebas unitarias automáticas (`pytest`).
- Implementar interfaz gráfica (GUI) con `tkinter` o `customtkinter`.
- Soporte para cifrado personalizado (clave manual y modo archivo).
- Añadir una opción de "salir" en el menú actual en terminal.
- Eliminar la salida automática después del cifrado o descifrado.