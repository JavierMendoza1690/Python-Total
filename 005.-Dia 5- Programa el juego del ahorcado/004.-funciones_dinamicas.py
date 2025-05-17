

#---------------------------EJEMPLO 1 FUNCIONES DIMANIMCAS-----------------------------------

#Funcion que se encargue de chequear si un determinado numero tiene tres cifrs
def chequear_3_cifras(numero):
    '''hace una comparacion si el numero está comprendido entre 0 y 999 retorna True si es verdad'''
    return numero in range(100,1000) #retorna un booleano
#---FIN FUNCION---

suma = 586 +402
resultado = chequear_3_cifras(suma)
print(resultado)


#---------------------------EJEMPLO 2 FUNCIONES DIMANIMCAS-------------------------------------


#verificar si al menos un elemento de una lista está en un rango entre cero y 1000
def chequear_3_cifras_2(lista):
    for n in lista:
        if( n in range(100,1000)):
            return True #el return acaba inmediatamente con el ciclo
        else:
            pass #No hace nada solo rellena el codigo y evita el error

    return False #si no encontró return False



resultado = chequear_3_cifras_2([1,1,2,10000])
print(resultado) #None si no encontró Nada

#---------------------------EJEMPLO 3 FUNCIONES DIMANIMCAS-------------------------------------


#llenar una nueva lista con los elementos que estén comprendidos entre 100 y 999
def chequear_3_cifras_3(lista):
    lista_3_cifras = []
    for n in lista:
        if( n in range(100,1000)):
            lista_3_cifras.append(n)
        else:
            pass #No hace nada solo rellena el codigo y evita el error

    return lista_3_cifras



resultado = chequear_3_cifras_3([1,1,2,10000,105,675])
print(resultado)
