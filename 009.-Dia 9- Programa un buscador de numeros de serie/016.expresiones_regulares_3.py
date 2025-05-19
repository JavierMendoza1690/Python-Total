import re

texto = 'llama al 564-522-6588 ya mismo'

#compilando con cuantificadores
patron = re.compile(r'(\d{3})-(\d{3})-(\d{3})')

resultado = re.search(patron, texto)

print(resultado.group(2))       #522