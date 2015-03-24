# CardGameAI
AI for some playing card games. See below for games and progress.

Uses [cardsource.](https://github.com/davidfischer/cardsource)

## Seven of Hearts
Seven of Hearts is an Indian game known as "Badam Saath" and also known as [Sevens](https://en.wikipedia.org/wiki/Sevens_(card_game)).
It is a [shedding card game](https://en.wikipedia.org/wiki/Shedding-type_game) where players take turns to play cards.
If they have no legal moves, they have to pass. The first player to finish all of their cards wins.

The goal is to build up consecutive arrays of each suit, centered on the 7 of each suit, going from Ace up to King. A card can only be played if the card 1 closer to Seven of that suit has already been played. That is, Jiub can only play his 4 of Spades if Caius has previously played his 5 of Spades. A Seven of any suit can be played at any time.

### AI
I made a random player which chooses randomly from all legal moves as a baseline opponent, and another that uses a simple heuristic to choose which card to play each round. The heuristic is the sum of the card's "distance" from 7 and its potential to help with playing other cards in hand in future rounds. This is approximated by calculating the percentage of cards in hand in each of the 8 "blocks" of the game: above and below the Seven of each suit. The two values are equally weighted, and the the card with the highest sum is chosen.

I've found that because there is not much choice in which move to make, the heuristic AI only barely outperforms the random player against humans and other AI. The initial randomness from shuffling the deck dominates any choice made by a player.
