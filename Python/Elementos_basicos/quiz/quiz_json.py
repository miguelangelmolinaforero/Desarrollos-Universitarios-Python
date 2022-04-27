
#Codigo mio
import json

# se carga el archivo json
with open("C:/Users/mikem/OneDrive/Escritorio/Python/archivos/quiz.json") as f:
    data = json.load(f)
content = data.get('arrayColores', [])
for color_data in content:
    color_name = color_data['nombreColor'] 
    color_value = color_data['valorHexadec']

    name = "\nNombre del Color: " + color_name
    value = "\nValor Hexagecimal: " + color_value

    print(name)
    print(value)

    archivo = open('C:/Users/mikem/OneDrive/Escritorio/Python/archivos/quiz_texto.txt', 'a+')
    with archivo:
        writer = archivo.write(name)
        writer = archivo.write(value)

print("Creado correctamente")

'''
# Codigo ustedes

import json

json_file = '{"arrayColores": [{"nombreColor": "rojo","valorHexadec": "#f00"},{"nombreColor": "verde","valorHexadec": "#0f0"},{"nombreColor": "azul","valorHexadec": "#00f"},{"nombreColor": "cyan","valorHexadec": "#0ff"},{"nombreColor": "magenta","valorHexadec": "#f0f"},{"nombreColor": "amarillo","valorHexadec": "#ff0"},{"nombreColor": "negro","valorHexadec": "#000"}]}'

data = json.loads(json_file)

content = data.get('arrayColores', [])
for color_data in content:
    color_name = color_data['nombreColor'] 
    color_value = color_data['valorHexadec']

    name = "\nNombre del Color: " + color_name
    value = "\nValor Hexagecimal: " + color_value

    print(name)
    print(value)

    archivo = open('C:/Users/mikem/OneDrive/Escritorio/Python/archivos/quiz_texto.txt', 'a+')
    with archivo:
        writer = archivo.write(name)
        writer = archivo.write(value)

print("Creado correctamente")
'''