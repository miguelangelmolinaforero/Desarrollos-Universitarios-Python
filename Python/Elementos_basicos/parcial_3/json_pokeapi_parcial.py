import json, requests, psycopg2

url = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=5'
results = requests.get(url).json().get('results', [])

for result in results:
    name = result['name']
    url_details = result['url']
    pokemon_details = requests.get(url_details).json().get("abilities", [])
    ability = ""
    for pokemon_ability in pokemon_details:
        capacidad = pokemon_ability.get("ability")
        if ability == "": 
            ability = capacidad['name'] 
        else: 
            ability += ", " + capacidad['name']
    print("DATOS DEL POKEMON \n" + "Nombre: " + str(name) + "\nHabilidades: " + str(ability) + "\n")