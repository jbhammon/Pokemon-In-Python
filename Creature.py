# Copyright (c) 2014 Jackson B Hammond

class Pokemon(object):

	def __init__(self):
		self.name = ""

		self.health = 0

		self.attack = 0
		self.specialAttack = 0
		self.defence = 0
		
		self.specialDefense = 0
		self.speed = 0

		self.moves = []
		self.mine = False

class Move(object):

	def __init__(self):
		self.name = ""
		self.totalPP = 0
		self.remainingPP = 0