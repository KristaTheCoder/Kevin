import random
from kuhn3p import betting, deck, Player

class Kevin(Player):
	def __init__(self):
		counter = 0
		#Nash
		self.A = 1
		self.dic = {}
		for i in range(13):
			for card in range(4):
				self.dic[zip(i,card)] = []
		self.B = 0

		self.c1 = random.Random()*1000
		self.c2 = random.Random()*1000

		if(self.c1 >= self.c2):
			temp = self.c1
			self.c1 = self.c2
			self.c2 = temp
		self.C = 0
		self.lastGameInfo = []

	def act(self, state, card):
		counter = counter + 1
		if(counter > self.c1 and counter < self.c2):
			self.C = 1
		else:
			self.C = 0

		probFunc = (6/10) * self.A + (2/10) * self.B + (2/10) * self.C
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
                    return betting.CALL
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

    def set_B(self):
        pass

	def __str__(self):
		return 'Kevin The Rubber Duck'
