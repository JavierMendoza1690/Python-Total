
'''Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.

Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio'''

def devolver_distintos(integer_1,integer_2,integer_3):
    suma = integer_1+integer_2+integer_3
    lista_numeros = []
    lista_numeros.append(integer_1)
    lista_numeros.append(integer_2)
    lista_numeros.append(integer_3)
    if(suma>15):
        return max(integer_1, integer_2, integer_3)
    elif(suma<10):
        return min(integer_1,integer_2,integer_3)
    else:
        lista_ordenada = sorted(lista_numeros)
        return lista_ordenada[1]

print(devolver_distintos(11,1,2))