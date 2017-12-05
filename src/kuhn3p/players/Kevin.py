import random
from kuhn3p import betting, deck, Player

class Kevin(Player):
	def __init__(self):
		#
		# there are 4 betting situations for any player:
		#   1) it is checked to them
		#   2) it was raised by the person on their right
		#   3) it was raised two to their right, and the middle player called
		#   4) it was raised two to their right, and the middle player folded
		#
		# => there are 4*3 = 12 betting decisions states
		#
		# in situation 1, the player can bet or check.
		# in situation 2, the player can call or fold.
		#
		# in situation 3 and 4, any action ends the betting
		# in situation 1 for player 3, checking ends the betting
		#
		# =>
		self.q = [0] * 4
		self.q = [self.q] * 4 * 4
		self.R = [None] * 4
		self.R = [self.R] * 4 * 4
		self.gamma = 0.8
		for x in range(4):#possible situations
			for k in range(1,5):
				for y in range(4):#given the first situation
					if x == 0:#situation 1
						if y == 0: #this is a bet
							self.R[x][y*k] = -1
						if y == 1: #this is a check
							self.R[x][y*k] = 0
					if x == 1 #situation 2
						if y == 2:#call
							self.R[x][y*k] = -1
						if y == 3:#fold
							self.R[x][y*k] = 0
					if x >= 2:#situation 3
						if y == 2:#call
							self.R[x][y*k] = -1
						if y == 3:#folded
							self.R[x][y*k] = 0
		print self.R



	def act(self, state, card):
		if state == 0:
			if card == deck.JACK:
				return betting.CHECK
			elif card == deck.ACE:
				return betting.BET
			else:
				if random.Random() < 1/2:
					return betting.CHECK
				else:
					return betting.BET
		current_state = state * card
        self.q[current_state]
















		if betting.can_bet(state):
    		    if card == deck.ACE:
		        return betting.BET
                    elif card == deck.KING:
                        if(random.Random() < (2/3)):
                            return betting.BET
                        else:
                            return betting.CHECK
                    elif card == deck.QUEEN:
                        if(random.Random() < (1/3)):
                            return betting.BET
                        else:
                            return betting.CHECK
		    else:
                        return betting.CALL
		else:
			if card == deck.ACE or card == deck.KING:
				return betting.CALL
			else:
				return betting.FOLD



	def __str__(self):
		return 'Kevin 2.0'
