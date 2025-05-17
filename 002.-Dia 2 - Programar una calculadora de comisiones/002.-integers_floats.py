#creating variable mi_numero
mi_numero = 1 +3
print(mi_numero + mi_numero)

#inspecting variable type
print(type(mi_numero)) #<class 'int'> -> Integer

#overwritting minumero
mi_numero = 5.8
print(type(mi_numero)) #<class 'float'> ->float


#Example 2
edad = input('Dime tu edad: ') #always string
print('Tu edad es: ' +  edad )
print(type(edad)) #<class 'str'>

nueva_edad = 1+edad #error we must make conversions between types
print('vas a cumplir ' + nueva_edad)