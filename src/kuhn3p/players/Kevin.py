import random
from kuhn3p import betting, deck, Player

class Kevin(Player):
	def __init__(self):
		self.counter = 0
		#Nash
		self.A = 1
		self.dic = {}
		for i in range(13):
			for card in range(4):
				self.dic[(i,card)] = []
		self.B = 0

		self.c1 = random.randint(0,999)
		self.c2 = random.randint(self.c1, 1000)

		self.C = 0
		self.lastGameInfo = []

	def act(self, state, card):
		self.counter = self.counter + 1
		if(self.counter > self.c1 and self.counter < self.c2):
			self.C = 1
		else:
			self.C = 0

		probFunc = (6/10)* random.random() + (2/10) * self.B + (2/10) * self.C
		if betting.can_bet(state):
    		    if card == deck.ACE:
		            return betting.BET
                elif card == deck.KING:
                    if(random.Random() < (probFunc)):
                        return betting.BET
                    else:
                        return betting.CHECK
                elif card == deck.QUEEN:
                    if(random.Random() < (probFunc - 1/3)):
		                return betting.BET
                    else:
                        return betting.CHECK
		        
		else:
		    if card == deck.ACE or card == deck.KING:
	    		return betting.CALL
	    	    else:
			if(self.C == 1):
                            if(random.Random() < random.Random()):
			    	return betting.CALL
			    else:
		    		return betting.FOLD
			else:
			    return betting.FOLD


	def end_hand(self, position, card, state, shown_cards):
		player = betting.actor(position) + 1

		if (betting.folded(state, player)):
			print("Player: " + str(player) + "has folded with card " + str(card))
			print("Player: " + str(player) + "has lost " + str(betting.pot_contribution(state, player)))
		else:
			print("Player: " + str(player) + " is in showdown with card " + str(card))
		if(card == 3):
    			print("Player: " + str(player) + "has won the pot! " + str(betting.pot_size(state)))

	def __str__(self):
		return 'Kevin The Rubber Duck'
