#funcion tradicional
def suma(a,b):
    return a+b

#print(suma(5,6,3)) #error porque deben ser solo dos argumentos

#-------------------FUNCIONES CON ARGUMENTOS INDEFINIDOS------------------------

def suma_2(*args):
    total = 0
    for arg in args:
        total+=arg

    return total

# se puede enviar cualquier cantidad de argumentos
print(suma_2(1,2))
print(suma_2(1,2,3,4,1))

#-------------------MODO SIMPLIFICADO DE LA FUNCION ANTERIOR------------------------

def suma_3(*args):
    return(sum(args))

# se puede enviar cualquier cantidad de argumentos
print(suma_3(1,2))
print(suma_3(1,2,3,4,1))