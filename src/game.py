'''
Game set-up for 3-player Kuhn Poker, A game takes three players.
The person of interest is kevin, we always want kevin to win. 
'''

from player import *

class Game:
    #TODO ask professor how first player is picked in the poker game
    def __init__(self):
        '''Start a new game with a full deck and everyone playing'''
        kevin.new_round()
        opponent1.new_round()
        opponent2.new_round()
        self.pot = 0 # winnings at end of game
        self.deck = dict([('jack', 0), ('queen', 1), ('king', 2), ('ace', 3)])
        play_order = {'first' : kevin, 'second' : opponent1, 'third' : opponent2}

    def set_play_order(self):
        #FIXME Come up with some way of deciding who is playing first aside from
        self.play_order = play_order

    def play_round(self):
        #FIXME design ways to pick actions for what each player should do
        #THIS IS THE AI PART
        play_order['first'].bet(1)
        self.pot = self.pot + 1

        play_order['second'].bet(1)
        self.pot = self.pot + 1

        play_order['third'].bet(1)
        self.pot = self.pot + 1

    def deal(self):
        #every player bets 1 chip to enter game
        kevin.antes(1)
        opponent1.antes(1)
        opponent2.antes(1)
        self.pot = 3

        kevin.set_card(self.deck['jack'])
        opponent1.set_card(self.deck['queen'])
        opponent2.set_card(self.deck['king'])

    #FIXME undo the hard coding
    def winner(self):
        #TODO for all players in game check their card

        #TODO find the max card

        #TODO find player with max card and declare the winner

        winner = opponent2
        winner.win(self.pot)
        self.pot = 0



### This section is just to play with to maek sure the game works.
kevin = Player()
opponent1 = Player()
opponent2 = Player()
x = Game()
x.deal()

print kevin.show_hand()
print opponent1.show_hand()
print opponent2.show_hand()

x.winner()
print opponent2.get_money()
