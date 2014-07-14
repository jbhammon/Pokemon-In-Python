import Creature
import random

def Sequence(faster, slower):
	#new logic here
	if faster.mine:
		myAttack(faster, slower)
		if slower.health > 0:
			attack(slower, faster)
	else:
		attack(faster, slower)
		if slower.health > 0:
			myAttack(slower, faster)

def attack(attacker, defender):
	print "It's " + attacker.name + " turn."
	attackType = random.randint(1, 100)
	if (attackType < 25):
		# healing
		print attacker.name + " healed itself."
		medicine = random.randint(1, 15)
		attacker.health = attacker.health + medicine
		if (attacker.health > 100):
			attacker.health = 100
		print attacker.name + " healed itself " + str(medicine) + " HP, and its health is now " + str(attacker.health)
	elif(attackType < 75):
		# attack
		print attacker.name + " used a normal attack."
		damage = random.randint(1, 15)
		defender.health = defender.health - damage
		if (defender.health < 0):
			defender.health = 0
		print attacker.name + " did " + str(damage) + " damage and " + defender.name + "'s health is now " + str(defender.health)
	else:
		# critical hit
		print attacker.name + " landed a critical hit!"
		damage = random.randint(10, 30)
		defender.health = defender.health - damage
		if (defender.health < 0):
			defender.health = 0
		print attacker.name + " did " + str(damage) + " damage and " + defender.name + "'s health is now " + str(defender.health)
	print "\n"

def myAttack(attacker, defender):
	print "It's " + attacker.name + " turn."
	while True:
		movePrint(attacker)
		choice = raw_input("Which move should " + attacker.name + " use? ")
		move = -1
		for i in range(4):
			# change so user doesn't have to use a leading space for this to be true
			if choice == attacker.moves[i].name:
				move = i
				break
		if move == -1:
			print attacker.name + " doesn't know that move!"
			continue
		else:
			break
	attacker.moves[move].remainingPP = attacker.moves[move].remainingPP - 1
	print attacker.name + " used " + attacker.moves[move].name + "!"
	attackType = random.randint(1, 100)
	if(attackType < 75):
		# attack
		damage = random.randint(1, 15)
		defender.health = defender.health - damage
		if (defender.health < 0):
			defender.health = 0
		print attacker.name + " did " + str(damage) + " damage and " + defender.name + "'s health is now " + str(defender.health)
	else:
		# critical hit
		print attacker.name + " landed a critical hit!"
		damage = random.randint(10, 30)
		defender.health = defender.health - damage
		if (defender.health < 0):
			defender.health = 0
		print attacker.name + " did " + str(damage) + " damage and " + defender.name + "'s health is now " + str(defender.health)
	print "\n"



def movePrint(pokemon):
	default = 15
	cell0 = "|" + pokemon.moves[0].name + " " + str(pokemon.moves[0].remainingPP) + "/" + str(pokemon.moves[0].totalPP) + " |"
	cell1 = " " + pokemon.moves[1].name + " " + str(pokemon.moves[1].remainingPP) + "/" + str(pokemon.moves[1].totalPP) + " |"
	cell2 = "|" + pokemon.moves[2].name + " " + str(pokemon.moves[2].remainingPP) + "/" + str(pokemon.moves[2].totalPP) + " |"
	cell3 = " " + pokemon.moves[3].name + " " + str(pokemon.moves[3].remainingPP) + "/" + str(pokemon.moves[3].totalPP) + " |"



	
	print "+----------------------------+"
	print "|" + pokemon.moves[0].name + " " + str(pokemon.moves[0].remainingPP) + "/" + str(pokemon.moves[0].totalPP) + " | " + pokemon.moves[1].name + " " + str(pokemon.moves[1].remainingPP) + "/" + str(pokemon.moves[1].totalPP) + " |"
	print "+----------------------------+"
	print "|" + pokemon.moves[2].name + " " + str(pokemon.moves[2].remainingPP) + "/" + str(pokemon.moves[2].totalPP) + " | " + pokemon.moves[3].name + " " + str(pokemon.moves[3].remainingPP) + "/" + str(pokemon.moves[3].totalPP) + " |"
	print "+----------------------------+"