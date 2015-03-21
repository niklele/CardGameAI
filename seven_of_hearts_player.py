from cardsource import *
from player import *
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
                    return Card('X')
                choice = Card(choice)
            except CardSourceError as e:
                print e
            else:
                if choice.rank == 'X': # submit a joker to skip the turn
                    return choice
                elif choice in self.hand and self.game.legal(choice):
                    self.hand.remove(choice)
                    print "Playing " + str(choice)
                    return choice
                else:
                    print "Card not in hand or illegal"

    def update(self, update_msg):
        print "Player " + self.name + " update: " + str(update_msg)
        self.game_state = update_msg