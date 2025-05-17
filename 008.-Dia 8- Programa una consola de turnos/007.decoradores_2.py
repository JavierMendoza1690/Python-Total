

def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayuscula

    if tipo == 'min':
        return minuscula


def main():
    funcion_retorno = cambiar_letras('may')

    funcion_retorno('javier')

if __name__ == '__main__':
    main()