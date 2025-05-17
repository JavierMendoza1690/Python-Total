

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')

    return otra_funcion

'''
Si agrego directamente el decorador imprime siempre 
Hola
texto
Adios
'''

#@decorar_saludo
def mayuscula(texto):
    print(texto.upper())
#@decorar_saludo
def minuscula(texto):
    print(texto.lower())

mayuscula('Javier') #Hola JAVIER Adios

#Forma de llamar el decorador cuando quiera
mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula_decorada('ivonne') #Hola IVONNE Adios

#Si quiero llamar solo a la funcion sin los decoradores
mayuscula('\nivonne') #IVONNE
