'''
Game set-up for 3-player Kuhn Poker, A game takes three players.
'''

from player import *

class Game:

    def __init__(self, you, opponent1, opponent2):
        you.new_round()
        opponent1.new_round()
        opponent2.new_round()
        deck = dict([('jack', 0), ('queen', 1), ('king', 2), ('ace', 3)])


#There are Three players
#single round of betting
#mandatory bet at the beginning
# we need to build three player objects
#need to play rounds
