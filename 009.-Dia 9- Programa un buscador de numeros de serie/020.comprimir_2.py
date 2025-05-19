import zipfile

#ubicando zip en modo lectura
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip','r')

zip_abierto.extractall()
