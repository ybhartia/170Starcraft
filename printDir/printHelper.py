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
def getIntro():


	# introduces the commentator and the start
	introLines = getIntroLines()
	intro = pickRandom(introLines)
	return intro


def getClosing():
	listOfLines = getClosingLines()
	line = pickRandom(listOfLines)
	return line
	
def getClosingLines():
	lines = []
	lines += ["That's it folks. I hope you enjoyed my commentary!"]
	lines += ["A truly interesting match! I'm done here, so so are you."]
	lines += ["My commentary was next level right? I'm here all week."]
	lines += ["Match over! Have a nice day."]


def getAIPrint(outcome, players):
	team1 = []
	team2 = []
	for player in players:
		if player.team_id == 1:
			team1.append(player.name)
		else:
			team2.append(player.name)
	matchup1 = team1[0]
	matchup2 = team2[0]
	for i in range(1,len(team1)):
		matchup1 += ", " + team1[i]
		matchup2 += ", " + team2[i]

	if outcome > 3:
		return dominatedLine(matchup1, matchup2)
	elif outcome > 0:
		return winningLine(matchup1, matchup2)
	elif outcome == 0:
		return closeMatch(matchup1, matchup2)
	elif outcome < -3:
		return dominatedLine(matchup2, matchup1)
	else:
		return winningLine(matchup2, matchup1)


def dominatedLine(team1, team2):
	listOfLines = getDominatedLines(team1, team2)
	line = pickRandom(listOfLines)
	return line

def winningLine(team1, team2):
	listOfLines = getWinningLines(team1, team2)
	line = pickRandom(listOfLines)
	return line


def closeMatch(team1, team2):
	listOfLines = getCloseMatchLines(team1, team2)
	line = pickRandom(listOfLines)
	return line


def getDominatedLines(team1, team2):
	lines = []
	lines.append(team1 + " is crushing " + team2 + "!")
	lines.append(team2 + " is getting dominated by " + team1 + "!")
	lines.append("It's looking really bleak for " + team2 + ".")
	lines.append("At this rate, " + team1 + " will win pretty soon against " + team2 + "!")
	return lines

def getWinningLines(team1, team2):
	lines = []
	lines.append(team1 + " is pulling ahead of " + team2 + ".")
	lines.append(team2 + " is winning! Psych lmao! Actually " + team1 + " is winning.")
	lines.append("It's getting harder for " + team2 + " to stay in the game.")
	lines.append("The scales are slipping towards" + team1 + ".")
	return lines

def getCloseMatchLines(team1, team2):
	lines = []
	lines.append(team1 + " and " + team2 + " are head to head!")
	lines.append("What do you call a flammable piece of wood sitting right next to you? It's a close match!")
	lines.append("I guess we need a DNA test to differentiate this one. The teams look pretty identical!")
	lines.append(team1 + " and " + team2 + " are doing pretty well against each other. It's gonna be an exciting one!")
	return lines

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
# player: string contains the player's name that the unit belong to
# unit: string contains unit's type being produced
#
def getUnitBornLine(player, unit, event):
	listOfLines = getUnitBornLines(player, unit, event)
	line = pickRandom(listOfLines)
	return line

#
# Generates a list of lines regarding a unit's production has been 'born'.
# This is a response to a UnitBornEvent().
# Not sure if the productions of machinary units (vehicles) are considered
# 
# player: string contains the player's name that the unit belong to
# unit: string contains unit's type being produced
#
def getUnitBornLines(player, unit, event):
	# more than one unit made togther
	if(len(event) > 4):
		event[4] = str(event[4])
		lines = []
		lines += [ player + "'s " + event[4] + " " + unit + "s are ready to go." ]
		lines += [ "The production of " + event[4] +" "+ unit + "s is completed for " + player + "." ]
		lines += [ "What will " + player + " do with " + event[4] + " new " + unit + "s?"]
	else:
		lines = []
		lines += [ player + "'s " + unit + " is ready to go." ]
		lines += [ unit + "'s production is completed for " + player + "." ]
		lines += [ "What will " + player + " do with that new " + unit + "?"]
		lines += [ "Hey " + player + " your " + unit + " is here!"]
	return lines


#
# Get a random line from a list of lines regarding a unit's dead
# Assume the unit actually died and not morph into another unit
# This is a response to UnitDieEvent()
# 
# player: string contains the player's name that the unit belong to
# unit: string contains unit's type being produced
#
def getUnitDieLine(player, unit, event):
	listOfLines = getUnitDieLines(player, unit, event)
	line = pickRandom(listOfLines)
	return line

#
# Generates a list of lines regarding a unit's production has been completed
# Assume the unit actually died and not morph into another unit
# 
# player: string contains the player's name that the unit belong to
# unit: string contains unit's type being produced
#
def getUnitDieLines(player, unit, event):
	if(len(event) > 4):
		num = str(event[4])
		lines = []
		lines += [ player + "'s " + num + makePlural(unit)+ " have been destroyed!"]
		lines += [ player + " has lost " + num + makePlural(unit) + "." ]
		lines += [ num + makePlural(unit) + " have died, " + player + " should get new ones."]
		lines += [ player + " doesn't take a good care of those " + num + makePlural(unit) + ". They're dead."]
	else:
		lines = []
		lines += [ player + "'s " + unit + " has been destroyed!"]
		lines += [ player + " has lost " + add_a_or_an(unit, False) + "." ]
		lines += [ add_a_or_an(unit, True) + " has died, " + player + " should get a new one."]
		lines += [ player + " doesn't take a good care of that " + unit + ". It's dead."]
	return lines

