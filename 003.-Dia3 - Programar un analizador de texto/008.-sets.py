#-------------------------Declarando variables---------------------------------
mi_set = set([1,2,3,4,5,6,7])   #forma 1 de declarar un set
#Declarando otro set
otro_set = {1,2,3,4,5,6,7,8}    #forma 2 de declarar un set


#---------------------------IMPRIMIENDO OTRO SET-------------------------------
#imprimiendo tipo del set
print(type(set))

#imprimiendo el set
print(mi_set)  #<class 'type'>

#imprimiendo otro_set
print(otro_set)

#tratando de imprimir el indice cero del set (ERROR)
#print(mi_set[0])  #ERROR (los sets no tienen indices)

#creando un set con elementos repetidos
mi_set2 = set([1,2,3,4,5,6,7,1,1,1,2,2,7])
print(mi_set2) #{1, 2, 3, 4, 5, 6, 7}

#no se pueden agregar listas o diccionarios dentro de un set
#mi_set3= set((1,2,[2,3],{'cv1':5},5,6))
#print(mi_set3) #ERROR

#Si se pueden agregar tuplas a un set ya que son inmutables
mi_set4=((1,2,3,('a',7),9))
print(mi_set4)

#cantidad de elementos de una tupla
print(len(mi_set))

#Buscar un elemento en mi_set
print(2 in mi_set)

#--------------------------------METODOS DE SETS-------------------------------
#UNION DE SETS (union)
s1 = {1,2,3}
s2 = {3,4,5}

s3 = s1.union(s2)

print(s3)

#AGREGAR UN ELEMENTO A UN SET
s1.add(4)
print(s1)

#ELIMINAR UN ELEMENTO (REMOVE) (DA ERROR SI NO EXISTE UN ELEMENTO)
s1.remove(3)
#s1.remove(9) #ERROR
print(s1)

#DESCARGAR UN ELEMENTO (NO DA ERROR SI NO EXISTE UN ELEMENTO)
s1.discard(9)
print(s1)

#ELIMINAR UN ELEMENTO CON POP (ELIMINA UNO ALEATOREO AL NO TENER ORDEN)
#s1.pop() #elimina elemento aleatorio (no recomendable)

#ELIMINAR TODOS LOS ELEMENTOS DEL SET
s1.clear()
print(s1) #set()