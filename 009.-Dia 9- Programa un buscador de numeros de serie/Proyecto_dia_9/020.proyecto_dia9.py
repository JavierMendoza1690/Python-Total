import os
import re
from datetime import datetime
import time

def buscar_numeros_serie(directorio_raiz):

    # Iniciar temporizador
    inicio = time.time()

    # Obtener fecha actual formateada
    fecha_actual = datetime.now().strftime("%d/%m/%y")


    # Compilar patrón de expresión regular para números de serie:
    # N + 3 letras (mayúsculas o minúsculas) + guión + 5 dígitos
    patron = r'N\D{3}-\d{5}'
    patron_serie = re.compile(patron)

    # Lista para almacenar los resultados encontrados
    resultados = []

    # Recorrer el árbol de directorios usando os.walk()
    # raiz: directorio actual
    # _: lista de subdirectorios (no se usa, por eso el _)
    # archivos: lista de archivos en el directorio actual

    for raiz, dirs, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            # Procesar solo archivos con extensión .txt
            if archivo.endswith('.txt'):
                # Construir ruta completa al archivo
                ruta_completa = os.path.join(raiz, archivo)
                try:
                    # Intentar abrir el archivo con codificación UTF-8 (la más común)
                    with open(ruta_completa, 'r', encoding='utf-8') as f:
                        # Leer todoo el contenido del archivo
                        contenido = f.read()
                        # Buscar coincidencia con el patrón de número de serie
                        coincidencia = patron_serie.search(contenido)

                        if coincidencia:
                            # Si se encuentra, agregar a resultados (nombre archivo y número)
                            resultados.append((archivo, coincidencia.group()))

                except UnicodeDecodeError:
                    print('Error')
                    pass

    # Calcular tiempo transcurrido desde el inicio de la búsqueda
    duracion = time.time() - inicio

    # Redondear hacia arriba el tiempo de ejecución
    duracion_redondeada = int(duracion) + (1 if duracion % 1 > 0 else 0)

    # Mostrar resultados en formato de tabla
    print("-" * 50)  # Línea separadora
    print(f"Fecha de búsqueda: {fecha_actual}\n")
    # Encabezados de la tabla
    print("ARCHIVO\t\t\tNRO. SERIE")  # \t para tabulación
    print("------------\t--------------")

    # Imprimir cada resultado encontrado
    for archivo, numero in resultados:
        print(f"{archivo}\t{numero}")

    # Resumen de la búsqueda
    print(f"\nNúmeros encontrados: {len(resultados)}")
    print(f"Duración de la búsqueda: {duracion_redondeada} segundos")
    print("-" * 50)  # Línea separadora final


# Uso del programa
if __name__ == "__main__":

    directorio = "Mi_Gran_Directorio"


    buscar_numeros_serie(directorio)