
#Creando listas
#NOTA: si hay una lista con mas elementos que otra agruapará los campos hasta que la cadena mas corta lo permita
nombres = ['Ana','Hugo','Valeria']
edades  = [65,29,24,30]
ciudades = ['Lima', 'Madrid', 'Mexico']

#creando nueva variable y usando zip
combinados = zip(nombres,edades)

#imprimiendo combinados
print(combinados)           #<zip object at 0x0000013EE61E1C00>

#para visualizarlo de forma adecuada debemos hacer un casting
combinados = list(combinados)
print(combinados)           #[('Ana', 65), ('Hugo', 29), ('Valeria', 24)]

#-----------------------------COMBINANDO 3 LISTAS--------------------------------
combinados_2 = list(zip(nombres,edades,ciudades))
print(list(combinados_2))   #[('Ana', 65, 'Lima'), ('Hugo', 29, 'Madrid'), ('Valeria', 24, 'Mexico')]

#--------------------------IMPRIMIR CADA ELEMENTO DE NUESTRAS LISTAS------------------------
print('\n')
for nombre,edad,ciudad in combinados_2:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')
