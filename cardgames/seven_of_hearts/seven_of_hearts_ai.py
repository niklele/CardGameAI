import logging as log
import cardsource as cs
from player import Player
from seven_of_hearts import SevenOfHearts, Value
from seven_of_hearts_player import SevenOfHeartsPlayer
import random

class RandomPlayer(SevenOfHeartsPlayer):
    """ An AI player that chooses randomly from legal moves """
    def __init__(self, name, game):
        super(RandomPlayer, self).__init__(name, game)

    def play(self):
        choices = self.game.legal_moves(self.hand)
        log.debug("legal moves in hand: " + str(choices))
        try:
            return random.choice(choices)
        except IndexError:
            log.debug("No legal moves! Skipping turn")
            return cs.Card('X')

    def update(self, update_msg):
        log.debug("Player " + self.name + " update: " + str(update_msg))
        self.game_state = update_msg