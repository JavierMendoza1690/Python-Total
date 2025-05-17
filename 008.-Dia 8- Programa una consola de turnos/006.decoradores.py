def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

def una_funcion(funcion_parametro):
    return funcion_parametro

#puedo igualar la referencia de la funcion
mi_funcion = mayuscula

mi_funcion('javier')                #JAVIER

una_funcion(mayuscula('ivonne'))    #IVONNE