from io import open

# abrir archivo para escribir
archivo = open("archivo_de_texto.txt", "a+") # write

# abrir archivo para eliminar contenido
# archivo = open("archivo_de_texto.txt", "w") # remove


# escribir
archivo.write("que mas pues :v\n\nTons khe")
archivo.write("")
archivo.write("\ntamos melos :VVVVV\n")
archivo.write("\nViva el Real Madrid\n")

print("creado correctamente")

# cerrar archivo
archivo.close()

print("cerrado correctamente")

# leer contenido
archivo_lectura = open("archivo_de_texto.txt", "r")
# almacena el contenido del archivo en una variable
contenido = archivo_lectura.read()
print(contenido)

for element in contenido:
    # imprime el contenido letra por letra
    print(element)


# Leer contenido lista
archivo_lectura_lista = open("archivo_de_texto.txt", "r")
lista = archivo_lectura_lista.readlines()
archivo_lectura_lista.close()

# print(lista)
for frase in lista:
    # frase = frase.lower()
    # frase = frase.swapcase() # invierte las mayusculas por minusculas
    print(frase)
    # print("---" + str(frase.count("e"))) # cuenta las letras "e"
    # print(frase.find("e")) # busca las letras "e"
    print(frase.replace("Real Madrid", "Barcelona"))
    # print(frase.title()) # convierte el texto en un titulo