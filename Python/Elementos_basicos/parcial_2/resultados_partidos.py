import requests
from bs4 import BeautifulSoup

resultado = requests.get('https://es.wikipedia.org/wiki/Clasificaci%C3%B3n_de_Conmebol_para_la_Copa_Mundial_de_F%C3%BAtbol_de_2022')
s = BeautifulSoup(resultado.text, 'lxml')

# nations = s.find('table').find_all('td')                                      
# results = s.find('tr').find_all('td')                                                
results = s.find('th').find_all('a', {'class':'mw-redirect'})  
# print(results)

for result in results:
    print(result.get_text())
'''
lista = list()
for seccion in results:
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

'''