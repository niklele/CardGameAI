import logging as log
import random
import cardsource as cs
from player import Player
from seven_of_hearts import SevenOfHearts, Value
from seven_of_hearts_player import SevenOfHeartsPlayer

class RandomPlayer(SevenOfHeartsPlayer):
    """ An AI player that chooses randomly from legal moves """
    def __init__(self, name, game):
        super(RandomPlayer, self).__init__(name, game)

    def play(self):
    """ Chooses randomly from legal moves """
        choices = self.game.legal_moves(self.hand)
        log.debug("legal moves in hand: " + str(choices))
        try:
            return random.choice(choices)
        except IndexError:
            log.debug("No legal moves! Skipping turn")
            return cs.Card('X')

class HeuristicPlayer(SevenOfHeartsPlayer):
    """ 
    An AI player that chooses randomly from legal moves
    - distance to 7: heuristic for moves which block other players the most
    - number of cards in hand in the same "block": heuristic for moves which help self
    - implicit (1,1) tuning
    """

    def __init__(self, name, game):
        super(HeuristicPlayer, self).__init__(name, game)
        self.reset_blocks()
        self.victories = 0

    def reset_blocks(self):
    """ Reset block counters to 0.
    Values are percentages of held cards in position relative to the 7 in each suit array
    """
        self.blocks =  {'h': {'above': 0, 'below': 0},
                        'd': {'above': 0, 'below': 0},
                        's': {'above': 0, 'below': 0},
                        'c': {'above': 0, 'below': 0} }

    def distance(self, card):
        """ linear from (1/6) for 6 and 8 to (1) for Ace and King """
        return float(abs(Value(card) - 7)) / 6.0

    def count_blocks(self):
        """ Record the percentage of cards in hand in each block """
        # number of cards in each block
        dividend = 0.0
        for c in self.hand:
            dividend += 1
            if (Value(c) > 7):
                self.blocks[c.suit]['above'] += 1
            elif (Value(c) < 7):
                self.blocks[c.suit]['below'] += 1
            else:
                self.blocks[c.suit]['above'] += 1
                self.blocks[c.suit]['below'] += 1
                dividend += 1

        # divide all by dividend
        for suit in "hdsc":
            for block in ['above', 'below']:
                self.blocks[suit][block] /= dividend

        log.debug("blocks: " + str(self.blocks))

    def block_value(self, card):
        """ get the block value for a given card """
        v = Value(card)
        above = self.blocks[card.suit]['above']
        below = self.blocks[card.suit]['below']
        if (v > 7):
            return above
        elif (v < 7):
            return below
        else:
            return above + below

    def play(self):
        """ Reconunt cards in hand, then choose the card to play based on the heuristic
        Chosen card is argmax(block value + distance value)
        """
        self.reset_blocks()
        self.count_blocks()

        legal_moves = self.game.legal_moves(self.hand)
        log.debug("legal moves in hand: " + str(legal_moves))

        # create list of tuples with (card, heuristic)
        choices = map(lambda c: (c, self.distance(c) + self.block_value(c)), legal_moves)
        log.debug("choices: " + str(choices))

        try:
            # return tuple in choices that has the max heuristic value
            card,value = max(choices, key=lambda x: x[1])
            log.debug("chose " + str(card) + " value: " + str(value))
            return card
        except ValueError:
            log.debug("No legal moves! Skipping turn")
            return cs.Card('X')

    def victory_proc(self):
        """ count vicotries to look at performace later """
        self.victories += 1
        log.debug("Player " + self.name + " was won " + str(self.victories) + " times")
