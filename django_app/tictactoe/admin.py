from django.contrib import admin

# Register your models here.
from .models import Game

class GameAdmin(admin.ModelAdmin):
  list_display = ('player_x', 'player_o', 'state')

admin.site.register(Game, GameAdmin)
