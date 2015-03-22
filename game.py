from cardsource import *
from player import *
from collections import deque

class SheddingGame(object):
    """ Represents a Shedding-type game https://en.wikipedia.org/wiki/Shedding-type_game """
    def __init__(self, deck):
        super(SheddingGame, self).__init__()
        self.players = deque()
        self.state = {'deck': deck}

    def add_player(self, player):
        self.players.append(player)

    def next_player(self):
        self.players.rotate(1)
        return self.players[0]

    def deal_all_cards(self):
        ''' Deal all cards to all players '''
        self.state['deck'].shuffle()

        while len(self.state['deck']) > 0:
            card = self.state['deck'].pop()
            player = self.next_player()
            player.hand.append(card)

    def setup(self):
        ''' Deal cards and setup board '''
        raise NotImplemented("Cannot setup without a specific game!")

    def round(self):
        ''' A single round of the game '''
        for p in self.players:
            card = p.play()
            if (not 'X' in card.rank): # skip their turn if they play a joker
                self.update_state(card)
                self.update_players()
                if (self.victory(p)):
                    return winner
            else:
                print "Skipping " + player.name + "'s turn"

        return None

    def run(self):
        count = 1
        while True:
            print "Playing round " + str(count)
            count += 1
            winner = self.round()
            if winner:
                print "Player " + str(winner.name) + " has won!"
                break

    def legal(self, card):
        raise NotImplemented("Cannot check legality without a specific game!")

    def update_state(self, card):
        raise NotImplemented("Cannot update_state without a specific game!")

    def update_players(self):
        ''' Construct an update message and send it to all players '''
        raise NotImplemented("Cannot update_players without a specific game!")

    def finish(self):
        raise NotImplemented("Cannot finish without a specific game!")

    def victory(self, player):
        raise NotImplemented("Cannot declare victory without a specific game!")

    def print_state(self):
        print self.state