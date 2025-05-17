#importando randint desde la libreria random
from random import *
#NOTA IMPORTANTE: El nombre del archivo .py no debe llamarse igual que la libreria de la que se importa


#----------------------------------------RANDINT--------------------------------------
#usando randint
#randint genera un numero aleatorio entre su primer y segundo argumento
print(randint(5,40))    #el sistema no reconoce a randint si no se importa


#----------------------------------------UNIFORM---------------------------------------

#uniform: genera un valor aleatorio comprendido entre el primer y segundo argumento
aleatorio_float = round(uniform(1,8),1)
print(aleatorio_float)

#----------------------------------------RANDOM---------------------------------------
#random() elige un numero decimal o float entre 0 y 1
aleatorio_random = random()
print(aleatorio_random)

#----------------------------------------CHOICE---------------------------------------
#permite trabajar con una seleccion aleatoria dentro de los elementos de una lista o cualquier otro coleccionable

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatrio_choice = choice(colores)
print("Choice",aleatrio_choice)

#----------------------------------------SHUFFLE---------------------------------------
#shuffle hace una mezcla aleatoria de las posiciones de la coleccion
#shuffle modifica diretamente la lista, (por referencia)
numeros = list(range(5,50,5)) #[5, 10, 15, 20, 25, 30, 35, 40, 45]

shuffle(numeros)  # [40, 45, 10, 15, 30, 25, 20, 5, 35] por ejemplo

print(numeros)