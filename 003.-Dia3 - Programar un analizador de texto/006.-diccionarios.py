#declarando diccionario
#las claves no se pueden repetir, pero los valores si
diccionario = {'c1':'valor1','c2':'valor2'}

#imprimiendo type de diccionario
print(type(diccionario)) #<class 'dict'>

#imprimiendo el contenido diccionario
print(diccionario)

#imprimiendo el contenido de una clave
resultado = diccionario['c2']
print(resultado) #'valor2


#------------------------------ EJEMPLO DICCIONARIO-----------------------
cliente = {'nombre':'Juan', 'apellido':'Fuentes', 'peso':88, 'talla': 1.76}
consulta = (cliente['apellido'])
print(consulta)

#------------------------------ EJEMPLO 2 DICCIONARIO-----------------------
dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
print(dic['c2'][1])
print(dic['c3']['s2'])

#------------------------------ EJEMPLO 3 DICCIONARIO-----------------------
dic = {'c1':['a','b','c'], 'c2':['d','e','f']}
print(dic['c2'][1].upper())
#------------------------------ EJEMPLO 4 DICCIONARIO-----------------------
#agregar elementos a un diccionario que ya ha sido creado
dic = {1:'a', 2:'b'}
print(dic)

#AGREGANDO NUEVA CLAVE VALOR AL DICCIONARIO
dic[3] = 'c'
print(dic)

#LOS DICCIONARIOS SON MUTABLES
#sobreescribiendo el valor de la clave 2
dic[2] = 'B'
print(dic)

#IMPRIMIENDO SOLO CLAVES DEL DICCIONARIO (las regresa en una lista)
print(dic.keys()) #dict_keys([1, 2, 3])

#IMPRIMIENDO SOLO VALORES DEL DICCIONARIO
print(dic.values()) #dict_keys

#IMPRIMIENDO ITEMS EN PARES (TUPLAS)
print(dic.items())