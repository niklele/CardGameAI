from cardsource import *

class Player(object):
    """ Base class for human and AI players """
    def __init__(self, name, game):
        super(Player, self).__init__()
        self.name = name
        self.hand = Hand()
        self.game = game
        
    def play(self):
        raise NotImplemented("Cannot play without a specific kind of player")

    def update(self, update_message):
        raise NotImplemented("Cannot update without a specific kind of player")

