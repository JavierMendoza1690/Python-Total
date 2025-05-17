#forma tradicional de buscar indices
lista = ['a','b','c']
indice = 0

for item in lista:
    print(f'indice:{indice} item: {item}')
    indice+=1

#Forma con enumerate general

lista_2 = ['a','b','c']

for item in enumerate(lista):
    print(item) #genera una tupla con indice y valor (0, 'a')

#--------------------------FORMA ENUMERATE DESESTRUCTURADA-----------------------------------------------------
lista_3 = ['a','b','c']
#se desestructura la tupla antes de trabajarla
for indice, item in enumerate(lista):
    print(f'indice:{indice} item: {item}')

#--------------------------FORMA ENUMERATE DESESTRUCTURADA CON ENTEROS--------------------------------------------

#se desestructura la tupla antes de trabajarla
for indice, item in enumerate(range(50,55)):
    print(f'indice:{indice} item: {item}')

#--------------------------TRANSFORMANDO LISTA EN UNA LISTA DE TUPLAS----------------------------------------------

lista_4 = ['a','b','c']

#verificando que la enumeracion quede en forma de lista
#print(list(enumerate(lista_4))) #[(0, 'a'), (1, 'b'), (2, 'c')]

#creando variable mi_lista_tuples con lo hecho en la linea anterior
mi_lista_tuples = list(enumerate(lista_4))

#imprimiendo mi_lista_tuples
print(mi_lista_tuples)