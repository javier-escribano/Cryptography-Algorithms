import functions as f
import msvcrt

if __name__ =="__main__":
      S=[]
      T=[]
      plainText = ''
      cipherText=''

      option=f.getOption()
      while(True):
          if (option in ["e","E"]):
             f.faseInicial(S,T)
             caracter = chr(00)  ##Caracter Nulo
             while (caracter != ' '):
                 ##Va añadiendo el texto sin cifrar para luego mostrarlo
                 plainText = plainText + caracter
                 print('\nEnter a character (Enter to exit): ')
                 caracter = msvcrt.getwch()
                 print(caracter)
                 if(ord(caracter) == 13):
                     print("\nPlain Text: " + plainText)
                     print("\nCypher Text: " + cipherText + "\n")
                     break
                 else:
                     print("\nASCII codification: \n", ord(caracter))
                     print("Binary codification: \n", bin(ord(caracter)))
                     k = f.getKeystream(S,'E')
                     ##Va añadiendo el texto sin cifrar para luego mostrarlo
                     cipherText = cipherText + f.encode(caracter,k)
                     print("\n")
             #Limpia las variables para reutilizarlas en caso de volver a codificar
             S=[]
             T=[]
             plainText=''
             cipherText = ''
             option = f.getOption()
          else:
                f.faseInicial(S,T)
                tCifrado = input("\nEnter text to decrypt (Hexadecimal format): ")
                tCifrado = f.toHexa(tCifrado)
                keystream=[]
                for i in range(len(tCifrado)):
                    keystream.append(f.getKeystream(S,'D'))
                tDescifrado = f.decode(tCifrado, keystream)
                print(f.listToString(tDescifrado)+ "\n")
                option = f.getOption()
