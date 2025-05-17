#-------------------implicit conversion--------------------------

#declaring variables
num1=20
num2=20.5

#printing variables types
print(type(num1))
print(type(num2))

#-------------------explicit conversion--------------------------

num3= 5.8
print(type(num3))

#casting to int
num4 = int(num3)

print(num4)         # 5
print(type(num4))   #int


#-------------------Example-----------------------
edad = input('tell me your age: ')
edad = int(edad)

nueva_edad = 1 + edad;


print('Tu nueva edad es: ' + nueva_edad) #error no se puede concatener un string con un int de esta forma
