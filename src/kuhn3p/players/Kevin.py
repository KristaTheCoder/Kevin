import random
from kuhn3p import betting, deck, Player

class Kevin(Player):
	def __init__(self):
		pass

	def act(self, state, card):
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
                        return betting.FOLD
		else:
			if card == deck.ACE or card == deck.KING:
				return betting.CALL
			else:
				return betting.FOLD
    			
	    

	def __str__(self):
		return 'Kevin 2.0'
