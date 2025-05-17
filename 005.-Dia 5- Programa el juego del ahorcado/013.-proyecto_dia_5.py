#JUEGO EL AHORCADO
from random import *


#definiendo funcion que decide una palabra al azar
def palabra_azar():
    '''esta funcion retorna una palabra al azar de las almacenadas en una lista'''
    palabras_ahorcado = [
        "python", "programacion", "computadora", "teclado", "monitor",
        "internet", "algoritmo", "variable", "funcion", "bucle",
        "guitarra", "piano", "musica", "artista", "cantante",
        "futbol", "baloncesto", "natacion", "atletismo", "ciclismo",
        "elefante", "jirafa", "tigre", "delfin", "leon",
        "manzana", "banana", "naranja", "sandia", "fresa"
    ]
    palabra_seleccionada = choice(palabras_ahorcado)
    return palabra_seleccionada

def mostrar_guiones(palabra):
    '''
    esta funcion se encarga de mostrar la cantidad de guiones
    que debe ver el usuario en base a la palabra que se recibe como argumento
    '''

    guiones = ' '.join('_' for letra in palabra)
    #print(palabra)
    #print(guiones)
    return  guiones

def pedir_letra_usuario(letras_usadas):

    es_valida = False

    while( not es_valida):
        letra_ingresada = input('Por favor ingrese una letra: ').strip()

        if(len(letra_ingresada)!=1):
            pass
        elif not letra_ingresada.isalpha():
            print("Error: Solo se permiten letras (a-z).")
            pass
        elif letra_ingresada in letras_usadas:
            print(f"Ya usaste la letra '{letra_ingresada}'. Intenta otra.")
        else:
            # Convierte a minúscula para uniformidad
            letra = letra_ingresada.lower()
            letras_usadas.append(letra)
            es_valida = True

    return letra


'''def verificar_letras(palabra_secreta, letras_usadas, ultima_letra=None):
    """
    Verifica letras usadas en la palabra secreta y genera representación con guiones.

    Args:
        palabra_secreta (str): Palabra a adivinar
        letras_usadas (set/list): Letras ya intentadas
        ultima_letra (str, optional): Última letra ingresada para verificación especial

    Returns:
        tuple: (string_resultante, acierto_ultima_letra)
    """
    resultado = []
    acierto_ultima = False

    # Convertimos a minúsculas para comparación sin distinción de mayúsculas
    palabra_secreta = palabra_secreta.lower()
    letras_usadas = {letra.lower() for letra in letras_usadas}

    if ultima_letra:
        ultima_letra = ultima_letra.lower()
        acierto_ultima = ultima_letra in palabra_secreta

    for letra in palabra_secreta:
        if letra in letras_usadas:
            resultado.append(letra.upper())  # Mostramos letras adivinadas en mayúsculas
        else:
            resultado.append('_')

    return ' '.join(resultado), acierto_ultima
'''

#verificando si letra está en la palabra
def verificar_letra_palabra(ultima_letra=None,palabra_secreta='', letras_usadas=[]):

    resultado=[]
    acierto_ultima = False

    # Convertimos a minúsculas para comparación sin distinción de mayúsculas
    palabra_secreta = palabra_secreta.lower()
    letras_usadas = {letra.lower() for letra in letras_usadas}

    if ultima_letra:
        ultima_letra = ultima_letra.lower()
        acierto_ultima = ultima_letra in palabra_secreta

    for letra in palabra_secreta:
        if letra in letras_usadas:
            resultado.append(letra.upper())  # Mostramos letras adivinadas en mayúsculas
        else:
            resultado.append('_')

    return ' '.join(resultado), acierto_ultima

def gestionando_vidas(vidas,se_encontro):
    if(se_encontro):
        return vidas
    else:
        vidas-=1
        return vidas

def perdio(vidas):
    if(vidas==0):
        print('Perdiste')
        return True
    else:
        print(f'Te quedan {vidas} vidas')
        return False

def gano(coincidencias):
    if('_' in coincidencias):
        return False
    else:
        print('Ganaste!')
        return True




#arreglo letras usadas
letras_usadas = []
#vidas iniciales
vidas=6
#variable perdio
usuario_perdio=False
#coincidencias
coincidencias=[]
#usuario gano
usuario_gano=False


#llamando palabra al azar
palabra= palabra_azar()
print(palabra)
#llamando mostrar guiones
mostrar_guiones(palabra)

#VA EN WHILE
while(not usuario_perdio and not usuario_gano):
    coincidencias_nuevas = list(coincidencias)
    #pidiendo letra a usuario
    letra_ingresada = pedir_letra_usuario(letras_usadas)
    #verificando si letra está en la palabra
    coincidencias,se_encontro = verificar_letra_palabra(letra_ingresada,palabra,letras_usadas)
    print(coincidencias)
    #Gestionando vidas
    vidas = gestionando_vidas(vidas,se_encontro)
    #comprobando si perdio
    usuario_perdio = perdio(vidas)
    #comprobando si gano
    usuario_gano=gano(coincidencias)








