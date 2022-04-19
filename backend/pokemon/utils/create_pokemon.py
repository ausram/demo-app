import requests
import json
import logging
from requests.exceptions import HTTPError

from pokemon.serializers import PokemonSerializer
from pokemon.models import Pokemon, PokemonMove


logger = logging.getLogger(__name__)

url = "https://pokeapi.co/api/v2/pokemon/"


def query_poke_api(pokemon: str):
    poke_url = f"{url}/{pokemon}/"
    try:
        response = requests.get(poke_url, timeout=1)
        response.raise_for_status()
        response_dict = json.loads(response.content.decode('utf-8'))
        return response_dict
    except HTTPError as http_err:
        logger.exception(str(http_err))
        raise HTTPError(f'HTTP error occurred: {http_err}')
    except Exception as err:
        logger.exception(str(err))
        raise Exception(f'Other error occurred: {err}')


def fetch_pokemon(pokemon: str):
    moves = {p['name'].lower(): p['id'] for p in PokemonMove.objects.values('id', 'name')}
    try:
        obj = Pokemon.objects.get(name__iexact=pokemon)
        payload = PokemonSerializer(obj).data
    except Pokemon.DoesNotExist:
        poke_data = query_poke_api(pokemon)
        new_pokemon = Pokemon()
        new_pokemon.name = poke_data['name'].title()
        new_pokemon.photo_url = poke_data['sprites']['front_default']
        new_pokemon.type1 = poke_data['types'][0]['type']['name'].upper()
        if len(poke_data['types']) > 1:
            new_pokemon.type2 = poke_data['types'][1]['type']['name'].upper()
        new_pokemon.save()
        for move in poke_data['moves']:
            move_name = move['move']['name'].lower()
            if move_name in moves:
                new_pokemon.moves.add(moves[move_name])
            else:
                new_move = PokemonMove.objects.create(name=move['move']['name'].title())
                new_pokemon.moves.add(new_move)
        payload = PokemonSerializer(new_pokemon).data
    except Exception as e:
        logger.exception(str(e))
        raise Exception(f'Error occurred: {str(e)}')
    return payload
