
#abriendo archivo
mi_archivo = open('001.-prueba.txt')

'''
si se ejecuta una lectura el cursor queda al final del archivo,
al tratar de hacer otra consecutiva no arrojará nada
ya que el cursor está al final

NOTA IMPORTANTE: cuando se lee una linea o un documento se mueve la ubicacion de lectura 
es decir, si se lee una linea del archivo el cursor se posiciona en la segunda linea para
posteriores lecturas. es importante tener en cuenta donde está el cursor todo el tiempo
'''

#forma incorrecta de leer un archivo
print(mi_archivo) #<_io.TextIOWrapper name='001.-prueba.txt' mode='r' encoding='cp1252'>

#--------------------------LEYENDO DE TODO EL DOCUMENTO TOTAL ----------------------------

#metodo que sirve para leer el archivo (forma correcta)
#print(mi_archivo.read())   #Soy la primera linea
                            #Â¡Vaya! Â¡Yo soy la segunda!
                            #He quedado tercera

#--------------------------LEYENDO DE LINEA A LINEA----------------------------

#leyendo una sola linea del archivo rstrip quita el salto de linea en un print
#print(mi_archivo.readline().rstrip()) #Soy la primera linea
#print(mi_archivo.readline().rstrip()) #Â¡Vaya! Â¡Yo soy la segunda!
#print(mi_archivo.readline().rstrip()) #He quedado tercera

#--------------------------INTERANDO ENTRE LAS LINEAS DE UN ARCHIVO----------------------------
# no se necesita readline ni funciones adicionales

#for linea in mi_archivo:
#    print(f'Aqui dice: '+ linea)

#---------------------------------USANDO METODO READLINES -------------------------------------
#genera una lista donde cada elemento de la lista es una linea del archivo
#solo recomendable para archivos pequeños
todas_las_lineas= mi_archivo.readlines()
print(todas_las_lineas)

#-------------------------------CERRANDO EL ARCHIVO (RECOMENDACION)----------------------------
mi_archivo.close()
