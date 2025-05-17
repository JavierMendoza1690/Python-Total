from random import *

#1.-Lista inicial
palitos = ['-', '--', '---', '----']

#2.-mezclar palitos en una funcion
def mezclar(lista):
    shuffle(lista) #mezclando la lista
    return lista


#3.-pedirle intento en una funcion
def probar_suerte():
    intento=''

    while(intento not in ['1','2','3','4']):
        intento = input('elige un numero del 1 al 4: ')

    return  int(intento)


#4.-Comprobar intento
def chequear_intento(lista,intento):
    if(lista[intento-1]=='-'):
        print('A lavar los platos')
    else:
        print('Esta vez te has salvado')

    print(f'Te ha tocado {lista[intento-1]}')

#-----------CODIGO PRINCIPAL-------------

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

