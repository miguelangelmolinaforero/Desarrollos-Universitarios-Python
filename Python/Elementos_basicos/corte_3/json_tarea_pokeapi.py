import json
import requests
import psycopg2

url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20'

respuesta = requests.get(url)
contenido = respuesta.json()
resultados = contenido.get('results', [])

conexion = psycopg2.connect(database="pokemones", user="miguel", password="12345", host="127.0.0.1", port="5432")
print("base de datos - conectado")

cur = conexion.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS pokemonesapi (pokemonID INT GENERATED ALWAYS AS IDENTITY, Nombre VARCHAR(255) NOT NULL, Weights VARCHAR(255) NOT NULL, Height VARCHAR(255) NOT NULL, Urls VARCHAR(255) NOT NULL, Foto VARCHAR(255) NOT NULL, Ability VARCHAR NOT NULL, Location VARCHAR NOT NULL, Color VARCHAR NOT NULL, Movimientos VARCHAR NOT NULL , PRIMARY KEY(pokemonID));")



for pokemon in resultados:
    name = pokemon["name"]
    url_details = pokemon["url"]
    
    pokemon_details = requests.get(url_details)
    pokemon_content = pokemon_details.json()
    photos_pokemons = pokemon_content.get("sprites")
    other = photos_pokemons.get("other")
    photo_link = other.get("official-artwork")
    photo_pokemon = photo_link["front_default"]
    weight = pokemon_content.get('weight')
    height = pokemon_content.get('height')
    location = pokemon_content.get('location_area_encounters')


    moves = pokemon_content.get('moves', [])
    move = ""
    for poke_move in moves:
        movement_general = poke_move.get("move")

        if move == "":
            move = movement_general["name"]
        else:
            move += ", " + movement_general["name"]
    

    game_indices_pokemon = pokemon_content.get("game_indices", [])
    color = ""
    for poke_indice in game_indices_pokemon:
        version = poke_indice.get("version")

        if color == "":
            color = version["name"]
        else:
            color += ", " + version["name"]
        
    pokemon_abilities = pokemon_content.get("abilities", [])
    ability = ""
    for pokemon_ability in pokemon_abilities:
        capacidad = pokemon_ability.get("ability")

        if ability == "": 
            ability = capacidad["name"] 
        else: 
            ability += ", " + capacidad["name"]
    
    cur.execute("INSERT INTO pokemonesapi (Nombre, Weights, Height, Urls, Foto, Ability, Location, Color, Movimientos) VALUES ('" + str(name) + "','" + str(weight) + "','" + str(height) + "','" + str(url_details) + "','" + str(photo_pokemon) + "','" + str(ability) + "', '" + str(location) + "', '" + str(color) + "', '" + str(move) + "');")

    print("DATOS DEL POKEMON \n" + "Nombre: " + str(name) + "\nPeso: " + str(weight) + " \nAltura: " + str(height) + " \nUrl: " + str(url_details) + " \nFoto: " + str(photo_pokemon) + " \nHabilidades: " + str(ability) +"\nUbicación: " + str(location) + "\nColores disponibles: " + str(color) + "\nMovimientos dispobibles: " + str(move) + "\n")
conexion.commit()

archivo = open('integrantes.txt', 'a+')
with archivo:
    writer = archivo.write("INTEGRANTES\n\n")
    writer = archivo.write("Miguel Angel Molina Forero\n")
    writer = archivo.write("Edwar Santiago Rojas Cardenas\n")
    writer = archivo.write("Deivi Alejandro Villamil Ramirez\n\n")
    writer = archivo.write("EXTRACCION, TRANSFORMACION, CARGA DE DATOS\n")
print("datos almacenados")