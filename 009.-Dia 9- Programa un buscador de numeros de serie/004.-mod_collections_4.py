from collections import namedtuple

#mi_tupla = (500,18,65)
#print(mi_tupla[1])      #18


'''
Hace algo similar a convertir una tupla en una clase, para mejorar la busqueda
'''

#modificando nombre de la tupla y valores que recibirá
Persona = namedtuple('Persona',  ['nombre','altura', 'peso'])
ariel = Persona('Ariel',1.76, 79)

print(ariel.altura)     #1.76
print(ariel[1])         #1.76