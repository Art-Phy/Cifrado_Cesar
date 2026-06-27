# Cifrado Cesar

Herramienta de linea de comandos para cifrar y descifrar texto utilizando el cifrado Cesar.

El cifrado Cesar es un metodo de sustitucion simple en el que cada letra del texto original se desplaza un numero fijo de posiciones en el alfabeto. Los caracteres no alfabeticos (numeros, espacios, signos de puntuacion) se mantienen intactos.

## Instalacion

```bash
pip install .
```

Para modo editable (desarrollo):

```bash
pip install -e .
```

## Uso

### Modo interactivo

Ejecuta el programa sin argumentos para usar el menu interactivo:

```bash
cifrado-cesar
```

### Modo CLI directo

Cifrar con desplazamiento aleatorio:

```bash
cifrado-cesar encrypt "Hola Mundo"
```

Cifrar con desplazamiento especifico:

```bash
cifrado-cesar encrypt "Hola Mundo" --shift 3
```

Descifrar:

```bash
cifrado-cesar decrypt "Krod Pxqgr" --shift 3
```

Ejecutar como modulo de Python:

```bash
python -m cifrado_cesar
```

## Pruebas

```bash
pip install -e ".[dev]"
pytest -v
```

## Licencia

MIT
