import ast
import msvcrt

def hexa(l):
    for i in range(len(l)):
        l[i] = hex(l[i])
    print(l)
    return l


def binario(l):
    aux = []
    for i in range(len(l)):
        aux.append(bin(l[i]))
    print(aux)

#Initialization
def Inits(S,T,K):
    for i in range(256):
        S.append(i)
        T.append(K[i % len(K)])

    print("Initial value of S: \n")
    binario(S)

def swap(S,a,b):
    temp=S[a]
    S[a]= S[b]
    S[b]=temp

    #Initial Permutation of S
def res(S,T):
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        swap(S,i,j)

    print("\nS value after initial procedure: \n")
    binario(S)
    print("\n")

def getKeystream(S,option):
    i=0
    j=0
    i = (i+1) % 256
    j = (j + S[i]) % 256
    swap(S,i, j)
    t = (S[i] + S[j]) % 256
    k = S[t]
    if (option in ["e","E"]):
        print("\nS Vector with keystream generation: \n")
        binario(S)
        print("\nKeystream value: \n", k)
    return k

def encode (plainText,k):
    cipherText=chr(ord(plainText)^k)
    print("Encrypted character binary codification: \n", bin(ord(cipherText)))
    print("Encrypted character hexadecimal codification: \n", hex(ord(cipherText)))
    return cipherText


def decode(texto,keystream):
    descifrado = []
    for i in range(len(texto)):
        descifrado.append(chr(texto[i]^keystream[i]))
    return descifrado


def getOption():
    option= ""
    while (option not in ["e", "E", "d", "D"]):
        print("Enter (e) to encrypt, (d) to decrypt or Enter to exit:\n")
        option = msvcrt.getwch()
        print(option)
        if (ord(option) == 13 ):
            print("Program ends")
            quit()
        if (option not in ["e", "E", "d", "D"]):
            print("Error: Invalid character\n")
    return option


def faseInicial(S,T):
     clave = input ("\nEnter key(numerical value): ")
     Inits(S,T,toHexa(clave))
     res(S,T)

def toHexa(text):
    return [int(text[i:i+2],16) for i in range(0,len(text),2)]

def listToString(list):
    string=''
    for i in range(len(list)):
        string = string + list[i]
    return string
