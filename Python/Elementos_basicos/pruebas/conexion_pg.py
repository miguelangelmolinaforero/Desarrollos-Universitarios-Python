import psycopg2

conexion = psycopg.connect(database="futbolistas", user="prueba", password="12345", host="172.0.0.1" )

print ("Base de Datos - conectada")

con = conexion.cursor()
con.execute("INSERT INTO futbolistas (id, nombre, edad) VALUES (1, Lionel Messi, 33)")

print("Datos ingresados correctamente")

conexion.commit()
conexion.close()
