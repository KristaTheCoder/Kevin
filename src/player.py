'''
Class for players who can play the game, and actions they can take in the game
'''

class Player:
    """Build a new player"""
    def __init__(self, card):
        self.card = card #expand this so that the same player can play multiple times
        self.money = 1000000
        self.inGame = True

    def antes(self, chip):
        #Enter the game by betting a first chip
        self.money = self.money - chip

    def bet(self, chip):
        self.money = self.money - chip

    def check(self):
        bet(0)

    def fold(self):
        self.inGame = False

    def set_card(self, card):
        ''' This method is for when the same player participates in multiple games'''
        self.card = card

    def new_round(self):
        self.inGame = True

    #add all the getters

    def show_hand(self):
        return self.card

    def is_playing(self):
        return self.inGame

    def get_money(self):
        return self.money
