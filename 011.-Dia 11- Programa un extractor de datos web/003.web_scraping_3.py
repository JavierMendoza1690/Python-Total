import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")


sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')

parrafo_especial = sopa.select('.post-title div')

for p in parrafo_especial:
    print(p.getText())


