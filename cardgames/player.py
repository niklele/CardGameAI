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
    """ A single play from the player.
    Must return a single Card from the player's hand.
    """
        raise NotImplemented("Cannot play without a specific kind of player")

    def update_proc(self, update_message):
    """ Process an update message from the game loop """
        raise NotImplemented("Cannot update without a specific kind of player")

    def victory_proc(self):
    """ Process a victory notification from the game loop """
        raise NotImplemented("Cannot be notified of victory without a specific kind of player")

