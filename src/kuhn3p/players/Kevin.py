import random
from kuhn3p import betting, deck, Player

class Kevin(Player):
	def __init__(self):
		pass

	def act(self, state, card):
		return betting.FOLD

	def __str__(self):
		return 'Always Fold'
