import sys
import cardsource as cs
from player import Player
from seven_of_hearts import SevenOfHearts

class SevenOfHeartsPlayer(Player):
    """ A human or AI player of SevenOfHearts """
    def __init__(self, name, game):
        super(SevenOfHeartsPlayer, self).__init__(name, game)
        
    def play(self):
        print "Unimplemented Player " + name + " passing their turn"

    def update(self, update_msg):
        print "Player " + self.name + " update: " + str(update_msg)

class HumanPlayer(SevenOfHeartsPlayer):
    """ A human player """
    def __init__(self, name, game):
        super(HumanPlayer, self).__init__(name, game)
        
    def play(self):
        print "Human Player " + self.name
        print "Hand: " + str(self.hand)
        while True:
            try:
                choice = raw_input("Choice:")
                if ('X' in choice):
                    return cs.Card('X')
                choice = cs.Card(choice)
            except KeyboardInterrupt:
                print "\nQuitting the game"
                sys.exit(1)
            except cs.CardSourceError as e:
                print e
            else:
                if choice.rank == 'X': # submit a joker to skip the turn
                    return choice
                elif choice not in self.hand:
                    print str(choice) + " not in hand"
                elif not self.game.legal(choice):
                    print str(choice) + " not a legal move"
                else:
                    self.hand.remove(choice)
                    return choice

    def update(self, update_msg):
        # print "Player " + self.name + " update: " + str(update_msg)
        self.game_state = update_msg