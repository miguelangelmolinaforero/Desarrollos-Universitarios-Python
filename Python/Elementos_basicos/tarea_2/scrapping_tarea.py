import requests
from bs4 import BeautifulSoup
import csv
import operator

resultado = requests.get('https://www.elespectador.com')
s = BeautifulSoup(resultado.text, 'lxml')
secciones = s.find('section').find_all('h2')

noticeList = list()
for seccion in secciones:
    # añadir el contenido que venga en la variable seccion a la lista
    add_list = seccion.get_text()
    noticeList.append(add_list)

arrayContent = list()
arrayContent.append(['Número de Noticia', 'Titulo'])

iterator = 1

for elementList in noticeList:
    arrayAux = ["Noticia " + str(iterator), elementList]
    iterator = iterator + 1
    arrayContent.append(arrayAux)

print(arrayContent)
 
myFile = open('my_first_csv.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(arrayContent)
     
print("Creado correctamente")