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
        log.info("Unimplemented Player " + name + " passing their turn")

    def update(self, update_msg):
        log.debug("Player " + self.name + " update: " + str(update_msg))

class HumanPlayer(SevenOfHeartsPlayer):
    """ A human player """
    def __init__(self, name, game):
        super(HumanPlayer, self).__init__(name, game)
        
    def play(self):
        log.info("Human Player " + self.name)
        log.info("Hand: " + str(self.hand))
        while True:
            try:
                choice = raw_input("Choice:")
                if ('X' in choice):
                    return cs.Card('X')
                choice = cs.Card(choice)
            except KeyboardInterrupt:
                log.warning("\nQuitting the game")
                sys.exit(1)
            except cs.CardSourceError as e:
                print e
            else:
                if choice.rank == 'X': # submit a joker to skip the turn
                    return choice
                elif choice not in self.hand:
                    log.warning(str(choice) + " not in hand")
                elif not self.game.legal(choice):
                    log.warning(str(choice) + " not a legal move")
                else:
                    return choice

    def update(self, update_msg):
        log.info("Player " + self.name + " update: " + str(update_msg))
        self.game_state = update_msg