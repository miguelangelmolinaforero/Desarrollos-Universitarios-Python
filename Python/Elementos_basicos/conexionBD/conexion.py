
import psycopg2
import requests
from bs4 import BeautifulSoup
from datetime import date

resultado = requests.get('https://www.elespectador.com')
s = BeautifulSoup(resultado.text, 'lxml')
secciones = s.find('section').find_all('a')

contador = 1
lista = list()

for seccion in secciones:
    conexion = psycopg2.connect(database='fecha_titulares', user='miguel', password='12345', host='localhost', port='5432')
    # print("base de datos - conectada")
    add_date = date.today()
    add_nombre = seccion.get_text()
    lista.append(add_nombre)
    print("Noticia " + str(contador) + ": "  + add_nombre)
    cur = conexion.cursor()
    cur.execute("INSERT INTO fecha_titulares (id, fecha, nombre) VALUES ('"+ str(contador) + "', '" + str(add_date) +"', '"+ add_nombre + "')")
    contador = contador + 1
    conexion.commit()
    conexion.close()


'''
conexion = psycopg2.connect(database='fecha_titulares', user='miguel', password='12345', host='localhost', port='5432')
print("base de datos - conectada")
cur = conexion.cursor()
cur.execute("DELETE FROM fecha_titulares")
conexion.commit()
conexion.close()
'''
