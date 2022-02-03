# Create your views here.
import logging

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
        print(pokemon, type(pokemon))
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
