### Cifrado César ###

import random # para que el cifrado sea aleatorio

# creamos la función para cifrar
def cifrar_cesar(texto, desplazamiento):
    resultado = " "

    # hacemos que repita para cada carácter en el texto
    for char in texto:
        if char.isalpha(): # sólo cifra las letras
            base = ord('A') if char.isupper() else ord ('a') # mantenemos mayúsculas y minúsculas
            # realizamos el desplazamiento
            nuevo_char = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado += nuevo_char
        else:
            resultado += char # modifica sólo letras

    return resultado

# creamos la función para descifrar
def descifrar_texto(texto, desplazamiento):
    return cifrar_cesar(texto, - desplazamiento) # usamos el mismo desplazamiento pero a la inversa

# función de menu
def menu():
    opcion = " "
    while opcion not in ['c', 'd']:
        opcion = input("¿Quieres cifrar o descifrar? (c/d): ").lower()
        # evitamos que se responda algo diferente a 'c' o 'd'
        if opcion not in ['c', 'd']:
            print("Va a ser que no, prueba otra vez.")
    
    texto = input("Ingresa el texto: ")

    if opcion == 'c':
        desplazamiento = random.randint(1, 26) # desplazamiento aleatorio entre 1 y 26
        print(" Tu clave es:", desplazamiento)
        print("Tu texto cifrado es:", cifrar_cesar(texto, desplazamiento))
    elif opcion == 'd':
        desplazamiento = int(input("Ingresa la clave: "))
        print("Tu texto descifrado:", descifrar_texto(texto, desplazamiento))

# ejecutamos el menu
menu()
