
#creando funcion
def suma(**kwargs):
    print(type(kwargs))     #devuelve un diccionario
    print(kwargs)           #{'x': 3, 'y': 5, 'z': 4}

suma(x=3,y=5,z=4) #todos los elementos deben ser homogeneos


#--------------------MODIFICANDO FUNCION--------------------
def suma_2(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        total+=valor
    return total

total = suma_2(x=3,y=5,z=4) #todos los elementos deben ser homogeneos
print(total)

#------------------FUNCION CON TODOS LOS TIPOS DE ARGUMENTOS--------------------

def prueba(num1,num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')

#invocando suma_3
args= [100,200,300,400,1,32]
kwargs= {'x':'1','y':'2','z':'3'}

#prueba(15,50,100,200,300,400,1,32, x='1',y='2',z='tres')
prueba(15,50,*args, **kwargs)