def pedir_numero():

    while True:
        try:
            numero = int(input('Dame un numero: '))
        except:
            print('Ese no es un numero')
        else:
            print(f'Ingresaste el numero {numero}')
            break

    print('Gracias')

def main():
    pedir_numero()

if __name__ == '__main__':
    main()
