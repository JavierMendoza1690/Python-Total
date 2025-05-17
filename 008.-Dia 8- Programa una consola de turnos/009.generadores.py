
#Definiendo una funcion
def mi_funcion():
    return 4

#definiendo generador
def mi_generador():
    yield 4                 #produce el 4 justo cuando se le pide

print(mi_funcion())         #4
print(mi_generador())       #<generator object mi_generador at 0x00000225B0BA6400>

#almacenando funcion generadora en una variable
g = mi_generador()

#imprimiendo
print('valor almacenado en g:', next(g))    #valor almacenado en g 4
#print('valor almacenado en g:', next(g))    #Error ya que solo genera un solo numero