import logging as log
import cardsource as cs
from seven_of_hearts.seven_of_hearts import SevenOfHearts
from seven_of_hearts.seven_of_hearts_player import HumanPlayer
from seven_of_hearts.seven_of_hearts_ai import RandomPlayer, HeuristicPlayer

if __name__ == '__main__':
    log.basicConfig(format='%(levelname)s: %(message)s', level=log.DEBUG)

    game = SevenOfHearts(cs.Deck())

    # 2 human players
    # game.add_player(HumanPlayer("Human 1", game))
    # game.add_player(HumanPlayer("Human 2", game))

    # 4 random players
    # game.add_player(RandomPlayer("Random 1", game))
    # game.add_player(RandomPlayer("Random 2", game))
    # game.add_player(RandomPlayer("Random 3", game))
    # game.add_player(RandomPlayer("Random 4", game))

    # 1 human and 1 Heuristic AI
    game.add_player(HumanPlayer("Human 1", game))
    game.add_player(HeuristicPlayer("Heuristic 2", game))

    # run a single game
    game.setup()
    game.run()
    game.finish()