import zipfile

'''
    El primer argumento de ZipFile() es el nombre que tendra el comprimido
    El segundo parametro es el modo de apertura
'''
mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')

#eligiendo los archivos que van dentro del comprimido
mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

#cerrando el zip (Creandolo)
mi_zip.close()