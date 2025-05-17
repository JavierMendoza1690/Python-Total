#1.-Verificando que los strings son inmutables
nombre = "Carina"

#tratando de mutar el string
#nombre[0] = 'K'  #Error

#2.-Pueden ser concatenados
n1="Kari"
n2="na"

print(n1+n2)

#3.-los strings se pueden multiplicar
print(n1*2) #KariKari

#4.-Pueden contener varias lineas de codigo sin necesidad de \n
poema ="""
mil pequeños peces blancos
coomo si hirviera el color del agua"""

print(poema)

#5.-Verificando si existe la palabra agua en el texto
print("agua" in poema)

#6.-Verificar el largo de un string
print(len(poema))