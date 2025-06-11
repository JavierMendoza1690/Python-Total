import bs4
import requests

resultado = requests.get("https://www.escueladirecta.com/l/products?sortKey=created_at&sortDirection=asc&page=1")


sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')

imagenes = sopa.select('.ProductImage')[0]['src']

print(imagenes)

#segunda peticion con la url de la imagen
imagen_curso_1 = requests.get(imagenes)

#tomando la imagen
#print(imagen_curso_1.content)


#guardando imagenes
#wb --> escribir binario
f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()


