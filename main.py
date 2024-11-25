# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main


#play(player, quincy, 1000) # Cycle strat
#play(player, mrugesh, 1000) # Most frequent strat
#play(player, kris, 1000) # Prev play strat
#play(player, abbey, 1000) # Markov strat (best of the four)

# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)

# Uncomment line below to run unit tests automatically
main(module='test_module', exit=False)