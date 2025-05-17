#usando el rango
for numero in range(5):
    print(numero) #imprime valores de range (del 0 al 5)

#ejemplo 2 de range, con dos argumentos
for numero in range(20,30):
    print(numero) #imprime del 20 al 29

#ejemplo range con 3 argumentos
for numero in range(20,30,2):
    print(numero) #imprime del 20 al 29 saltando de 2 en 2

#Creando una lista del 1 al 100 con la palabra range
lista = list(range(1,101))

print(lista)