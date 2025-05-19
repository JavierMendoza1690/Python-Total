import re

clave = input('Clave: ')

#Debe empezar por una letra y tener seis caracteres alfanumericos
patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)


'''
    si el match no cumple   -->   chequear retorna None
    si el match cumple      -->   chequear retorna por ejemplo <re.Match object; span=(0, 8), match='daswfawe'>
'''
print(chequear)