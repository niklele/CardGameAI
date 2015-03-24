import logging as log
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
    """ Gives the ordering of the cards in the game. Note: Aces are low """
    return VALUES[card.rank]

class SevenOfHearts(SheddingGame):
    def __init__(self):
        super(SevenOfHearts, self).__init__()
        self.state['h'] = [] # hearts
        self.state['d'] = [] # diamonds
        self.state['s'] = [] # spades
        self.state['c'] = [] # clubs

    def setup(self):
        """ Deal all cards to players """
        self.state['round'] = 0
        log.debug("Dealing cards for " + str(len(self.players)) + " players")
        self.deal_all_cards()

    def legal(self, card):
        """ Define a legal move:
        Card must be a 7 or can be placed in a suit array if the correct neighbor is present.
        Correct neighbors are 1 closer to 7.
        """
        s_array = self.state[card.suit]
        value = Value(card)
        if (value > 7):
            return len(filter(lambda c: Value(c) is value-1, s_array)) > 0
        elif (value < 7):
            return len(filter(lambda c: Value(c) is value+1, s_array)) > 0
        else: # always allowed to place a 7
            return True

    def legal_moves(self, cards):
        """ Filter a set of cards to only include legal moves """
        return filter(lambda c: self.legal(c), cards)

    def update_players(self):
        """ Send the entire state of the game as an update to players.
        Currently unused by all players.
        """
        update = self.state
        log.debug("Update: " + str(update))
        for p in self.players:
            p.update_proc(update)

    def update_state(self, card):
        """ Add the given card to the suit arrays of the game """
        s_array = self.state[card.suit]
        value = Value(card)
        if (value >= 7):
            s_array.append(card)
        else:
            s_array.insert(0,card)

    def victory(self, player):
        """ Victory condition: a player wins when their hand is exhausted """
        return (len(player.hand) == 0)

    def finish(self):
        """ Cleanup the game by taking all cards back from players """
        log.debug("finished the game in " + str(self.state['round']) + " rounds")
        self.take_all_cards()
