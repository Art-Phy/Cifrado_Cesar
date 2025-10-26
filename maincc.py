"""
=============================
     CIFRADO CÉSAR (v2)
=============================

Autor: Art-Phy
Descripción:
  Programa que permite cifrar o descifrar texto utilizando el cifrado César.
  Mantiene mayúsculas/minúsculas y deja intactos los caracteres no alfabéticos.
  Incluye desplazamiento aleatorio para el cifrado.

Mejoras respecto a la versión anterior:
- Docstrings y comentarios explicativos.
- Validación de entradas.
- Lógica modularizada y más legible.
- Manejo de errores de entrada de clave.
- Estructura preparada para pruebas unitarias o futura CLI.

"""

import random


def cifrar_cesar(texto: str, desplazamiento: int) -> str:
    """
    Cifra el texto recibido utilizando el cifrado César.

    Args:
        texto (str): Texto que se desea cifrar.
        desplazamiento (int): Número de posiciones que se desplazará cada letra.

    Returns:
        str: Texto cifrado.
    """
    resultado = ""

    for char in texto:
        if char.isalpha():  # Solo cifrar letras
            # Determina si el carácter es mayúscula o minúscula
            base = ord('A') if char.isupper() else ord('a')
            # Aplica desplazamiento y vuelve a convertir a carácter
            nuevo_char = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado += nuevo_char
        else:
            # Si no es letra, se deja igual
            resultado += char

    return resultado


def descifrar_cesar(texto: str, desplazamiento: int) -> str:
    """
    Descifra un texto cifrado con el cifrado César.

    Args:
        texto (str): Texto cifrado.
        desplazamiento (int): Desplazamiento utilizado para cifrar el texto.

    Returns:
        str: Texto descifrado.
    """
    # Descifrar es equivalente a cifrar con desplazamiento negativo
    return cifrar_cesar(texto, -desplazamiento)


def mostrar_menu() -> None:
    """
    Muestra el menú principal y gestiona la interacción con el usuario.
    """
    print("\n=== Cifrado César ===")
    print("Selecciona una opción:")
    print("  [c] Cifrar texto")
    print("  [d] Descifrar texto")
    print("-----------------------")

    opcion = ""
    while opcion not in ('c', 'd'):
        opcion = input("¿Quieres cifrar o descifrar? (c/d): ").lower()
        if opcion not in ('c', 'd'):
            print("⚠️  Opción inválida, intenta nuevamente.\n")

    texto = input("\nIngresa el texto: ")

    if opcion == 'c':
        desplazamiento = random.randint(1, 26)
        print(f"\n🔑 Clave de cifrado generada: {desplazamiento}")
        texto_cifrado = cifrar_cesar(texto, desplazamiento)
        print(f"🧩 Texto cifrado: {texto_cifrado}\n")

    elif opcion == 'd':
        while True:
            try:
                desplazamiento = int(input("Ingresa la clave numérica: "))
                break
            except ValueError:
                print("⚠️  La clave debe ser un número entero.")
        texto_descifrado = descifrar_cesar(texto, desplazamiento)
        print(f"\n📜 Texto descifrado: {texto_descifrado}\n")


if __name__ == "__main__":
    # Punto de entrada principal del programa
    mostrar_menu()
