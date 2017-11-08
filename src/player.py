'''
Class for players who can play the game, and actions they can take in the game
'''

class Player(object):
    """Build a new player"""
    def __init__(self, card):
        superPlayer, self.__init__()
        self.card = card #expand this so that the same player can play multiple times
        self.money = 1000000
        self.inGame = True

    def antes(chip):
        #Enter the game by betting a first chip
        self.money = self.money - chip

    def bet(chip):
        self.money = self.money - chip

    def check():
        bet(0)

    def fold():
        self.inGame = False

    def set_card(card):
        ''' This method is for when the same player participates in multiple games'''
        self.card = card

    #add all the getters

    def show_hand():
        return self.card

    def is_playing():
        return self.inGame

    def get_money():
        return self.money
