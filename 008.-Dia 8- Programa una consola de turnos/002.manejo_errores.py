def suma():
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    print(n1 + n2)
    print('Gracias por sumar' + n1)

#Modo de manejar errores


def main():
    '''
    try:
        # Codigo que queremos probar
    except:
        #Codigo a ejecutar si hay un error
    else:
        # Codigo a ejecutar si no hay error
    finally:
        #Codigo que se va a ejecutar de todos modos

    Solo se entra a un except y no ambos
    '''

    try:
        suma()
    except ValueError:
        print('Ese no es un numero')
    except TypeError:
        print('Estas intentando concatenar tipos distintos')
    else:
        print('Hiciste todo bien')
    finally:
        print('Eso fue todo')

if __name__ == '__main__':
    main()


