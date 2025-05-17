#diferencia entre = y ==

#el igual hace una asignación
mi_variable = 'hola mundo'

#el == se usa para hacer una comparacion
mi_bool =   (10 == 25) #compara si 10 es igual a 25 (false)
print(mi_bool)
mi_bool2 =  (5+5 ==18-8) #compara los resultados (true
print(mi_bool2)

#COMPARACION DE STRINGS
# la comparacion de strings es sensible a mayusculas
bool_strings    = 'blanco' == 'Blanco'          #False
bool_strings2   = 'blanco' == 'blanco'          #True
bool_strings3   = 'blanco' == 'Blanco'.lower()  #False

print('bool 1',bool_strings)
print('bool 2',bool_strings2)

#COMPARANDO DATOS DIFERENTES
mi_bool4 = '100' == 100     #False
mi_bool5 = 100.0 == 100     #True

print('bool 4',mi_bool4)
print('bool 5',mi_bool5)

#COMPARANDO DIFERENCIA
mi_bool6 = '100' != 100     #True
mi_bool7 = 5 >= 6           #False

print('bool 6',mi_bool6)
