'''Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']'''

#Definiendo Funcion
def ordenar_string(palabra):
    #pasando la lista a lower
    palabra_lower = palabra.lower()
    print(sorted(set(palabra_lower)))

#Invocando funcion
ordenar_string('entretenido')