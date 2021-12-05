from collections import Counter
from math import gcd
import sys

distlist=[]
text = open(sys.argv[1]).read()

def get_trigs():
	rec_trig = {}
	for i in range(len(text)-2):
		current_trig = text[i]+text[i+1]+text[i+2]	#Seleccionamos el trigrama actual
		if not current_trig in rec_trig:	#Si no esta dentro de los recorridos lo metemos en el diccionario
			rec_trig[current_trig] = [i]    #Guarda la posicion en la que empieza el trigrama
		else:
			aux = rec_trig[current_trig][-1] #Se coge la posicion anterior en la lista dentro del trigrama actual
			rec_trig[current_trig].append(i-aux) #Se calcula la distancia entre la posicion anterior en la que aparecia el trigrama y la actual

	for trig in rec_trig:
		rec_trig[trig].pop(0)
		if len(rec_trig[trig])>0: 
			for count in range(len(rec_trig[trig])):
				actual = rec_trig[trig].pop(0)
				distlist.append(actual)			#Se guardan las distancias de los trigramas que aparecen más de una vez

def frequenceAndMcd():	
	frequents = Counter(distlist).most_common(6)	#Cogemos los 6 elementos mas comunes debido a que el objetivo es encontrar un numero que divida la mayoria pero no 
	frequents_list=[]								#todas las separaciones, y la mayoría de los números son divisibles por 6
	for i in range(len(frequents)):
		frequents_list.append([frequents[i][0]])

	aux2=frequents_list.pop(0).pop(0)
	for elem in range(len(frequents_list)):
		mcd=gcd(aux2,frequents_list.pop(0).pop(0))	#Hacemos el maximo comun divisor
		aux2=mcd

	return mcd

if __name__=='__main__':
	get_trigs()
	mcd = frequenceAndMcd()
	print('Your key has', mcd, 'characters\n')