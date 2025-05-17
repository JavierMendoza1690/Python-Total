#Creando booleanos forma dierecta
var1= True
var2= False

#Creando booleans de forma indirecta
numero = (5 >= 2+3)



#--------------------------CODIGO------------------------
#print tipo de dato booleano
print(type(var1)) #<class 'bool'>

#print numero tipo de numero
print(type(numero)) #<class 'bool'>
#imprimiendo numero
print(numero)

#la expresion bool sirve para forzar y hacer explicito el resultado de un booleano
numero2 = bool(5>3) #se forza explicitamente al resultado booleano, si se deja bool() sin argumento da falso
print(numero2)



#---------------------BOOLEANOS EN LISTAS--------------------------
#Creando lista
lista = [1,2,3,4,5]
control = 2 in lista
print(f'Control = {control}')
