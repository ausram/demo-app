from rest_framework import serializers
from .models import Pokemon, PokemonMove


class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonMove
        fields = (
            'name',
        )


class PokemonSerializer(serializers.ModelSerializer):
    moves = MoveSerializer(many=True)

    class Meta:
        model = Pokemon
        fields = (
            'name',
            'type1',
            'type2',
            'moves',
            'photo_url',
        )

