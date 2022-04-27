import requests, psycopg2, json, csv
from bs4 import BeautifulSoup

# BASE DE DATOS INTERNACIONAL

conexion_inter = psycopg2.connect(database='ETL_bolsa_internacional', user='miguel', password='12345', host='localhost', port='5432')
cur_inter = conexion_inter.cursor()
cur_inter.execute("CREATE TABLE IF NOT EXISTS indice (id_indice INT GENERATED ALWAYS AS IDENTITY, fecha_indice VARCHAR(255) NOT NULL, nom_empresa VARCHAR(255) NOT NULL, valor_indice VARCHAR(255) NOT NULL, fk_nom_pais VARCHAR(255), PRIMARY KEY(id_indice));")

cur_inter.execute("CREATE TABLE IF NOT EXISTS pais (nom_pais VARCHAR(255) NOT NULL, PRIMARY KEY(nom_pais));")

cur_inter.execute("ALTER TABLE indice ADD CONSTRAINT fk_n_p FOREIGN KEY (fk_nom_pais) REFERENCES pais(nom_pais)")

# Inserciones de los paises a la base de datos
cur_inter.execute("INSERT INTO pais (nom_pais) VALUES ('Mexico')")
cur_inter.execute("INSERT INTO pais (nom_pais) VALUES ('Argentina')")

with open("C:/Users/mikem/OneDrive/Escritorio/Python/archivos/proyecto_indice_internacional.json") as f:
    data = json.load(f)
content = data.get('datos_internacionales', [])
for data_inter in content:
    indice_date_inter = data_inter['fecha_indice'] 
    indice_name_inter = data_inter['nom_empresa'] 
    indice_value_inter = data_inter['valor_indice']

    cur_inter.execute("INSERT INTO indice (fecha_indice, nom_empresa, valor_indice) VALUES ('" + str(indice_date_inter) + "', '" + str(indice_name_inter) + "', '" + str(indice_value_inter) + "');") 

conexion_inter.commit()
print("Creado correctamente")



# BASE DE DATOS NACIONAL

conexion_nal = psycopg2.connect(database='ETL_bolsa_nacional', user='miguel', password='12345', host='localhost', port='5432')
cur_nal = conexion_nal.cursor()
cur_nal.execute("CREATE TABLE IF NOT EXISTS indice (id_indice INT GENERATED ALWAYS AS IDENTITY, fecha_indice VARCHAR(255) NOT NULL, nom_empresa VARCHAR(255) NOT NULL, valor_indice VARCHAR(255) NOT NULL, fk_nom_pais VARCHAR(255), PRIMARY KEY(id_indice));")

cur_nal.execute("CREATE TABLE IF NOT EXISTS pais (nom_pais VARCHAR(255) NOT NULL, PRIMARY KEY(nom_pais));")

cur_nal.execute("ALTER TABLE indice ADD CONSTRAINT fk_n_p FOREIGN KEY (fk_nom_pais) REFERENCES pais(nom_pais)")

cur_nal.execute("INSERT INTO pais (nom_pais) VALUES ('Colombia')")

with open("C:/Users/mikem/OneDrive/Escritorio/Python/archivos/proyecto_indice_nacional.json") as f:
    data = json.load(f)
content = data.get('datos_nacionales', [])
for data_nal in content:
    indice_date_nal = data_nal['fecha_indice'] 
    indice_name_nal = data_nal['nom_empresa'] 
    indice_value_nal = data_nal['valor_indice']

    cur_inter.execute("INSERT INTO indice (fecha_indice, nom_empresa, valor_indice) VALUES ('" + str(indice_date_nal) + "', '" + str(indice_name_nal) + "', '" + str(indice_value_nal) + "');") 

conexion_nal.commit()
print("Creado correctamente")


# BOLSA DE DATOS RESULTANTE

conexion_result = psycopg2.connect(database='ETL_bolsa_resultante', user='miguel', password='12345', host='localhost', port='5432')
cur_result = conexion_result.cursor()
cur_result.execute("CREATE TABLE IF NOT EXISTS indice (id_indice INT GENERATED ALWAYS AS IDENTITY, fecha_indice VARCHAR(255) NOT NULL, nom_empresa VARCHAR(255) NOT NULL, valor_indice VARCHAR(255) NOT NULL, PRIMARY KEY(id_indice));")

cur_result.execute("CREATE TABLE IF NOT EXISTS pais (nom_pais VARCHAR(255), PRIMARY KEY(nom_pais));")

# Limpieza e insercion de datos a la base de datos resultante

cur_inter.execute("SELECT * FROM pais")
tablas_pais_inter = cur_inter.fetchall()

for tabla_pais in tablas_pais_inter:
    paises_inter = tabla_pais[0]
    cur_result.execute("INSERT INTO pais (nom_pais) VALUES ('" + paises_inter + "')")
    
cur_inter.execute("SELECT * FROM indice")
tablas_indice_inter = cur_inter.fetchall()

for tabla_indice in tablas_indice_inter:
    fecha_indice_result = tabla_indice[1]
    nombre_indice_result = tabla_indice[2]
    valor_indice_result = tabla_indice[3]
    cur_result.execute("INSERT INTO indice (fecha_indice, nom_empresa, valor_indice) VALUES ('" + str(fecha_indice_result) + "', '" + str(nombre_indice_result) + "', '" + str(valor_indice_result) + "');")

cur_nal.execute("SELECT * FROM pais")
tablas_pais_nal = cur_nal.fetchall()

for tabla_pais in tablas_pais_nal:
    paises_nal = tabla_pais[0]
    # cur_result.execute("INSERT INTO pais (nom_pais) VALUES '" + str(paises_nal) + "');")
    
cur_nal.execute("SELECT * FROM indice")
tablas_indice_nal = cur_nal.fetchall()

for tabla_indice in tablas_indice_nal:
    fecha_indice_result = tabla_indice[1]
    nombre_indice_result = tabla_indice[2]
    valor_indice_result = tabla_indice[3]
    cur_result.execute("INSERT INTO indice (fecha_indice, nom_empresa, valor_indice) VALUES ('" + str(fecha_indice_result) + "', '" + str(nombre_indice_result) + "', '" + str(valor_indice_result) + "');")


# Creacion de archivo .csv para analisis de datos

cur_result.execute("SELECT * FROM indice")
tablas_indice_result = cur_result.fetchall()

lista_indices = list()
lista_indices.append(['ID', 'Fecha', 'Nombre', 'Valor'])
for tabla_indice in tablas_indice_result:
    id_indice_result = tabla_indice[0]
    fecha_indice_result = tabla_indice[1]
    nombre_indice_result = tabla_indice[2]
    valor_indice_result = tabla_indice[3]
    arrayAux = [str(id_indice_result), str(fecha_indice_result), str(nombre_indice_result), str(valor_indice_result)]
    lista_indices.append(arrayAux)

myFile = open('C:/Users/mikem/OneDrive/Escritorio/Python/archivos/archivo_base_final.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(lista_indices)
    


conexion_inter.close()
conexion_nal.close()
conexion_result.close()
