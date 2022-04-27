import requests
from bs4 import BeautifulSoup

resultado = requests.get('https://www.elespectador.com')
s = BeautifulSoup(resultado.text, 'lxml')
secciones = s.find('section').find_all('h3')

lista = list()
for seccion in secciones:
    # añadir el contenido que venga en la variable seccion a la lista
    add_list = seccion.get_text()
    lista.append(add_list)
    
# mostrar que la lista si tiene el contenido de los titulos  
# print(lista)

contador = 1
for elementoLista in lista:
    # mostrar el contenido de la variable elementoLista
    print("Noticia " + str(contador) + ": "  + elementoLista)
    contador = contador + 1