import numeros
from numeros import turno_perfumeria


generador_farmacia = numeros.turno_farmacia()

opcion = 0

while opcion != 4:
    print('\nElige el área a la que te diriges')
    print('1.-Perfumeria')
    print('2.-Farmacia')
    print('3.-Cosmeticos')
    print('4.-Salir')
    opcion = int(input('Opcion: '))

    match(opcion):
        case 1:
            numeros.decorar_turno('P')
            input('Enter para continuar')
        case 2:
            numeros.decorar_turno('F')
            input('Enter para continuar')
        case 3:
            numeros.decorar_turno('C')
            input('Enter para continuar')
        case _:
            print('Opcion invalida')