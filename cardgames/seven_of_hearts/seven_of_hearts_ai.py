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
        choices = self.game.legal_moves(self.hand)
        log.debug("legal moves in hand: " + str(choices))
        try:
            return random.choice(choices)
        except IndexError:
            log.debug("No legal moves! Skipping turn")
            return cs.Card('X')

    def update(self, update_msg):
        log.debug("Player " + self.name + " update: " + str(update_msg))
        self.game_state = update_msg

class HeuristicPlayer(SevenOfHeartsPlayer):
    """ 
    An AI player that chooses randomly from legal moves
    - distance to 7: heuristic for moves which block other players the most
    - number of cards in hand in the same "block": heuristic for moves which help self
    - implicit (1,1) tuning
    """

    def __init__(self, name, game):
        super(HeuristicPlayer, self).__init__(name, game)
        # number of cards in each block
        self.blocks =  {'h': {'above': 0, 'below': 0},
                        'd': {'above': 0, 'below': 0},
                        's': {'above': 0, 'below': 0},
                        'c': {'above': 0, 'below': 0} }

    # def block_generator(self):
    #     for suit in "hdsc":
    #         for block in ['above', 'below']:
    #             yield self.blocks[suit][block]

    def distance(self, card):
        # linear from 1/6 for 6,8 to 1 for A/K
        return float(abs(Value(card) - 7)) / 6.0

    def count_blocks(self):
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

        # self.blocks = map(lambda b: b / dividend, self.block_generator())

        # divide all by dividend
        for suit in "hdsc":
            for block in ['above', 'below']:
                self.blocks[suit][block] /= dividend

        log.debug("blocks: " + str(self.blocks))

    def block_value(self, card):
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
        self.count_blocks()

        # choose card with highest sum of block val and distance
        legal_moves = self.game.legal_moves(self.hand)
        log.debug("legal moves in hand: " + str(legal_moves))

        # return tuple in choices that has the max value
        choices = map(lambda c: (c, self.distance(c) + self.block_value(c)), legal_moves)
        log.debug("choices: " + str(choices))

        try:
            card,value = max(choices, key=lambda x: x[1])
            log.debug("chose " + str(card) + " value: " + str(value))
            return card
        except ValueError:
            log.debug("No legal moves! Skipping turn")
            return cs.Card('X')

    def update(self, update_msg):
        log.debug("Player " + self.name + " update: " + str(update_msg))
        self.game_state = update_msg

