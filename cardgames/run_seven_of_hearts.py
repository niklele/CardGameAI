import logging as log
import random
from seven_of_hearts.seven_of_hearts import SevenOfHearts
from seven_of_hearts.seven_of_hearts_player import HumanPlayer
from seven_of_hearts.seven_of_hearts_ai import RandomPlayer, HeuristicPlayer

if __name__ == '__main__':
    # setup logging library to avoid console spam
    log.basicConfig(format='%(levelname)s: %(message)s', level=log.WARNING)

    game = SevenOfHearts()

    # human players
    # game.add_player(HumanPlayer("Human 1", game))
    # game.add_player(HumanPlayer("Human 2", game))

    # random players
    game.add_player(RandomPlayer("Random 1", game))
    game.add_player(RandomPlayer("Random 2", game))

    # Heuristic AI
    h_players = [HeuristicPlayer("Heuristic 1", game),
                 HeuristicPlayer("Heuristic 2", game)]
    map(lambda h: game.add_player(h), h_players)

    game.print_players()

    # run multiple games
    ROUNDS = 30
    for i in xrange(ROUNDS):
        try:
            game.setup()
            game.run()
            game.finish()

            # shuffle starting position
            random.shuffle(game.players)
        except KeyboardInterrupt:
            exit(1)

    h_victories = sum(h.victories for h in h_players)
    expected = float(len(h_players))/len(game.players)
    ratio = (float(h_victories)/ROUNDS - expected) / expected
    log.critical("Heuristic improvement percentage: " + str(ratio) + " after " + str(ROUNDS) + " rounds")
    # -0.05 after 200 rounds with 2 random, 2 heuristic
