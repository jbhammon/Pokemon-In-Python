class Pokemon(object):

	def __init__(self):
		self.name = ""
		self.health = 0
		self.speed = 0
		self.moves = []
		self.mine = False

class Move(object):

	def __init__(self):
		self.name = ""
		self.totalPP = 0
		self.remainingPP = 0