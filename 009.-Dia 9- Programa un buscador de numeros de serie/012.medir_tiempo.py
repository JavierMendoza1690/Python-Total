import timeit

'''
    Usando modulo timeit:
    
    timeit tiene la funcion de identificar el tiempo de ejecucion de un bloque de codigo que le pasemos
'''

def main():
    declaracion = '''
prueba_for(10)
    '''

    mi_setup ='''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
    '''

    duracion = timeit.timeit(declaracion,mi_setup, number= 100000)
    print(duracion)     #0.21355840004980564

    declaracion_2 = '''
prueba_while(10)
    '''

    mi_setup_2 ='''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
    '''

    duracion_2 = timeit.timeit(declaracion_2, mi_setup_2, number=100000)

    print(duracion_2)   #0.10053769999649376


if __name__ == '__main__':
    main()