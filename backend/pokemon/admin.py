from django.contrib import admin
from pokemon.models import Pokemon, PokemonMove
# Register your models here.


admin.site.site_header = 'Pokemon Admin'
admin.site.index_title = 'Access Management'


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'type1', 'type2')
    filter_horizontal = ('moves', )

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser


admin.site.register(PokemonMove)
