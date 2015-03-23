from collections import deque
import logging as log

class SheddingGame(object):
    """ Represents a Shedding-type game https://en.wikipedia.org/wiki/Shedding-type_game """
    def __init__(self, deck):
        super(SheddingGame, self).__init__()
        self.players = deque()
        self.state = {'deck': deck, 'round': 0}

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
                log.info("Player " + p.name + " played " + str(card))
                try:
                    p.hand.remove(card)
                except ValueError:
                    log.critical("illegal move by " + p.name + ": card: " + str(card) + " not in hand!")
                    exit(1)
                self.update_state(card)
                self.update_players()
                if (self.victory(p)):
                    return p
            else:
                log.info("Player " + p.name + " skipped their turn")

        return None

    def run(self):
        while True:
            log.info("Round " + str(self.state['round']))
            winner = self.round()
            if winner:
                log.info("Player " + str(winner.name) + " has won!")
                break
            self.state['round'] += 1

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