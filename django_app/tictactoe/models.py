from collections import Counter
from django.urls import reverse
from django.db import models


class Game(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    state = models.CharField(max_length=9, default=" " * 9)

    player_x = models.CharField(max_length=64)
    player_o = models.CharField(max_length=64)

    def __unicode__(self):
        return '{0} vs {1}, state="{2}"'.format(self.player_x, self.player_o, self.state)

    def get_absolute_url(self):
        return reverse('game:detail', kwargs={'pk': self.pk})

    @property
    def next_player(self):
        count = Counter(self.state)
        if count.get('X', 0) > count.get('O', 0):
            return 'O'
        return 'X'

    FORMULAE = [
        [0, 1, 2],  
        [3, 4, 5],  
        [6, 7, 8],  
        [0, 3, 6],  
        [1, 4, 7],  
        [2, 5, 8],  
        [0, 4, 8],  
        [2, 4, 6], 
    ]

    @property
    def is_game_over(self):
        board = list(self.state)
        for wins in self.FORMULAE:
            # Create a tuple
            w = (board[wins[0]], board[wins[1]], board[wins[2]])
            if w == ('X', 'X', 'X'):
                return 'X'
            if w == ('O', 'O', 'O'):
                return 'O'
        # Check for draw
        if ' ' in board:
            return None
        return ' '

    def play(self, index):
        if index < 0 or index >= 9:
            raise IndexError("Invalid board index")

        if self.board[index] != ' ':
            raise ValueError("Square already played")

        board = list(self.state)
        board[index] = self.next_player
        self.state = u''.join(board)

    def play_auto(self):
        from .players import get_player

        while not self.is_game_over:
            next = self.next_player
            player = self.player_x if next == 'X' else self.player_o
            if player == 'human':
                return

            player_obj = get_player(player)
            self.play(player_obj.play(self))
