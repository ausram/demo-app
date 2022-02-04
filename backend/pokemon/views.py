# Create your views here.
import logging
import random

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import PokemonSerializer
from .models import Pokemon
from .utils.create_pokemon import fetch_pokemon

logger = logging.getLogger(__name__)


class PokemonViewSet(viewsets.ModelViewSet):
    """
    A viewset for retrieving pokemon data
    """
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

    # @action(detail=False, methods=['GET'], )
    def retrieve(self, request, pk=None, *args, **kwargs):
        pokemon = pk
        if not pokemon:
            payload = "Giving a pokemon name might be a good idea"
            status_code = status.HTTP_404_NOT_FOUND
        else:
            try:
                payload = fetch_pokemon(pokemon.lower())
                status_code = status.HTTP_200_OK
            except Exception as e:
                payload = f"An error occurred fetching pokemon data: {str(e)}"
                status_code = status.HTTP_400_BAD_REQUEST
        return Response(data=payload, status=status_code)

    @action(detail=False, methods=['GET', ], url_path=r'change-colour/(?P<pk>\d+)',)
    def change_colour(self, request, pk=None, *args, **kwargs):
        try:
            obj = Pokemon.objects.get(pk=pk)
            if obj.type1 == Pokemon.GRASS:
                payload = "#0fa63f"
                status_code = status.HTTP_200_OK
            else:
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                payload = f"rgb({r}, {g}, {b})"
                status_code = status.HTTP_200_OK
        except Exception as e:
            payload = f"An error occurred fetching pokemon data: {str(e)}"
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(data=payload, status=status_code)

    @action(detail=False, methods=['GET', ], url_path=r'pokemon-name/(?P<pk>\d+)', )
    def change_colour(self, request, pk=None, *args, **kwargs):
        try:
            obj = Pokemon.objects.get(pk=pk)
            if 'Quick Attack' in obj.moves.first().name:
                payload = 'Quick Attack'
                status_code = status.HTTP_200_OK
            else:
                payload = obj.moves.first().name
                status_code = status.HTTP_200_OK
        except Exception as e:
            payload = f"An error occurred fetching pokemon data: {str(e)}"
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(data=payload, status=status_code)
