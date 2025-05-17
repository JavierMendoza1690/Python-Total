#declaring variables
mi_texto= "Esta es una prueba"

#resultado = mi_texto[0] #E
resultado = mi_texto[9] #n

#searching letter
resultado = mi_texto.index('a')

#can search entire words (is key sensitive)
resultado = mi_texto.index('prueba')

#tiene parametros opcionales
resultado = mi_texto.index('a',5) #busca a partir del 5 caracter
#resultado = mi_texto.index('a',5,10) #busca a partir del 5 caracter hasta el decimo sin incluirlo


#METODO RINDEX
#similar a index pero busca de derecha a izquierda
resultado = mi_texto.rindex('a') #17


print(resultado)