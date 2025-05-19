import  re

texto = "Si necesitas ayuda llama al (658) - 598 - 9977 las 24 horas al servicio de ayuda online"

patron = 'ayuda'

#Buscando patron (expresion regular) en el texto
busqueda = re.search(patron, texto)

print(busqueda)             #<re.Match object; span=(13, 18), match='ayuda'>

#ubicacion de donde comienza y termina la palabra (la primera encontrada)
print(busqueda.span())      #(13, 18)

#donde empieza la palabra
print(busqueda.start())     #13

#donde termina la palabra
print(busqueda.end())       #18

#------------BUSCANDO TODAS LAS COINCIDENCIAS-----------------
print('\nTODAS LAS COINCIDENCIAS\n')

busqueda2 = re.findall(patron, texto)
print(busqueda2)                        #['ayuda', 'ayuda']

#finditer
print(re.finditer(patron, texto))       #<callable_iterator object at 0x0000015ED574A8F0>
print()

#forma de imprimir con finditer
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())