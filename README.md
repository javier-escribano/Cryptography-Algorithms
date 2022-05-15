# Cryptography-Algorithms

This repository will host some cryptography algorithms that belong to different types of cypher.

## Vigenere

Vigenere's algorithm works by substitution operations performed by some rounds of permutations depending on the key and the letters in them. In this particular case, the algorithm will only work with the 26 capital letters in the alphabet, no special characters are concerned in the processing stage of the algorithm.

Usage:
- Linux:
  - ``python3 ./vigenere.py <action> <file_to_encrypt/file_to_decrypt> <key>``
- Windows:
  - ``python.exe vigenere.py <action> <file_to_encrypt/file_to_decrypt> <key>``

## RC4 

RC4's algorithm is used in data flows in order to encrypt in a sequencial procedure. In order to understand the process and make it interactive, this version works by pressing enter in each letter that we want to encrypt.
Especifically if we want to encrypt, we will need to provide the program some number key and then we will proceed to enter the process of encryption step by step.

Usage:
- Linux:
  - ``python3 ./RC4.py ``
- Windows:
  - ``python.exe RC4.py``

## Kasiski's method

Kasiski's method is used to decrypt an encrypted text with Vigenere's algorithm, although it can be used to try a decryption with any encrypted text using a substitution encryption technique.
In this repository there will be two files, *kasiski.py* and *ftable.py*. The first one will guess the number of characters in the key, then the second file will try to guess which character is in each position of the key.

Usage:
- Linux:
  - ``python3 ./kasiski.py <encrypted_text>``
  - ``python3 ./ftable.py <key_characters>`` 
- Windows:
  - ``python.exe kasiski.py <encrypted_text>``
  - ``python.exe ftable.py <key_characters>``

## Monoalphabet algorithm

This algorithm is a tecnhique of encryption that uses substitution with one alphabet (Caesar's tecnhique) and Polybios algorithm changing default parameters.

Usage:
- Linux:
  - ``python3 ./monoalfabeto.py <action> <file_to_encrypt/file_to_decrypt> <key>(int)``
- Windows:
  - ``python.exe monoalfabeto.py <action> <file_to_encrypt/file_to_decrypt> <key>(int)``
