#### API POKEMON
# DOC: https://pokeapi.co/docs/v2

# GraphQL
# https://beta.pokeapi.co/graphql/console/

import requests, json

nome_pokemon = input(f"Informe o nome do pokemon: ")

#nome_pokemon = "pikachu"

url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}/"

resposta = requests.get(url)

print(resposta)


if resposta.status_code == 200:
    
    pokemon = resposta.json()
    
    print(f"Name: {pokemon['name']}")
    print(f"Altura: {pokemon['height']}")
    print(f"HP: {pokemon['stats'][0]['base_stat']}")
    print(f"Ataque: {pokemon['stats'][1]['base_stat']}")
    print(f"Ataque: {pokemon['moves'][0]['move']['name']}")
    print(f"Ataque: {pokemon['moves'][0]['move']}")
    
else:
    print(f"Não conseguimos obter informações do pokemon!!!")



def get_pokemon():
    nome_pokemon = input(f"Informe o nome do pokemon: ")
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}/"
    resposta = requests.get(url)

    return resposta

resposta = get_pokemon()

if resposta.status_code == 200:
    
    pokemon = resposta.json()
    
    print(f"Name: {pokemon['name']}")
    print(f"Altura: {pokemon['height']} metros")
    print(f"HP: {pokemon['stats'][0]['base_stat']}")
    print(f"Ataque: {pokemon['stats'][1]['base_stat']}")
    print(f"Ataque: {pokemon['moves'][0]['move']['name']}")
    print(f"Ataque: {pokemon['moves'][0]['move']}")

    for i in pokemon['abilities']:
        print(f"Habilidade {i}: {i['ability']['name']}")
else:
    print(f"Não conseguimos obter informações do pokemon!!!")