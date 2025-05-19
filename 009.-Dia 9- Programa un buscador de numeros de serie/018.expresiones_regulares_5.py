import re

texto = "No atendemos los lunes por la tarde"

#patron = r'lunes|martes'

#el punto es un comodin que significa tomara una letra antes de la coincidencia
patron = r'.demos'

# el ^ fuerza que tiene que ser al comienzo de la cadena
patron_2 = r'^\D'       #no hay un digito (numero) al inicio de la cadena

# el $ fuerza al final de la cadena
patron_3 = r'\D$'       #no hay un digito al final de la cadena

# [^here] excluye lo que se ponga justo despues de ^
patron_3 = r'[^\s]'     #toma lo que sea un espacio en blanco

# [^here] excluye lo que se ponga justo despues de ^
patron_4 = r'[^\s]'     #toma lo que sea un espacio en blanco

# [^here] excluye lo que se ponga justo despues de ^
patron_5 = r'[^\s]+'     #toma lo que sea un espacio en blanco

buscar = re.search(patron,texto)
buscar_2 = re.search(patron_2,texto)
buscar_3 = re.search(patron_3,texto)
buscar_4 = re.findall(patron_4, texto)
buscar_5 = re.findall(patron_5,texto)

print(buscar)           #<re.Match object; span=(17, 22), match='lunes'>
print(buscar_2)         #<re.Match object; span=(0, 1), match='N'>
print(buscar_3)         #<re.Match object; span=(34, 35), match='e'>
print(buscar_4)         #['N', 'o', 'a', 't', 'e', 'n', 'd', 'e', 'm', 'o', 's', 'l', 'o', 's', 'l', 'u', 'n', 'e', 's', 'p', 'o', 'r', 'l', 'a', 't', 'a', 'r', 'd', 'e']
print(buscar_5)         #['No', 'atendemos', 'los', 'lunes', 'por', 'la', 'tarde']