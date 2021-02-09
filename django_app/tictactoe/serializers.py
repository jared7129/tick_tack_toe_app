from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Game
    fields = ('player_x' ,'player_o', 'state')
