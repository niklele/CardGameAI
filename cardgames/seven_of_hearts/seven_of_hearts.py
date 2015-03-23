import cardsource as cs
from game import SheddingGame

VALUES = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13
}
def Value(card):
    return VALUES[card.rank]

class SevenOfHearts(SheddingGame):
    def __init__(self, deck):
        super(SevenOfHearts, self).__init__(deck)
        self.state['h'] = [] # hearts
        self.state['d'] = [] # diamonds
        self.state['s'] = [] # spades
        self.state['c'] = [] # clubs

    def setup(self):
        print "Dealing cards for " + str(len(self.players)) + " players"
        self.deal_all_cards()

    def legal(self, card):
        pile = self.state[card.suit]
        value = Value(card)
        # Return true if there is a correct neighbor card in the pile
        if (value > 7):
            return len(filter(lambda c: Value(c) is value-1, pile)) > 0
        elif (value < 7):
            return len(filter(lambda c: Value(c) is value+1, pile)) > 0
        else: # always allowed to place a 7
            return True

    def legal_moves(self, cards):
        return filter(lambda c: self.legal(c), cards)

    def update_players(self):
        update = self.state
        print "Update: " + str(update)
        for p in self.players:
            p.update(update)

    def update_state(self, card):
        pile = self.state[card.suit]
        value = Value(card)
        if (value >= 7):
            pile.append(card)
        else:
            pile.insert(0,card)

    def victory(self, player):
        return (len(player.hand) == 0)

    def finish(self):
        print "finished the game in " + str(self.state['round']) + " rounds"
