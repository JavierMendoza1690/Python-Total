import  shutil
'''
    comprimiendo con shutil
'''
carpeta_origen = 'Carpeta Superior'

archivo_destino = 'Todo comprimido'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)