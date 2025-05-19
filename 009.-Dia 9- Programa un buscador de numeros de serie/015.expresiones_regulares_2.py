import re

texto = 'llama al 564-522-6588 ya mismo'

#sin cuantificadores
patron = r'\d\d\d-\d\d\d-\d\d\d\d'

#con cuantificadores
patron_2 = r'\d{3}-\d{3}-\d{3}'


resultado = re.search(patron, texto)

print(resultado)                    #<re.Match object; span=(9, 21), match='564-522-6588'>

print(resultado.group())            #564-522-6588
