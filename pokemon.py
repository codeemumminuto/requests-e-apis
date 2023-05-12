import requests, json

nome_pokemon = "pikachu"
url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
resposta = requests.get(url)

if resposta.status_code == 200:
    pokemon = resposta.json()

    print(f"Nome: {pokemon['name']}")
    print(f"Altura: {pokemon['height']}")
    print(f"HP: {pokemon['stats'][0]['base_stat']}")
    print(f"Ataque: {pokemon['stats'][1]['base_stat']}")
else:
    print("Não conseguimos obter informações.")