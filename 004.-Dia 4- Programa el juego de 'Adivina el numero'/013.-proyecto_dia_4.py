#Programa del juego adivina el numero

#importando librerias de random
from random import  *


#CREANDO VARIABLES
nombre = ''
intentos_restantes = 8
numero_ingresado =0


#--------------------------GENERANDO CODIGO--------------------------------

nombre = input('Por favor dime tu nombre para continuar: ')

#GENERANDO UN NUMERIO ALEATORIO ENTRE 1 Y 100
numero_aleatorio = randint(1,101)
print(numero_aleatorio)
#SOLICITANDO NUMERO AL USUARIO
while(intentos_restantes > 0):

    numero_ingresado = int(input('Por favor increse un numero comprendido entre 1 y 100'))

    if(numero_ingresado <1 or numero_ingresado > 100):
        print('el numero es invalido, intente con un valor comprendido entre 0 y 100')
        continue
    elif(numero_ingresado<numero_aleatorio):
        print('Seleccionaste un numero menor')
        intentos_restantes-=1
        continue
    elif(numero_ingresado>numero_aleatorio):
        print('Seleccionaste un numero mayor')
        intentos_restantes-=1
        continue
    else:
        print(f'Has ganado, te tomó {9-intentos_restantes} intentos')
        break


