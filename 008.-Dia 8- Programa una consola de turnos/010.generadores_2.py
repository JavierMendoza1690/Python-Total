
#GENERANDO Y RETORNANDO LISTA EN FUNCION NORMAL
def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x*10)

    return lista

# GENERANDO LISTA CON UNA FUNCION GENERADORA
def mi_generador():
    for x in range(1,5):
        yield x*10

def main():
    print(mi_funcion())             #[10, 20, 30, 40]
    print(mi_generador())           #<generator object mi_generador at 0x0000013BB6E5AA80>

    print(next(mi_generador()))     #10
    print(next(mi_generador()))     #10

    #guardando generador en una variable
    variable_generador = mi_generador()

    print(next(variable_generador)) #10
    print(next(variable_generador)) #20
    print(next(variable_generador)) #30
    print(next(variable_generador)) #40
    #print(next(variable_generador)) #Error



if __name__ == '__main__':
    main()