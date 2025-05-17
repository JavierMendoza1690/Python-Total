import time

'''
    Las dos funciones tienen la misma eficacia
    pero no la misma eficiencia, para saber que funcion
    lo hizo mas rapido podemos medir el tiempo en que se ejecutó
    el codigo, y lo podemos hacer midiendo el tiempo en que realiza
    la accion
    
    para empezar a medir tiempo debemos generar una marca similar a:
    inicio = time.time()
'''


def prueba_for(numero):
    lista = []
    for num in range(1, numero +1):
        lista.append(num)
    return  lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return  lista

def main():
   #para empezar a medir el tiempo debemos hacer una marca
   inicio = time.time()
   prueba_for(1000000)
   final = time.time()

   #Calculando el tiempo que transcurrio desde la llamada de prueba_for
   tiempo_transcurrido = final - inicio
   print(f'El tiempo que tardo en ejecutarse prueba_for fue de {tiempo_transcurrido}') #0.1424403190612793

   #calculando el tiempo de la funcion prueba_while

   inicio_while = time.time()
   prueba_while(1000000)
   final_while = time.time()
   tiempo_while = final_while - inicio_while
   print(f'El tiempo que tardo en ejecutarse prueba_for fue de {tiempo_while}')         #0.42195987701416016

'''
 el ciclo for tomó menos tiempo que el ciclo while
'''

if __name__ == '__main__':
    main()