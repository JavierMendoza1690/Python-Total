monedas = 5

#ciclo while
while(monedas>0):
    print(f'tengo {monedas} monedas')
    monedas -= 1
else:
    print('no tengo más dinero')

#------------------EJEMPLO 2----------------------
respuesta = 's'

while(respuesta=='s'):
    respuesta = input('Quieres seguir?: ')
else:
    print('Gracias')

#----------------PASS---------------------------
#pass es no hacer nada... se detiene el programa en ese punto
respuesta = 's'

#while(respuesta=='s'):
#    pass

#print('Aqui no llega')

#----------------BREAK--------------------------
#Interrumpe y termina el loop

nombre = input('Ingresa tu nombre: ')

for letra in nombre:

    if(letra=='r'):
        print('Se interrumpió el ciclo')
        break #interrumpe el ciclo
    print(letra)

print('Fuera del ciclo')

#----------------CONTINUE--------------------------
#No interrumpe el loop, solo interrumple la iteracion actual, pasando a la siguiente iteracion

nombre = input('Ingresa tu nombre: ')

for letra in nombre:

    if(letra=='r'):
        print('Se interrumpió el ciclo')
        continue #Pasa a la siguiente iteracion
    print(letra)

print('Fuera del ciclo')




