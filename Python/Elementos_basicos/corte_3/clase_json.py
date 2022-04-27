import json

# JSON >>>> DICCIONARIO

# PARTE 1


persona = '{"Nombre": "Miguel", "Lenguajes": ["Inglés", "Francés"]}'

persona_dict = json.loads(persona)

print(persona_dict)
print(persona_dict["Lenguajes"])


# PARTE 2

'''
with open("c:/Users/mikem/Desktop/Python/archivos/persona.json") as f:
    data = json.load(f)

print(data)
'''

# PARTE 3
'''
persona = {
    "Nombre": "Miguel",
    "Edad": 18,
    "Hijos": 0,
    "Casado": True
}

with open("c:/Users/mikem/Desktop/Python/archivos/persona_miguel.txt", "w") as json_archivo:
    json.dump(persona, json_archivo)
'''