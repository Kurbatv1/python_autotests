import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4fc41a6bd522c8a08e423ae864e6fdd8'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TREINER_ID = '4575' 

def test_status_code ():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TREINER_ID })
    assert response.status_code == 200