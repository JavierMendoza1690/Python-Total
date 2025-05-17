#ejercicio practico 1

#Creando variables
palabra = 'Python'
lista   = []

for letra in palabra:
    lista.append(letra) #agregando letra a la lista en cada vuelta

print(lista)

#--------------------------------COMPRENSION DE LISTAS--------------------------------------

#simplificando lo anterior, con comprension de listas
palabra_2='Python'
lista_2 = [letra for letra in palabra_2]
print(lista_2)

#Ejemplo comprension de listas simplificado con numeros

lista_3 = [n for n in range(2,12)]
print(lista_3)

#Ejemplo 4 comprension de listas simplificado
lista_4 = [n/2 for n in range(2,12)]
print(lista_4)

#-----------------------------COMPRENSION DE LISTAS CON CONDICIONALES--------------------------------------

lista_5 = [n for n in range(0,21,2) if n*2 >10]
print(lista_5)

#comprension de listas con condicionales if else
#si hay un else se debe poner el condicional antes del for
lista_6 = [n if n*2>10 else 'no' for n in range(0,21,2)]
print(lista_6)

#---------------------------EJEMPLO CON UNIDADES DE MEDICIÓN----------------------------------------------

pies    = [10, 20, 30 ,40]
metros  = [(medida/3,281) for medida in pies]

print(metros)