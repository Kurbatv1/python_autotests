import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4fc41a6bd522c8a08e423ae864e6fdd8'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
BODY_BOY = {
    "pokemon_id": "38463"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_BOY)
print(response.text)'''

'''response_smena = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_BOY)
print(response_smena.text)'''

'''response_poeman = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_BOY)
print(response_poeman.text)'''