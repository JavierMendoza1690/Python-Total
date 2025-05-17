#importando modulo collections
from collections import Counter

numeros = [8,34,2,3,6,32,1,3,5,3,4,6,6,7,5,5,5,1,3,7,4]

'''
El metodo counter se encarga de contar la cantidad de veces que se repite un elemento en una lista
y los pone en un diccionario en el formato 

{elemento lista : numero_veces_repite}

y lo ordena de mayor a minor
'''
print(Counter(numeros))         #Counter({3: 4, 5: 4, 1: 2, 4: 2, 7: 2, 8: 1, 34: 1, 2: 1, 6: 1, 32: 1, 66: 1})


#Contando numero de veces que se repiten las letras de una palabra
print(Counter('mississippi'))   #Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

#contando numero de palabras repetidas
frase = 'al pan pan al al vino vino'
print(Counter(frase.split()))   #Counter({'al': 3, 'pan': 2, 'vino': 2})