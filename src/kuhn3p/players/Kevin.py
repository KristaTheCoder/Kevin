import random
from kuhn3p import betting, deck, Player

class Kevin(Player):
	def __init__(self):
		pass

	def act(self, state, card):
		if betting.can_bet(state):
    		if card == deck.ACE:
				return betting.BET
			else:
				return betting.CHECK
			else:
				return betting.BET
		else:
			if card == deck.ACE:
				return betting.CALL
			else:
				return betting.FOLD
    			
		
		return betting.FOLD

	def __str__(self):
		return 'Always Fold'
