from pathlib import Path, PureWindowsPath

carpeta = Path('/006.-Dia 6- Programar un recetario/carpeta_alternativa/otro_archivo.txt')


#Nota: con pathlib no hace falta abrir ni cerrar el archivo, él lo hace automaticamente

#READ_TEXT(): abre el archivo en modo lectura (r)
print(carpeta.read_text()) #Ivonne galeano

#NAME: retorna el nombre del archivo que se esta abridno
print(carpeta.name) #otro_archivo.txt

#SUFFIX: retorna la extension del archivo que se abre
print(carpeta.suffix) #.txt

#STEM: retorna el nombre del archivo sin la extension #otro_archivo
print(carpeta.stem) #otro_archivo

#EXIST: retorna true si el archivo en la ruta especificada existe
print(carpeta.exists())

#se suele usar de la siguente forma
if not carpeta.exists():
    print('El archivo no existe')
else:
    print('Genial')

#--------USANDO PUREWINDOWSPATH------

ruta_windows= PureWindowsPath(carpeta)
# retorna la ruta completa de windows con barras invertidas para que se adapte al formato de windows
print(ruta_windows)  #C:\Users\Javier\Documents\001.-Programacion\001.-Dias Python Total\006.-Dia 6- Programar un recetario\carpeta_alternativa\otro_archivo.txt