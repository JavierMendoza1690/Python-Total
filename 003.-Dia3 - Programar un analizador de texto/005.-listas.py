#creando lista
mi_lista = ['a', 'b','c']
#creando lista con diferentes tipos de datos
otra_lista = ['Hola', 55, 6.1]
#crando mi_lista2
mi_lista2 = ['d','e','f']
#creando lista_auxiliar
lista_auxiliar = ['g','o','b','m','c']

#--------------------------------------------CODIGO--------------------------------------------

#imprimiendo el tipo de mi_lista
print(type(mi_lista)) #<class 'list'>

#calculando la logitud de mi_lista
longitud = len(mi_lista)
print(longitud)

#extrayendo el valor de uno de los elementos de mi_lista
primercampo = mi_lista[0]
print(primercampo) #devuelve 'a'

#extrayendo elementos con un slice
dos_primeros_campos = mi_lista[0:2]
print(type(dos_primeros_campos))    #<class 'list'>
print(dos_primeros_campos)          #['a', 'b']

#concatenando listas
mi_lista_3 = mi_lista + mi_lista2
print(mi_lista_3) #['a', 'b', 'c', 'd', 'e', 'f']

#mutando mi_lista_3
mi_lista_3[0] = 'alpha'
print(mi_lista_3) #['alpha', 'b', 'c', 'd', 'e', 'f']

#agregando elemento al final de la lista (append) (muta)
mi_lista_3.append('g')
print(mi_lista_3)

#eliminar el ultimo elemento de una lista
mi_lista_3.pop()
print(mi_lista_3)

#eliminar un indice especifico de una lista
elemento_eliminado = mi_lista_3.pop(0) #elimina el indice 0
print(elemento_eliminado)

#ordenar listas
#sort no es un metodo que devuelva nada
print(f'lista desordenada {lista_auxiliar}')
lista_auxiliar.sort()
print(f'lista ordenada {lista_auxiliar}')   #ordenado alfabeticamente o numericamente
print(type(lista_auxiliar.sort()))          #resultado de un metodo que no devuelve nada

#invertir el orden de una lista
print(f'lista al derecho {lista_auxiliar}')
lista_auxiliar.reverse()
print(f'lista al reves {lista_auxiliar}')





