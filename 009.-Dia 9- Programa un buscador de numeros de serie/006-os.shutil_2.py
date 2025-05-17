import os
from send2trash import send2trash

#Envia el archivo puesto como path a la papelera de reciclaje
#send2trash('curso.txt')     #elimina curso.txt


#METODO WALK (metodo de la clase os)
'''
Recorre todos los directorios capetas y sub-carpetas en su camino cuando le das una ruta
actua como un generador similar a una funcion generadora
primero almacena la ruta en la que se encuentra
segundo la ruta de las subcarpetas
tercero almacena los archivos que esten en las carpetas
la ruta puede estar en cualquier lugar del ordenador con ruta absoluta
tambien admite rutas relativas


una tupla de 3 argumentos
'''

print(os.walk('Carpeta Superior'))  #<generator object walk at 0x000002064FD976E0>

#ruta = 'C:\\Users\\Javier\\Documents\\001.-Programacion\\001.-Python Total\\009.-Dia 9- Programa un buscador de numeros de serie\\Carpeta Superior'
ruta = 'Carpeta Superior'

for carpeta, subcarpeta, archivo in os.walk(ruta):

    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son: ')

    for sub in subcarpeta:
        print(f'\t{sub}')

    print('Los archivos son: ')

    for arch in archivo:
        if(arch.startswith('2015')):
            print(f'\tel siguiente archivo comienza con 2015: ')
        else:
            print(f'\tel siguiente archivo no comienza con 2015: ')
        print(f'\t{arch}')

    print('\n')



