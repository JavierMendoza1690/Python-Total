
lista = ['a', 'b', 'c', 'd']

#creando loop for
for letra in lista:
    #obteniendo indice de la iteracion
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra} ")

#--------------------EJEMPLO 2----------------------
lista2 = ['pablo', 'laura', 'fede', 'luis', 'julia']

for nombre in lista2:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que no comienza con L')

#-----------------EJEMPLO 3----------------------
numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor += numero

print(mi_valor)

#---------------EJEMPLO 4------------------------

for letra in 'python':
    print(letra)

#---------------EJEMPLO 5-----------------------
#iterando en una lista
for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
   # print(b)

# ---------------EJEMPLO 6-----------------------

#iterando en diccionario

dic = {'clave1':'a', 'clave2':'b','clave3':'c'}

for item in dic:
    print(item) #imprime solo las claves

for item in dic.items():
    print(item) #imprime (clave, valor) en tuplas

for item in dic.values():
    print(item) #imprime solo valores

for a,b in dic.items():
    print(a,b) #claves en a y valores en b