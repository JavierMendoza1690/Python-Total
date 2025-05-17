#----------------------------------------INICIALIZANDO VARIABLES---------------------------------------

#creando e inicializando mi_tuple
mi_tuple = (1,2,3,4)
#creando tupla anidada
mi_tuple2 = (1,2,(10,20), 4)


#----------------------------------------CODIGO---------------------------------------
#imprimiendo tipo de mi_tuple
print(type(mi_tuple)) #<class 'tuple'>

#imprimiendo tupla
print(mi_tuple)

#imprimiendo posicion 0 de la tupla
print(mi_tuple[0]) #1

#imprimiendo posiciones negativas de tupla
print(mi_tuple[-2]) #3

#intentando cambiar valor tupla (error->inmutables)
#mi_tuple[0] =5
print(mi_tuple) #error

#imprimiendo tupla anidada
print(mi_tuple2[2]) #(10, 20)
print(mi_tuple2[2][1]) #20

#Haciendo casting a la tupla
casting_lista = list(mi_tuple2)
print(type(casting_lista))

print(casting_lista) #[1, 2, (10, 20), 4]

#asignar el contenido de una tupla a variables
t=(1,2,3)
x,y,z = t

print(t)

print(f'''x = {x}
y = {y}
z = {z}''')

#ejercicios adicionales

t=(1,2,3,1)
print(len(t))

#contando la cantidad de veces que está un elemento
print(t.count(1))

#encontrando el indice donde se encuentre el primer numero 2
print(t.index(2))