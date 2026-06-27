import argparse
import random
import sys

from cifrado_cesar.core import cifrar_cesar, descifrar_cesar


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cifrado-cesar",
        description="Encrypt or decrypt text using the Caesar cipher.",
    )
    sub = parser.add_subparsers(dest="command")

    enc = sub.add_parser("encrypt", help="Encrypt text")
    enc.add_argument("text", help="Text to encrypt")
    enc.add_argument("--shift", type=int, help="Shift value (random if omitted)")

    dec = sub.add_parser("decrypt", help="Decrypt text")
    dec.add_argument("text", help="Text to decrypt")
    dec.add_argument("--shift", type=int, required=True, help="Shift value used for encryption")

    return parser


def run_interactive() -> None:
    print("\n=== Cifrado Cesar ===")
    print("Selecciona una opcion:")
    print("  [c] Cifrar texto")
    print("  [d] Descifrar texto")
    print("-----------------------")

    opcion = ""
    while opcion not in ("c", "d"):
        opcion = input("Quieres cifrar o descifrar? (c/d): ").lower()
        if opcion not in ("c", "d"):
            print("Opcion invalida, intenta nuevamente.\n")

    texto = input("\nIngresa el texto: ")

    if opcion == "c":
        shift = random.randint(1, 26)
        print(f"Clave de cifrado generada: {shift}")
        resultado = cifrar_cesar(texto, shift)
        print(f"Texto cifrado: {resultado}\n")
    elif opcion == "d":
        while True:
            try:
                shift = int(input("Ingresa la clave numerica: "))
                break
            except ValueError:
                print("La clave debe ser un numero entero.")
        resultado = descifrar_cesar(texto, shift)
        print(f"Texto descifrado: {resultado}\n")


def run_encrypt(args: argparse.Namespace) -> None:
    shift = args.shift if args.shift is not None else random.randint(1, 26)
    resultado = cifrar_cesar(args.text, shift)
    print(resultado)
    if args.shift is None:
        print(f"Shift: {shift}")


def run_decrypt(args: argparse.Namespace) -> None:
    resultado = descifrar_cesar(args.text, args.shift)
    print(resultado)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command is None:
        run_interactive()
    elif args.command == "encrypt":
        run_encrypt(args)
    elif args.command == "decrypt":
        run_decrypt(args)


if __name__ == "__main__":
    main()
