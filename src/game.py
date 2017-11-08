'''
Game set-up for 3-player Kuhn Poker, A game takes three players.
'''

from player import *

class Game:
    #TODO ask professor how first player is picked in the poker game
    def __init__(self):
        '''Start a new game with a full deck and everyone playing'''
        you.new_round()
        opponent1.new_round()
        opponent2.new_round()
        self.deck = dict([('jack', 0), ('queen', 1), ('king', 2), ('ace', 3)])
        play_order = {'first' : you , 'second' : opponent1 , 'third' : opponent2}

    def set_play_order(self):
        ''' Come up with some way of deciding who is playing first aside from'''
        self.play_order = play_order

    # For simplicity in building game we will assume everyone joins the game.
    def deal(self):
        #every player bets 1 chip to enter game
        you.antes(1)
        opponent1.antes(1)
        opponent2.antes(1)

        you.set_card(self.deck['jack'])
        opponent1.set_card(self.deck['queen'])
        opponent2.set_card(self.deck['king'])

#single round of betting
#mandatory bet at the beginning
# we need to build three player objectss
#need to play rounds


you = Player()
opponent1 = Player()
opponent2 = Player()
x = Game()
x.deal()

print you.show_hand()
print opponent1.show_hand()
print opponent2.show_hand()
