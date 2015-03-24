import sys
import logging as log
import cardsource as cs
from player import Player
from seven_of_hearts import SevenOfHearts

class SevenOfHeartsPlayer(Player):
    """ A human or AI player of SevenOfHearts """
    def __init__(self, name, game):
        super(SevenOfHeartsPlayer, self).__init__(name, game)
        
    def play(self):
    """ Default behavior is to choose no card """
        log.info("Unimplemented Player " + name + " passing their turn")

    def update_proc(self, update_msg):
    """ Default behavior is to overwrite the internal game state with the update message """
        log.debug("Player " + self.name + " update: " + str(update_msg))
        self.game_state = update_msg

    def victory_proc(self):
    """ Default behavior is to log a victory """
        log.debug("Player " + self.name + " was won!")

class HumanPlayer(SevenOfHeartsPlayer):
    """ A human player """
    def __init__(self, name, game):
        super(HumanPlayer, self).__init__(name, game)
        
    def play(self):
        """ Ask the user for input on which card to play from their hand.
        Input is using cardsource notation, eg. 4s is 4 of spades, Ad is Ace of diamond
        To skip their turn, user inputs any string with 'X'
        """
        log.info("Human Player " + self.name)
        log.info("Hand: " + str(self.hand))
        while True:
            try:
                choice = raw_input("Choice:")
                if ('X' in choice):
                    return cs.Card('X')
                choice = cs.Card(choice)
            except KeyboardInterrupt:
                log.critical("\nQuitting the game")
                sys.exit(1)
            except cs.CardSourceError as e:
                print e
            else:
                if choice.rank == 'X': # submit a joker to skip the turn
                    return choice
                elif choice not in self.hand:
                    log.critical(str(choice) + " not in hand")
                elif not self.game.legal(choice):
                    log.critical(str(choice) + " not a legal move")
                else:
                    return choice