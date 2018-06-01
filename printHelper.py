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
	return list(index)

#
# Intro function that introduces the players and their matchups and win rates if provided
# players := replay.clients
#
def printIntro(players): 


	# introduces the commentator and the start
	introLine()



#
# Introductory Line 
#
def introLine():

	# variable for holding all the intro lines that will be spoken at the start of the game
	introLines = 
	[
	"Hey everyone and welcome to my live commentatory of the best game ever. My name is AI and yes I am very intelligent",
	"Hello and welcome to Starcraft, a real-time strategy game from Blizzard Entertainment. I’m Mr. AI, and I’ll be the commentator for today.",
	"Hi everyone. I’d like to welcome you all to another wonderful day in the world of Blizzard Entertainment. This is an AI commentator bot designed to enhance your viewing experience."
	]


	# picks one random element from the list
	toPrint = pickRandom(introLines)

	# PRINT



#
# Commentate on human or not as well as number of players and races 
# team_id and is_human
# 
def callTeamIntro(players):

	# will hold the number of players on each team
	playersOnEachTeam = len(players)/2

	# will hold number of humans
	humans = 0
	tempTeamId = 1

	# going through list of players
	for player in players:

		# checking if this team has humans
		if(player.team_id == tempTeamId and player.is_human == True):
			humans += 1
			tempTeamId += 1

	if(humans == 0):
		continue # call cpuVcpu
	elif(humasn  == 1):
		continue # call userVcpu
	else:
		continue # call userVuse


		