def getUpgradeCompleteLine(player, upgrade, unit, event):
	listOfLines = getUpgradeCompleteLines(player, upgrade, unit, event)
	line = pickRandom(listOfLines)
	return line

def getUpgradeCompleteLines(player, upgrade, unit, event):

	if(len(event) > 4):
		num = str(event[4])
		lines = []
		lines += [ num + makePlural(upgrade) + " upgrades completed for " + player + "." ]
		lines += [ num + makePlural(upgrade) + " upgrades are done. More power to " + player + "!"]
		lines += [ player + " now has " + num + makePlural(upgrade) + "." ]
	else:
		lines = []
		lines += [ upgrade + " upgrade completed for " + player + "." ]
		lines += [ upgrade + " upgrade is done. More power to " + player + "."]
		lines += [ player + " now has " + upgrade + "." ]
	if unit != "":
		lines += [ player + "'s " + unit + "'s power has been increased." ]
	return lines



def getTypeChangeLine(player, unit, faction, event):
	listOfLines = getTypeChangeLines(player, unit, faction)
	line = pickRandom(listOfLines)
	return line

#
# player, unit, previous, faction are strings, previous is the name of previous unit
# isBuilding is a boolean 
#
def getTypeChangeLines(player, unit, faction): 
	lines = []
	if faction == "Terran":
		lines +=  [player + " has upgraded " + unit]
		lines += [ player + "'s " + unit + " has put on his big boy pants!"]
	elif faction == "Zerg":
		lines += [ player + " has morphed his " + unit ]
		lines += [ player + "'s unit grown up to be a " + unit + "!"]
		
	elif faction == "Protoss":
		lines += [ player + " has upgraded " + unit]
		lines += [ player + "'s " + unit + " has put on his big alien boy pants!"]
	return lines

#
# This can be used to replace get random line functions that only requires 2 parameters
# Example: to call getUnitBornLine(player, unit)
#		Calls getLine(player, unit, getUnitBornLine)
#
def getLine(player, unit, function):
	listOfLines = function(player, unit)
	line = pickRandom(listOfLines)
	return line

#
# add 'a' or 'an' in front of the noun, returning a string containing 'a' or 'an' concaternated with the noun
#
# @cap is a boolean, indicating capitalization
#
def add_a_or_an(noun, cap):
	if noun[0] == 'a' or noun[0] == 'e' or noun[0] == 'i' or noun[0] == 'o' or noun[0] == 'u':
		return ("An " if cap else 'an ') + noun
	else:
		return ("A " if cap else 'a ') + noun

#
# make unit plural
#
# @cap is a boolean, indicating capitalization
#
def makePlural(noun):
	return " " + noun + "s"

#
# Check if unit should be ignore (if it dies or borns)
#
# @unit: string contains the name of the unit
#
def shouldIgnore(unit):
	insignificantUnits = [
		"Larva"
	]
	if unit in insignificantUnits:
		return True
	return False


# print getTypeChangeLine("Hung", "Banneling", "Zergling", "Zerg", False)
# print getUpgradeCompleteLine("Hung", "Zerg Attact Increase", "Zergling")
def getHumans(humans):
	if humans == 1:
		return "1 human"
	elif humans > 1:
		return str(humans) + " humans"
	return ""


def getAI(numAI):
	if numAI > 0:
		return " and " + str(numAI) + " AI"
	return ""
# Commentate on human or not as well as number of players and races 
# team_id and is_human
# #
def getTeamIntro(players):

	# will hold the number of players on each team
	playersOnEachTeam = len(players)/2

	# will hold number of humans

	team1AI = 0
	team2AI = 0
	team1Humans = 0
	team2Humans = 0
	team1 = []
	team2 = []

	# going through list of players
	for player in players:
		# separating players into teams and also getting data of number of humans and ai on each team
		if player.team_id == 1:
			team1.append(player.name)
			if player.is_human:
				team1Humans += 1
		else:
			team2.append(player.name)
			if player.is_human:
				team2Humans += 1

	teamIntro = []
	teamIntro += ["It's gonna be an interesting match with " + getHumans(team1Humans) +  getAI(team1AI) + " on Team 1 against " 
	+ getHumans(team1Humans) +  getAI(team1AI) + " on Team 2!"]
	matchup1 = team1[0]
	matchup2 = team2[0]
	for i in range(1,len(team1)):
		matchup1 += ", " + team1[i]
		matchup2 += ", " + team2[i]

	teamIntro += ["We're gonna see " + matchup1 + " VS " + matchup2 + "!"] 

	strteamIntro = '\n'.join(teamIntro)
	print strteamIntro
	return strteamIntro





		
