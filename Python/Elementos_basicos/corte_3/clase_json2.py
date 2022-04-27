import requests
import json

url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=5'

respuesta = requests.get(url)

contenido = respuesta.json()
# print(contenido)

resultados = contenido.get('results', [])
# print(resultados)
contador = 1
for pokemon in resultados:
    name = pokemon['name']
    url_pokemon = pokemon['url']
    frase = "Yo te elijo "
    answer_pokemon = requests.get(url_pokemon)
    general_pokemon = answer_pokemon.json()
    # print(general_pokemon)
    result_cont_pokemon_weight = general_pokemon.get('weight')
    result_cont_pokemon_height = general_pokemon.get('height')
    # print(result_cont_pokemon_weight)
    print(str(contador) + ". " + frase + str(name) + ", su peso es: " + str(result_cont_pokemon_weight) + ", su altura es: " + str(result_cont_pokemon_height))
    '''
    for gen_pokemon in result_cont_pokemon:
        color = gen_pokemon['color']
        print("     " + color)
    '''
    contador = contador + 1