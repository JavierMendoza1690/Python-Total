import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")


sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')

parrafo_especial = sopa.select('a')

print(parrafo_especial[99].getText())       #Con la tecnología de Blogger
