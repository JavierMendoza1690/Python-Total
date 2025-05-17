'''Escribe una función llamada contar_primos() que requiera un solo argumento
numérico.Esta función va a mostrar en pantalla todos los números primos existentes
en el rango que va desde cero hasta ese número incluido, y va a devolver la cantidad
de números primos que encontró.Aclaración, por convención el 0 y el 1 no se consideran
primos.'''

def contar_primos(numero):
    #si es menor a 2 no hay primos
    if(numero<2):
        return 0

    primos = []

    for n in range(2,numero+1):
        es_primo=True
        for divisor in range(2,n):
            if(n % divisor == 0):
                es_primo=False
                break

        if(es_primo == True):
            primos.append(n)

    # Mostrar los números primos encontrados
    print(f"Números primos entre 0 y {numero}: {primos}")

    # Retornar la cantidad de números primos encontrados
    return len(primos)

#Invocando funcion:
print(contar_primos(100))
# Salida:
# Números primos encontrados: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# 10
