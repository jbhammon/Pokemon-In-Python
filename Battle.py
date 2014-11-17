# Copyright (c) 2014 Jackson B Hammond

import Creature
import Sequence

def pokemonBuilder(source):
	pokemon = Creature.Pokemon()
	
	line = source.readline().rstrip()
	while line == "":
		line = source.readline().rstrip()

	pokemon.name = line
	pokemon.health = int(source.readline())
	pokemon.speed = int(source.readline())
	return pokemon

def moveBuilder(pokemon, source):
	for i in range(4):
		move = Creature.Move()
		row = source.readline().split()
		for j in range((len(row) - 1)):
			move.name = move.name + row[j] + " "
		move.name = move.name.rstrip()
		move.totalPP = int(row[len(row) - 1])
		move.remainingPP = int(move.totalPP)
		pokemon.moves.append(move)

data = open("data.txt", "r")

# Red's stats
red = pokemonBuilder(data)
red.mine = True

# Red's moves
moveBuilder(red, data)

# Blue's stats
blue = pokemonBuilder(data)

# Blue's moves
moveBuilder(blue, data)

# Start of the Battle
print("\n")
print("Enemy " + blue.name + " attacked!\n")
print("Go, " + red.name + "!\n")

if(red.speed > blue.speed):
	print(red.name + " is faster than " + blue.name + "!\n")
	while (red.health > 0 and blue.health > 0):
		Sequence.Sequence(red, blue)

elif(red.speed < blue.speed):
	print(blue.name + " is faster than " + red.name + "!\n")
	while (red.health > 0 and blue.health > 0):
		Sequence.Sequence(blue, red)

else:
	print("Their speeds are exactly the same!\n")
	coin = random.randint(1,10)
	if (coin < 6):
		while (red.health > 0 and blue.health > 0):
			Sequence.Sequence(red, blue)
	else:
		while (red.health > 0 and blue.health > 0):
			Sequence.Sequence(blue, red)

if (red.health <= 0):
	print(red.name + " fainted, " + blue.name + " wins!")
else:
	print(blue.name + " fainted, " + red.name + " wins!")


data.close()