from django.contrib import admin

from pokemon.models import User
from pokemon.models import Pokemon
from pokemon.models import Capture

class UserAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'place']

class PokemonAdmin(admin.ModelAdmin):
    list_display = ['name', 'place', 'master']

class CaptureAdmin(admin.ModelAdmin):
    list_display = ['pokemon','master','place','captured_at']

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Capture, CaptureAdmin)