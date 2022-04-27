import requests
from bs4 import BeautifulSoup

resultado = requests.get('https://eltiempo.com')
# print(resultado)

s = BeautifulSoup(resultado.text, 'lxml')

# print(s.find('div', attrs={'class': 'board-articles'}))
# print(s.find('div', attrs={'class': 'board-articles'}).find_all('a'))

secciones = s.find('div', attrs={'class': 'board-articles'}).find_all('a')

# seccion = secciones[1]
# print(seccion.get_text())

# print(s.prettify())

# print(resultado.headers)
# print(resultado.text)

titulos = [seccion.get_text() for seccion in secciones]
print(titulos)
print(type(titulos))