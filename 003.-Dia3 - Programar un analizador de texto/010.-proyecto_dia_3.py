
texto_analizar = input(' Por favor ingrese el texto que desea analizar: ')
#transformando texto a lower_case
texto_analizar = texto_analizar.lower()

#Solicitando ingresar tres letras
letra_1 = input('Por favor ingrese la letra 1 a buscar: ').lower()
letra_2 = input('Por favor ingrese la letra 2 a buscar: ').lower()
letra_3 = input('Por favor ingrese la letra 3 a buscar: ').lower()

print(letra_1, letra_2, letra_3)

#1.- Almacenando numero de veces de cada letra en el texto
numero_veces_letra_1 = texto_analizar.count(letra_1)
numero_veces_letra_2 = texto_analizar.count(letra_2)
numero_veces_letra_3 = texto_analizar.count(letra_3)

print(f'La letra {letra_1} se encuentra {numero_veces_letra_1} en el texto')
print(f'La letra {letra_2} se encuentra {numero_veces_letra_2} en el texto')
print(f'La letra {letra_3} se encuentra {numero_veces_letra_3} en el texto')

#2.-¿Cuantas palabras hay en el texto?

#creando una lista con el texto a analizar
lista_texto_analizar = texto_analizar.split()
#calculando el numero de divisiones de la nueva lista
numero_palabras = len(lista_texto_analizar)

print(f'el numero de palabras del texto ingresado es {numero_palabras}')

#3.-¿Cual es la primera y la ultima letra del texto?

#primera letra
print(f'La primera letra del texto es {texto_analizar[0]}')
#ultima letra
print(f'La ultima letra del texto es {texto_analizar[-1]}')

#4.-¿Como queda el texto si invertimos las palabras?
#invirtiendo la lista creada
texto_invertido_lista = lista_texto_analizar[::-1]

#uniendo la lista creada
texto_invertido = " ".join(texto_invertido_lista)

#imprimiendo lista invertida
print(texto_invertido)

#5.-Buscando la palabra Python en el texto
palabra_python = 'python' in texto_analizar

print(palabra_python)

