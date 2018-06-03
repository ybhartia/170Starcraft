# A printing library that prints all the desired output for the commentator

from random import randint

#
# random element picker returns one element randomly picked from a list
#
def pickRandom(list):

	# variables for the range of random numbers in the list
	lower = 0
	upper = len(list) - 1

	# pick an index such as lower <= index <= upper randomly
	index = randint(lower, upper)

	# returning a random number from that list of numbers
	return list[index]

#
# Intro function that introduces the players and their matchups and win rates if provided
# players := replay.clients
#
def getIntro(players):


	# introduces the commentator and the start
	introLines = getIntroLines()
	intro = pickRandom(introLines)
	return intro

#
# Introductory Line 
#
def getIntroLines():
	# variable for holding all the intro lines that will be spoken at the start of the game
	introLines =[]
	introLines  += [ "Hey everyone and welcome to my live commentatory of the best game ever. My name is AI and yes I am very intelligent"]
	introLines += [ "Hello and welcome to Starcraft, a real-time strategy game from Blizzard Entertainment."]
	introLines += ["I am Mr. AI, and I will be the commentator for today."]
	introLines += [ "Hi everyone. I would like to welcome you all to another wonderful day in the world of Blizzard Entertainment. This is an AI commentator bot designed to enhance your viewing experience."]
	return  introLines

#
# Get a random line from a list of lines regarding completion of unit prodcution
# This is a response to a UnitBornEvent()
# Not sure if the productions of machinary units (vehicles) are considered
# 
# player: the player that the unit belong to
# unit: the unit being produced
#
def getUnitBornLine(player, unit):
	listOfLines = getUnitBornLines(player, unit)
	line = pickRandom(listOfLines)
	return line

#
# Generates a list of lines regarding a unit's production has been 'born'.
# This is a response to a UnitBornEvent().
# Not sure if the productions of machinary units (vehicles) are considered
# 
# player: the player that the unit belong to
# unit: the unit being produced
#
def getUnitBornLines(player, unit):
	lines = []
	lines += [ player + "'s " + unit + " is ready to go." ]
	lines += [ unit + "'s production is completed for " + player + "." ]
	lines += [ "What will " + player + " do with that " + unit + "?"]
	lines += [ "Hey " + player + " your " + unit + " is here!"]
	return lines


#
# Get a random line from a list of lines regarding a unit's dead
# Assume the unit actually died and not morph into another unit
# This is a response to UnitDieEvent()
#
def getUnitDieLine(player, unit):
	listOfLines = getUnitDieLines(player, unit)
	line = pickRandom(listOfLines)
	return line

#
# Generates a list of lines regarding a unit's production has been completed
# Assume the unit actually died and not morph into another unit
#
def getUnitDieLines(player, unit):
	lines = []
	lines += [ player + "'s " + unit + " has been destroyed!"]
	lines += [ player + " has lost " + add_a_or_an(unit, False) + "." ]
	lines += [ add_a_or_an(unit, True) + " has died, " + player + " should get a new one."]
	lines += [ player + " doesn't take a good care of that " + unit + ". It's dead."]
	return lines




#
# add 'a' or 'an' in front of the noun, returning a string containing 'a' or 'an' concaternated with the noun
# @cap is a boolean, indicating capitalization
#
def add_a_or_an(noun, cap):
	if noun[0] == 'a' or noun[0] == 'e' or noun[0] == 'i' or noun[0] == 'o' or noun[0] == 'u':
		return ("An " if cap else 'an ') + noun
	else:
		return ("A " if cap else 'a ') + noun




# Commentate on human or not as well as number of players and races 
# team_id and is_human
# #
# def callTeamIntro(players):
#
# 	# will hold the number of players on each team
# 	playersOnEachTeam = len(players)/2
#
# 	# will hold number of humans
# 	humans = 0
# 	tempTeamId = 1
#
# 	# going through list of players
# 	for player in players:
#
# 		# checking if this team has humans
# 		if(player.team_id == tempTeamId and player.is_human == True):
# 			humans += 1
# 			tempTeamId += 1
#
# 	if(humans == 0):
# 		continue # call cpuVcpu
# 	elif(humasn  == 1):
# 		continue # call userVcpu
# 	else:
# 		continue # call userVuse


		
