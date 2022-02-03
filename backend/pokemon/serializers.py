from rest_framework import serializers
from .models import Pokemon, PokemonMove


class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonMove
        fields = (
            'name',
        )


class PokemonSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    moves = MoveSerializer(many=True)

    class Meta:
        model = Pokemon
        fields = (
            'id',
            'name',
            'type1',
            'type2',
            'moves',
            'photo_url',
        )

