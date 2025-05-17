
#Primer ejemplo del if
if (10 > 9):
    #solo se imprime si se cumple la condicion (debe existir la tabulacion)
    print('Es correcto')

#Segundo ejemplo de if
if( True ):
    #entrará siempre, porque if(True) es la condicion para entrada
    print('Es Correcto 2')

#Ejemplo if 3
if( 5==2 ):
    #No estrará porque la condicion 5==2 es Falsa
    print('Es Correcto 3')
else:
    print('No es correcto 3')


#---------------------EJEMPLO 4-------------------
mascota = 'perro'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota =='pez':
    print('Tienes un pez')
else:
    print('No sé que animal tienes')


#---------------------EJEMPLO 5--------------------
edad = 16
calificacion = 9

if edad < 18:
    print('Eres menor de edad')
    if(calificacion >= 7):
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')
