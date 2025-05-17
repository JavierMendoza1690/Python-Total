import os
import shutil



#Creando un archivo
'''
archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

print(os.getcwd())
'''

#shutil.move se encarga de mover un archivo de un directorio a otro
shutil.move('curso.txt', "C:\\Users\\Javier\\Desktop")  #moviendo archivo a escritorio

#ELIMINAR ARCHIVOS
'''
    os.unlink:                  elimina un archivo en una ruta que le proveas
    os.rmdir (remove dictory):  elimina una carpeta vacia
    shutil.rmtree:              elimina la carpeta seleccionada con todo su contenido interno
    
    hay otras alternativas gratuitas como:
    send2trash
'''

