import requests
import json

token = '6062f453ad72bc899edbd2963957405a'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token': token},
                         json = {
                            "name": "Python",
                            "photo": "https://dolnikov.ru/pokemons/albums/023.png"
                         })
print(response.text)
pokemon_id = response.json()['id']

response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token': token},
                         json = {
                            "pokemon_id": pokemon_id,
                            "name": "SuperPython "+pokemon_id,
                            "photo": "https://dolnikov.ru/pokemons/albums/024.png"
                         })
print(response_change.text)

response_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type': 'application/json', 'trainer_token': token},
                         json = {
                            "pokemon_id": pokemon_id,
                         })
print(response_pokeball.text)

response_trainers = requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id':2123})
print(response_trainers.text)

response_pokeball = requests.post('https://pokemonbattle.me:5000/pokemons/kill', headers = {'Content-Type': 'application/json', 'trainer_token': token},
                         json = {
                            "pokemon_id": 5498,
                         })
print(response_pokeball.text)
