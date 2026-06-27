def cifrar_cesar(texto: str, desplazamiento: int) -> str:
    """Encrypt text using the Caesar cipher.

    Args:
        texto: The text to encrypt.
        desplazamiento: Number of positions to shift each letter.

    Returns:
        The encrypted text.
    """
    resultado = ""

    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nuevo_char = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado += nuevo_char
        else:
            resultado += char

    return resultado


def descifrar_cesar(texto: str, desplazamiento: int) -> str:
    """Decrypt text encrypted with the Caesar cipher.

    Decryption is equivalent to encryption with a negative shift.

    Args:
        texto: The encrypted text.
        desplazamiento: The shift used during encryption.

    Returns:
        The decrypted text.
    """
    return cifrar_cesar(texto, -desplazamiento)
