from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PokemonMove(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return self.name


class Pokemon(BaseModel):
    """
    Pokemon data from https://pokeapi.co/api/v2/pokemon/
    """
    GRASS = 'GRASS'
    FIRE = 'FIRE'
    POISON = 'POISON'
    WATER = 'WATER'
    NORMAL = 'NORMAL'
    ELECTRIC = 'ELECTRIC'
    ICE = 'ICE'
    FIGHTING = 'FIGHTING'
    GROUND = 'GROUND'
    FLYING = 'FLYING'
    PSYCHIC = 'PSYCHIC'
    BUG = 'BUG'
    ROCK = 'ROCK'
    GHOST = 'GHOST'
    DARK = 'DARK'
    DRAGON = 'DRAGON'
    STEEL = 'STEEL'
    FAIRY = 'FAIRY'
    
    TYPE_CHOICES = (
        (GRASS, 'Grass'),
        (FIRE, 'Fire'),
        (POISON, 'Poison'),
        (WATER, 'Water'),
        (NORMAL, 'Normal'),
        (ELECTRIC, 'Electric'),
        (ICE, 'Ice'),
        (FIGHTING, 'Fighting'),
        (GROUND, 'Ground'),
        (FLYING, 'Flying'),
        (PSYCHIC, 'Psychic'),
        (BUG, 'Bug'),
        (ROCK, 'Rock'),
        (GHOST, 'Ghost'),
        (DARK, 'Dark'),
        (DRAGON, 'Dragon'),
        (STEEL, 'Steel'),
        (FAIRY, 'Fairy'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, blank=False, unique=True, max_length=30)
    moves = models.ManyToManyField(PokemonMove, related_name='pokemon')
    type1 = models.CharField(choices=TYPE_CHOICES, null=False, blank=False, max_length=10)
    type2 = models.CharField(choices=TYPE_CHOICES, null=True, blank=True, max_length=10)
    photo_url = models.CharField(null=True, blank=False, max_length=255)

    class Meta:
        ordering = ['name', ]
        verbose_name_plural = 'Pokemon'

    def __str__(self):
        return self.name
