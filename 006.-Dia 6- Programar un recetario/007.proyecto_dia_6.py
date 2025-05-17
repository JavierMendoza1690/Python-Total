from pathlib import Path
from os import system
import shutil

def dar_bienvenida():
    '''
    Esta funcion da la bienvenida al usuario
    '''

    print("¡Bienvenido al Sistema de Recetas!")
    print("Este programa muestra la ubicación de tus recetas y cuántas hay en cada categoría.")

def obtener_direccion_recetas():
    '''
    Esta funcion retorna la ruta de acceso a las recetas
    :return ruta recetas:
    '''
    #obteniendo la ruta absoluta de las recetas
    ruta_recetas = Path('./007.-Recetas').absolute()

    return  ruta_recetas

def contar_recetas_dentro_carpeta(ruta_principal):
    """
    Cuenta los archivos .txt en cada subdirectorio usando pathlib.

    Args:
        ruta (Path): Objeto Path que representa el directorio principal

    Returns:
        dict: Diccionario con {nombre_categoria: cantidad_recetas}
    """
    #creando un diccionario vacío
    categorias = {}

    # Iteramos sobre los elementos en el directorio principal
    for item in ruta_principal.iterdir():
        # Verificamos si es un directorio
        if item.is_dir():
            # Contamos archivos .txt usando glob
            txt_count = len(list(item.glob('*.txt')))
            #item.name retorna la ultima parte de la ruta que esta en item
            #creando un diccionario
            categorias[item.name] = txt_count

    return categorias

def mostrar_cantidad_recetas_categoria(diccionario_recetas):
    '''
    muestra la cantidad de recetas que hay por cada categoria
    en las rutas existentes
    :param diccionario_recetas (nombre_directorio: cantidad_recetas_directorio):
    :return null:
    '''

    contenido = {}
    i=1
    print("Cantidad de recetas por categoría:")
    for categoria, cantidad in diccionario_recetas.items():
        print(f"{i}- {categoria}: {cantidad} recetas (.txt)")
        i+=1

    #total = sum(diccionario_recetas.values())
    #print(f"\nTotal de recetas: {total}")

def leer_menu_interno(ruta,mensaje):
    i=0
    system('cls')
    diccionario = {}
    for txt in Path(ruta).glob('*.txt'):
        print(f'{i+1} {txt.name}')
        diccionario[i]=txt.name
        i+=1

    seleccion = int(input(mensaje))
    match seleccion:
        case 1:
            nueva_ruta = Path(ruta,diccionario[0])
            return nueva_ruta
        case 2:
            nueva_ruta = Path(ruta, diccionario[1])
            return nueva_ruta
        case _:
            print('Ruta invalida')

def leer_archivo(ruta):
    #abriendo el archivo con pathlib
    contenido = Path(ruta).read_text()
    print(contenido)

def crear_receta(nombre_receta, contenido_receta,ruta):
    nombre_archivo = f'{nombre_receta}.txt'
    ruta_archivo = Path(ruta,nombre_archivo)

    ruta_archivo.write_text(contenido_receta,encoding='utf-8')

def crear_categoria(ruta_principal,nombre_carpeta):
    system('cls')
    ruta_carpeta = Path(ruta_principal,nombre_carpeta)
    ruta_carpeta.mkdir(exist_ok=True)
    return ruta_carpeta

def eliminar_receta(ruta_eliminar):
    Path(ruta_eliminar).unlink()
    print(f'{ruta_eliminar.name} fue eliminada')

def eliminar_directorio(ruta_eliminar):
    try:
        ruta_eliminar.rmdir()  # Solo elimina si está vacío
        print(f"Directorio vacío '{ruta_eliminar.name}' eliminado.")
    except FileNotFoundError:
        print(f"El directorio '{ruta_eliminar.name}' no existe.")
    except OSError as e:
        print(f"No se pudo eliminar '{ruta_eliminar.name}' (¿Tiene archivos dentro?)")

def menu(ruta_principal,diccionario_principal):
    input('Presione enter para continuar')
    system('cls')
    print('[1]- leer receta')
    print('[2]- crear receta')
    print('[3]- crear categoria')
    print('[4]- eliminar receta')
    print('[5]- eliminar categoria')
    print('[6]- finalizar programa')
    opcion = int(input('Ingrese su opcion'))
    match opcion:
        case 1:
            system('cls')
            mostrar_cantidad_recetas_categoria(diccionario_principal)
            categoria = int(input('Que categoría quiere elegir?'))
            nueva_ruta = leer_menu_interno(list(ruta_principal.iterdir())[categoria-1],'Elige la receta que quiere leer')
            leer_archivo(nueva_ruta)

        case 2:
            system('cls')
            mostrar_cantidad_recetas_categoria(diccionario_principal)
            categoria = int(input('Que categoría quiere elegir?'))
            ruta_carpeta =list(ruta_principal.iterdir())[categoria-1]
            nombre_receta =     input('Elija nombre receta')
            contenido_receta =  input('contenido_receta')
            crear_receta(nombre_receta,contenido_receta,ruta_carpeta)
        case 3:
            system('cls')
            nombre_categoria = input('Ingrese el nombre de la categoria que quiere crear')
            crear_categoria(ruta_principal,nombre_categoria)
        case 4:
            system('cls')
            mostrar_cantidad_recetas_categoria(diccionario_principal)
            categoria = int(input('Que categoría quiere elegir?'))
            ruta_eliminar = leer_menu_interno(list(ruta_principal.iterdir())[categoria - 1], 'Que categoria quiere eliminar?')
            eliminar_receta(ruta_eliminar)
        case 5:
            system('cls')
            mostrar_cantidad_recetas_categoria(diccionario_principal)
            categoria = int(input('Que categoría quiere eliminar?'))
            ruta_directorio_eliminar= list(ruta_principal.iterdir())[categoria - 1]
            eliminar_directorio(ruta_directorio_eliminar)
        case _:
            print('no es caso 1')
#Funcion principal main
def main():
    system('cls')
    #invocando bienvenida
    dar_bienvenida()

    try:
        # obteniendo ruta principal recetas
        ruta_recetas = obtener_direccion_recetas()

        #verificando que la ruta de recetas exista
        if not ruta_recetas.exists():
            raise FileNotFoundError(f"No se encontró el directorio: {ruta_recetas}")

        print(f"\nTus recetas se encuentran en: {ruta_recetas}\n")

        #incovando contar_recetas_dentro_carpeta
        diccionario_recetas = contar_recetas_dentro_carpeta(ruta_recetas)
        # Mostramos resultados
        mostrar_cantidad_recetas_categoria(diccionario_recetas)
        # Desplegando Menu
        menu(ruta_recetas, diccionario_recetas)
    except FileNotFoundError as e:
        print(f"Error: {e}")

#Invocando funcion principal
if __name__ == "__main__":
    main()