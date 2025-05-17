#------------------------ABRIENDO ARCHIVO EN MODO R----------------------------------
archivo = open('002.-prueba.txt', 'r')

#Tratando de escribir en el nuevo archivo
#archivo.write('soy el nuevo texto')  #Error en modo de lectura r

#Cerrando archivo
archivo.close()

#------------------------ABRIENDO ARCHIVO EN MODO W----------------------------------

archivo = open('002.-prueba_1.txt', 'w')

#USANDO EL METODO WRITE
#el metodo write no agrega un salto de linea al final automaticamente (hay que usar \n)
archivo.write('soy el nuevo texto\n')  #crea la nueva linea con el texto entre comillas (modo w)
archivo.write('Hola mundo\n')

#FORMA 2 DE AGREGAR SALTOS DE LINEA
archivo.write('''soy el nuevo texto
hola mundo
''')

#USANDO EL METODO WRITELINES
#toma los elementos de una lista y las concatena todas juntas
archivo.writelines(['hola\n','mundo\n','aqui\n','estoy\n'])

#Cerrando archivo
archivo.close()

#------------------------ABRIENDO ARCHIVO EN MODO A----------------------------------

archivo = open('002.-prueba.txt', 'a')

#USANDO EL METODO WRITE
#el metodo write no agrega un salto de linea al final automaticamente (hay que usar \n)
archivo.write('\nbienvenido')

#Cerrando archivo
archivo.close()