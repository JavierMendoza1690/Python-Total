import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

print(type(resultado))                  #<class 'requests.models.Response'>

#print(resultado.text)                  #retorna todoo el html y css en formato string

sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')

#buscando la etiqueta title en el html. devuelve una lista
print(sopa.select('title')[0].getText())    #Escuela Directa | Blog