#creting variable
texto = "ABCDEFGHIJKLM"

#fragmentando texto
fragmento = texto[2:5]

#printing
print(fragmento) #CDE

#fragmentando desde 2 al final
fragmento = texto[2:]
print(fragmento) #CDEFGHIJKLM

#fragmentando desde el inicio hasta el 5
fragmento = texto[:5]
print(fragmento) #ABCDE

#fragmentando cada 2 caracteres
fragmento = texto[2:10:2]
print(fragmento) #CEGI

#fragmentar una letra cada 3 caracteres
fragmento = texto[::3]
print(fragmento) #ADGJM

#formar cadena al reves
fragmento = texto[::-1]
print(fragmento) #MLKJIHGFEDCBA