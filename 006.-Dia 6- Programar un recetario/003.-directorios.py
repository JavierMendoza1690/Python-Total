# --------------------------IMPORTANDO MODULOS------------------------------
#importando os (operative system)
import os
from pathlib import Path  #Path va en mayusculas porque es un objeto

#----------------------------------------OS.GETCWD-----------------------------------------------
#obteniendo directorio de ruta de trabajo actual(current working directory)
ruta = os.getcwd()

print(ruta)  #C:\Users\Javier\Documents\001.-Programacion\001.-Dias Python Total\006.-Dia 6- Programar un recetario



#----------------------------------------OS.CHDIR-----------------------------------------------
#change dir(cambiar de directorio)
#simula que estamos en otra carpeta para poder abrir archivos sin problemas
ruta_distinta = os.chdir('/006.-Dia 6- Programar un recetario\\carpeta_alternativa')

#abriendo archivo en nueva ruta
archivo = open('otro_archivo.txt')
#print(archivo)
print(archivo.read())

#----------------------------------------OS.MAKEDIRS-----------------------------------------------
#crea una carpeta nueva en la ruta especificada
ruta_makedirs = os.makedirs('/006.-Dia 6- Programar un recetario\\carpeta_alternativa\\otra_carpeta')
#la linea anterior crea una carpeta nueva si no existe (llamada otra carpeta) si no existe genera un error

#----------------------------------------- #SEPARANDO RUTA -------------------------------------------------
ruta = 'C:\\Users\\Javier\\Documents\\001.-Programacion\\001.-Dias Python Total\\006.-Dia 6- Programar un recetario\\prueba.txt'

#Toma la parte de la ruta del elemento a ejecutar
elemento    = os.path.basename(ruta)
elemento2   = os.path.dirname(ruta)

print(elemento)     #prueba.txt
print(elemento2)    #C:\Users\Javier\Documents\001.-Programacion\001.-Dias Python Total\006.-Dia 6- Programar un recetario

#obtener ambos elementos separados en una tupla
elemento3 = os.path.split(ruta)
print(elemento3)    #('C:\\Users\\Javier\\Documents\\001.-Programacion\\001.-Dias Python Total\\006.-Dia 6- Programar un recetario', 'prueba.txt')

#----------------------------------------- #ELIMINAR DIRECTORIO -------------------------------------------------
#elimina la carpetaen la ruta seleccionada (la ultima parte es el nombre de la carpeta)
#si no consigue la carpeta arroja un error
os.rmdir('/006.-Dia 6- Programar un recetario\\carpeta_alternativa\\otra_carpeta')

#------------------------------------- #ABRIR ARCHIVO CARPETA DISTINTA FORMA TRADICIONAL ----------------------------------------------
#genera un error en mac
otro_archivo = open('/006.-Dia 6- Programar un recetario\\carpeta_alternativa\\otro_archivo.txt')

print(otro_archivo.read())

#------------------------------------- #USANDO MODULO PATH DE PATHLIN ----------------------------------------------
#Al usar el objeto Path deben usarse nuevamente las barras normales para evitar errores (/)

carpeta = Path('/006.-Dia 6- Programar un recetario/carpeta_alternativa')

# la siguiente linea es ejecutable tanto para windows como para MAC
archivo_path = carpeta / 'otro_archivo.txt'   #concatenacion especial de rutas

#Abriendo archivo
mi_archivo_path = open(archivo_path)
print(mi_archivo_path.read())