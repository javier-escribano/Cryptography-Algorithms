#!/usr/bin/python3
import sys


def encrypt(text, key):
    cifrado = ""
    cifrado2 = ""

    # polybios con clave, la key indica el desplazamiento para las letras
    # resultantes del cifrado, las cabaceras de la tabla
    for char in text:

        # finding row of the table
        row = int((ord(char) - ord("A")) / 5) + 1

        # finding column of the table
        col = ((ord(char) - ord("A")) % 5) + 1

        # if character is 'k'
        if char == "K":
            row = row - 1
            col = 5 - col + 1

        # if character is greater than 'j'
        elif ord(char) >= ord("J"):
            if col == 1:
                col = 6
                row = row - 1

            col = col - 1

        r = str(chr((key % 26) + 65 + row))
        c = str(chr((key % 26) + 65 + col))
        cifrado = cifrado + r + c

    cifrado = cifrado[::-1]  # devuelve la cadena invertida

    # cesar solo con Letras mayusculas
    for i in range(len(cifrado)):  # Para cada letra del texto
        char = cifrado[i]
        cifrado2 += chr((ord(char) + key - 65) % 26 + 65)

    return cifrado2


def decrypt(text, key):

    descifrado = ""
    descifrado2 = ""

    # descifrado cesar solo con letras mayusculas
    for i in range(len(text)):  # Para cada letra del texto
        char = text[i]
        descifrado += chr((ord(char) - key - 65) % 26 + 65)  # Prima letra mayuscula (A)

    descInvert = descifrado[::-1]  # invierte la cadena
    cadena = list(descInvert)

    # descifrado polybios con clave key
    for i in range(0, len(descInvert), 2):

        r = int(ord(cadena[i]) - ((key % 26) + 65))
        c = int(ord(cadena[i + 1]) - ((key % 26) + 65))
        ch = chr(((r - 1) * 5 + c + 64))
        if ord(ch) - 64 >= 10:
            ch = chr(((r - 1) * 5 + c + 64 + 1))
        ch1 = str(ch)
        descifrado2 = descifrado2 + ch1

    return descifrado2


if __name__=="__main__":

    if (len(sys.argv) == 4):

        fichero = sys.argv[2]
        text = open(fichero, 'r').read()
        key = sys.argv[3]

        if (sys.argv[1] == "-e"):
            print(encrypt(text,ord(key)))

        elif (sys.argv[1] == "-d"):
            print(decrypt(text, ord(key)))

    elif (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        print("\n[*] Usage: ./monoalfabeto.py <action> <file_to_encrypt/file_to_decrypt> <key>(int)\n")
        print("Actions:")
        print("-d -> decrypts a file.")
        print("-e -> encrypts a file.")
        print("-h -> displays this help menu.")
        print("THE KEY MUST BE AN INTEGER\n")

    else:
        print("[*] Usage: ./monoalfabeto.py <action> <file_to_cipher/file_to_decipher> <key>(int)")
