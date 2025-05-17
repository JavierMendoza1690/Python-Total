#la funcion min o max puede recibir colecciones o una serie de numeros como argumendos

#funcion min
menor = min(58,96,72,64,35)
print('menor',menor)

#funcion max
mayor = max(58,96,72,64,35)
print('mayor',mayor)

#------------------------------MIN MAX SOBRE UNA LISTA --------------------------
#creando lista
lista = [58,96,72,64,35]

#minimo en la lista
menor_lista = min(lista)
print(menor_lista)

#maximo en lista
mayor_lista = max(lista)
print(mayor_lista)

#------------------------------MIN MAX SOBRE UNA LISTA DE STRINGS --------------------------

nombres = ['juan', 'pablo', 'alicia', 'carlos']

#imprimiendo el primer nombre por orden alfabetico
print(min(nombres)) #alicia

#imprimiendo el ultimo nombre por orden alfabetico
print(max(nombres)) #pablo

#------------------------------MIN MAX SOBRE UN STRING --------------------------

nombre = 'Carlos'

#imprimiendo la primera letre en orden alfabetico del nombre
print(min(nombre)) # C primero busca en mayusculas y luego en minusculas

#imprimiendo la ultima letra en orden alfabetico
print(max(nombre)) # s

#------------------------------MIN MAX SOBRE UN DICCIONARIO --------------------------

dic = {'C1':45, 'C2':11}

#buscando el minimo en el diccioario
print(min(dic)) #C1 busca por clave

#buscando el menor valor
print(min(dic.values())) #11 busca en valores