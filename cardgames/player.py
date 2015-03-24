import logging as log
import cardsource as cs

class Player(object):
    """ Base class for human and AI players """
    def __init__(self, name, game):
        super(Player, self).__init__()
        self.name = name
        self.hand = cs.Hand()
        self.game = game
        
    def play(self):
        raise NotImplemented("Cannot play without a specific kind of player")

    def update(self, update_message):
        raise NotImplemented("Cannot update without a specific kind of player")

    def notify_victory(self):
        raise NotImplemented("Cannot be notified of victory without a specific kind of player")

