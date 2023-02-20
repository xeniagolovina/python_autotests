import requests
import pytest

token = '6062f453ad72bc899edbd2963957405a'

def test_status_code():
        response = requests.get('https://pokemonbattle.me:5000/trainers')
        assert response.status_code==200
    
def test_trainer_name():
        response_trainer = requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id':2123})
        assert response_trainer.json()['trainer_name']=='Xenia G'
    
@pytest.mark.parametrize('key, value', [('trainer_name', 'Xenia G'), ('city', 'Moscow'), ('level','4'), 
                                        ('pokemons_alive', ['5500','5834'])])
def test_param(key,value):
        response_trainer = requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id':2123})
        assert response_trainer.json()[key]==value