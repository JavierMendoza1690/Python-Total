from pathlib import Path #Path es un objeto



#-----------------------------PATH------------------------------------------------
'''
    construye una ruta de acceso con los argumentos que se envian
    el separador depende del sistema operativo
'''

guia = Path('Barcelona','Sagrada_familia.txt')
print(guia) #Barcelona\Sagrada_familia.txt

'''
    A este tipo de rutas se les llama rutas relativas porque toman como base la carpeta
    actual, se pueden entender como parte parcial de una ruta absoluta
    Las rutas absolutas parten desde C:\\users....
'''

#------------------------------PATH.HOME-------------------------------------

#devuelve ruta absoluta al directorio principal del usuario actual
base = Path.home()
print(base)

#ejemplo de ruta absoluta
guia_2 = Path(base,'Barcelona','Sagrada_familia.txt')

print(guia_2) #C:\Users\Javier\Barcelona\Sagrada_familia.txt

#la ruta de guia_2 no existe pero es un ejemplo de como formularlo

#------------------------------EJEMPLO 3 PATH------------------------------------------
'''Path acepta tanto a strings como Paths creados con anterioridad como argumento'''
base_3=Path.home()
guia_3 = Path(base_3,'Europa', 'España',guia)

'''with_name cambia solo la parte final de la ruta, es decir, el archivo destino'''
guia_4 = guia_3.with_name('La_Pedrera.txt')

print(guia_3) #C:\Users\Javier\Barcelona\Sagrada_familia.txt
print(guia_4) #C:\Users\Javier\Europa\España\Barcelona\La_Pedrera.txt

#----------------------------METODO PARENT----------------------------
#devuelve la ruta hasta el antecesor del final de la ruta creada

print(guia_4.parent)            #C:\Users\Javier\Europa\España\Barcelona
print(guia_4.parent.parent)     #C:\Users\Javier\Europa\España


#-----------------------------EJERCICIO CON CARPETAS PRECREADAS-------------------------------------
#C:\Users\Javier\Documents\001.-Programacion\001.-Dias Python Total\006.-Dia 6- Programar un recetario
guia_5 = Path(Path.home(),'Documents','001.-Programacion','001.-Dias Python Total','006.-Dia 6- Programar un recetario','Europa')

print('\n')
'''IMRPIME TODOS LOS DIRECTORIOS INMEDIATAMENTE DENTRO DE EUROPA, '''
for txt in Path(guia_5).glob('*.txt'):
    print(txt)

print('\n')
'''IMRPIME TODOS LOS DIRECTORIOS DENTRO DE EUROPA, AUNQUE ESTEN DENTRO DE OTRAS SUBCARPETAS '''
for txt in Path(guia_5).glob('**/*.txt'):
    print(txt)


#-----------------------------EJERCICIO RUTAS RELATIVAS(RELATIVE_TO)-------------------------------------
'''Arroja las rutas que estan dentro de la carpeta seleccionada'''

print('\n')

guia_6=Path('Europa','España','Barcelona','sagrada_familia.txt')
en_europa = guia_6.relative_to(Path('Europa'))
print('here')
en_espania = guia_6.relative_to(Path('Europa','España'))

print(en_europa)
print(en_espania)