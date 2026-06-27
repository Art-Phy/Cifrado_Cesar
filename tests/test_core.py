import pytest

from cifrado_cesar import cifrar_cesar, descifrar_cesar


class TestCifrarCesar:
    def test_desplazamiento_conocido(self):
        assert cifrar_cesar("ABC", 1) == "BCD"
        assert cifrar_cesar("XYZ", 3) == "ABC"

    def test_conserva_mayusculas_minusculas(self):
        assert cifrar_cesar("AbC", 1) == "BcD"

    def test_minusculas(self):
        assert cifrar_cesar("abc", 1) == "bcd"

    def test_caracteres_no_alfabeticos_intactos(self):
        assert cifrar_cesar("ABC123!@#", 1) == "BCD123!@#"
        assert cifrar_cesar("Hola, mundo!", 3) == "Krod, pxqgr!"

    def test_desplazamiento_cero_identity(self):
        assert cifrar_cesar("Hola Mundo", 0) == "Hola Mundo"

    def test_desplazamiento_26_identity(self):
        assert cifrar_cesar("Hola", 26) == "Hola"

    def test_desplazamiento_grande(self):
        assert cifrar_cesar("ABC", 53) == "BCD"  # 53 = 27 = 1 mod 26

    def test_texto_vacio(self):
        assert cifrar_cesar("", 5) == ""


class TestDescifrarCesar:
    def test_descifrar_es_inverso(self):
        texto_original = "Hola Mundo"
        for shift in (1, 3, 13, 25, 0, 26):
            cifrado = cifrar_cesar(texto_original, shift)
            assert descifrar_cesar(cifrado, shift) == texto_original

    def test_desplazamiento_especifico(self):
        assert descifrar_cesar("BCD", 1) == "ABC"

    def test_texto_vacio(self):
        assert descifrar_cesar("", 5) == ""
