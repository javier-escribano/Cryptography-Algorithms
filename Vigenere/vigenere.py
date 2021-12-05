#!/usr/bin/python3

import sys

def encrypt(plaintext, key):

    k_length = len(key)
    key_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''

    for i in range(len(plaintext_int)):
        number = (plaintext_int[i] + key_int[i % k_length]) % 26
        ciphertext += chr(number + 65)

    return(ciphertext) 


def decrypt(ciphertext, key):

    k_length = len(key)
    key_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''

    for i in range(len(ciphertext_int)):
        number = (ciphertext_int[i] - key_int[i % k_length]) % 26
        plaintext += chr(number + 65)

    return(plaintext)

if __name__=="__main__":

    if (len(sys.argv) == 4):

        fichero = sys.argv[2]
        text = open(fichero, 'r').read()
        key = sys.argv[3]

        if (sys.argv[1] == "-e"):
            print(encrypt(text,key))

        elif (sys.argv[1] == "-d"):
            print(decrypt(text, key))

    elif (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        print("\n[*] Usage: ./vigenere.py <action> <file_to_encrypt/file_to_decrypt> <key>\n")
        print("Actions:")
        print("-d -> decrypts a file.")
        print("-e -> encrypts a file.")
        print("-h -> displays this help menu.")

    else:
        print("[*] Usage: ./vigenere.py <action> <file_to_encrypt/file_to_decrypt> <key>")
        print("Type -h for more information.")

    