
#Para que se cumpla un operador "and" ambas funciones deben ser verdaderas, de lo contrario será false
mi_bool = (4 < 5) and (5 > 6)
print(mi_bool)
#Ejemplo 2 "and"
mi_bool2 = ( 55 == 55 ) and ("perro" == "perro")
print(mi_bool2)

#la funcion or requiere que solo una condicion sea verdadera para que el conjunto sea verdadero
mi_bool3 = (10==10) or (3==3)
print(mi_bool3)

mi_bool4= (10==9) or (3==3)
print("mi_bool4",mi_bool4)

mi_bool5= (10==9) or (3==2)
print("mi_bool5",mi_bool5)

# Ejemplo con in

texto = "Javier es chiquiluqui"
mi_bool6 = ("Javier" in texto) and ('chiquiluqui' in texto)
print("mi_bool6", mi_bool6)

#OPERADOR LOGICO NOT
#invierte el booleano que le sigue
mi_bool7 = not('a' =='a') #que 'a' no sea igual a 'a'
print('mi_bool7',mi_bool7)