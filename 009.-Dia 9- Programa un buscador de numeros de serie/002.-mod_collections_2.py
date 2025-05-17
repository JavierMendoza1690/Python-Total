from collections import Counter

#asignamos la clase counter a una variable
serie = Counter([1,1,1,1,2,2,3,3,3,3,3,3,3,4])


'''
metodo most_common retorna los elementos mas comunes
en forma de una lista de tuplas
'''
print(serie.most_common())  #[(3, 7), (1, 4), (2, 2), (4, 1)]
print(serie.most_common(1)) #[(3, 7)]
print(serie.most_common(2)) #[(3, 7), (1, 4)]

#Podemos castear el objeto serie para retornar los elementos unicos de una lista

print(list(serie))          #[1, 2, 3, 4]