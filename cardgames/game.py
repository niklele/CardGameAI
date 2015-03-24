from collections import deque
import logging as log
import cardsource as cs

class SheddingGame(object):
    """ Represents a Shedding-type game https://en.wikipedia.org/wiki/Shedding-type_game """
    def __init__(self):
        super(SheddingGame, self).__init__()
        self.players = deque()
        self.state = {'deck': cs.Deck(), 'round': 0}

    def add_player(self, player):
        """ Add a player to the game """
        self.players.append(player)

    def next_player(self):
        """ Shift the start player over by 1 """
        self.players.rotate(1)
        return self.players[0]

    def print_players(self):
        """ Log all players' names """
        log.critical("Players: " + str(map(lambda p: p.name, self.players)).strip('[]'))

    def deal_all_cards(self):
        """ Shuffle the deck and deal all cards to all players """
        self.state['deck'].shuffle()
        while len(self.state['deck']) > 0:
            card = self.state['deck'].pop()
            player = self.next_player()
            player.hand.append(card)

    def take_all_cards(self):
        """ Take all cards from all players and recreate the deck """
        for p in self.players:
            p.hand = cs.Hand()
        self.state['deck'] = cs.Deck()

    def setup(self):
        """ Deal cards and setup board """
        raise NotImplemented("Cannot setup without a specific game!")

    def round(self):
        """ A single round of the game """
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
                    p.notify_victory()
                    return p
            else:
                log.info("Player " + p.name + " skipped their turn")

        return None

    def run(self):
        """ Run as many rounds as necessary until a player wins """
        while True:
            log.info("Round " + str(self.state['round']))
            winner = self.round()
            if winner:
                log.warning("Player " + str(winner.name) + " has won!")
                break
            self.state['round'] += 1

    def legal(self, card):
        """ Check that a move is legal """
        raise NotImplemented("Cannot check legality without a specific game!")

    def update_state(self, card):
        """ Update internal game state based on a played card """
        raise NotImplemented("Cannot update_state without a specific game!")

    def update_players(self):
        """ Construct an update message and send it to all players """
        raise NotImplemented("Cannot update_players without a specific game!")

    def finish(self):
        """ Cleanup the game """
        raise NotImplemented("Cannot finish without a specific game!")

    def victory(self, player):
        """ Determine that a player has won the game """
        raise NotImplemented("Cannot declare victory without a specific game!")
