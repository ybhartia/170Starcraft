from __future__ import print_function
import sc2reader
from sc2reader.engine.plugins import APMTracker

#
# This is the currently completed format of the input layer
# [time, isProtoss, isZerg, isTerran, UnitBornEvent, UnitDiedEvent, UnitTypeChangeEvent, UpgradeCompleteEvent, UpdateTargetUnitCommandEvent, UnitOwnerChangeEvent, ResourceRequestEvent, ResourceRequestFulfillEvent, ResourceRequestCancelEvent, PlayerLeaveEvent, result]
#


#
# The player data that is used to initialize the input vectors
#
class Player:
    def __init__(self):
        self.teamid = "" # Probably an int
        self.playerName = "" # String
        self.protoss = 0 # 0 or 1
        self.zerg = 0 # 0 or 1
        self.terran = 0 # 0 or 1
        self.result = -1 # 0 or 1, if -1 then it has not been initialized or was not found


#
# Temporary debugger function:
# Helps see player data
#
def printPlayers(players):
    for player in players:
        print("____________________________________")
        print("Team ID = " + str(player.teamid))
        print("Player Name = " + player.playerName)
        print("isProtoss = " + str(player.protoss))
        print("isZerg = " + str(player.zerg))
        print("isTerran = " + str(player.terran))
        print("Win or Loss = " + str(player.result))

    print("____________________________________")


#
# Reads basic data from the players array and initializes their values
# We want these values to be accurate and these values are constant 
# Through out the code so we do not need to change these values
# EVER
#
def initiatePlayers(replay):
    players = []
    for player in replay.people:
        obj = Player()
        name = str(player).split()

        obj.playerName = name[3]
        obj.teamid = player.team_id

        if player.result == "Win":
            obj.result = 2
        elif player.result == "Loss":
            obj.result = 1
        if player.play_race == "Protoss":
            obj.protoss = 1
        elif player.play_race == "Zerg":
            obj.zerg = 1
        elif player.play_race == "Terran":
            obj.terran = 1
        players.append(obj)
    return players

# 
# Fetches which indici the player with the name is in the players array
#
def getplayerNumber(name,players):

    for i in range(0,len(players) - 1):
        if name == players[i].playerName:
            return i

    return -1

#
# Initiates the data vector to be returned based on the player 
# data that we recieve we follow the template above( Line 10 )
#
def initiateDataVector(player, testOrTrain):

    vec = []
    k = 10
    # Creates a vector of 0s with a size of k
    for i in range(0,k):
        vec.append(0)

    # Sets the given fraction of the player to 1
    if player.protoss == 1:
        vec[1] = 1
    if player.zerg == 1:
        vec[2] = 1
    if player.terran == 1:
        vec[3] = 1

    # Sets the given result of the replay for the 
    # certain player to a  1 or a 0
    if testOrTrain == "train":
        if player.result == 1:
            vec[len(vec) - 1 ] = 1
    else:
        vec[len(vec) - 1] = player.teamid
   # print(player.playerName, " ", player.result)

    # Merges all the values of the vector
    return vec[:]


#
# Creates a comment and deata entry 
#
#
def getUnitBornEvent(players, tracker, testOrTrain):

    # Get timestamp in seconds for the array
    timestamp = str(tracker.second).split()[0]
    name = str(tracker).split()[4]

    if(name == "A.I."):
        bot = str(tracker).split()[11]
    else:
        bot = str(tracker).split()[9]

    # Create the vector for the data table
    vec = initiateDataVector(players[getplayerNumber(name,players)], testOrTrain)
    vec[0] = int(timestamp)
    vec[4] = 1

    comment = [int(timestamp), name, bot, "UnitBornEvent"]
    return vec, comment

#
# Creates a comment and deata entry
#
#
def getUnitDiedEvent(players, tracker, testOrTrain):

    # Get timestamp in seconds for the array
    timestamp = str(tracker.second).split()[0]
    name = str(tracker).split()[4]

    if(name == "A.I."):
        bot = str(tracker).split()[11]
    else:
        bot = str(tracker).split()[9]

    # Create the vector for the data table
    vec = initiateDataVector(players[getplayerNumber(name,players)], testOrTrain)
    vec[0] = int(timestamp)
    vec[5] = 1

    comment = [int(timestamp), name, bot, "UnitDiedEvent"]
    return vec, comment

#
# Creates a comment and deata entry
#
#
def getUnitTypeChangeEvent(players, tracker, testOrTrain):

    # Get timestamp in seconds for the array
    timestamp = str(tracker.second).split()[0]
    name = str(tracker).split()[4]
    bot = str(tracker).split()[16]

    if(name == "A.I."):
        bot = str(tracker).split()[20]
    else:
        bot = str(tracker).split()[16]

    # Create the vector for the data table
    vec = initiateDataVector(players[getplayerNumber(name,players)], testOrTrain)
    vec[0] = int(timestamp)
    vec[6] = 1

    comment = [int(timestamp), name, bot, "UnitTypeChangeEvent"]
    return vec, comment

#
# Creates a comment and deata entry
#
#
def getUpgradeCompleteEvent(players, tracker, testOrTrain):

    # Get timestamp in seconds for the array
    timestamp = str(tracker.second).split()[0]
    name = str(tracker).split()[4]

    if(name == "A.I."):
        bot = str(tracker).split()[9]
    else:
        bot = str(tracker).split()[7]

    # Create the vector for the data table
    vec = initiateDataVector(players[getplayerNumber(name,players)], testOrTrain)
    vec[0] = int(timestamp)
    vec[6] = 1

    comment = [int(timestamp), name, bot, "UpgradeCompleteEvent"]
    return vec, comment

def getUpdateTargetUnitCommandEvent(players, event, testOrTrain):

    # Get timestamp in seconds for the array
    timestamp = str(event.second).split()[0]
    name = str(event).split()[1]

    if(name == "A.I."):
        bot = str(event).split()[9]
    else:
        bot = str(event).split()[5]

    # Create the vector for the data table
    vec = initiateDataVector(players[getplayerNumber(name,players)], testOrTrain )
    vec[0] = int(timestamp)
    vec[7] = 1

    comment = [int(timestamp), name, bot, "UpdateTargetUnitCommandEvent"]
    return vec, comment



#
# This function recieves the trackerEvents subtrack 
# and calls respective functions to collect the values: 0s or 1s
#
def getTrackerEvents(data, comments, players, trackerEvents, testOrTrain):
    tempComments = ""
    tempData = ""
    # For each trackerEvent
    for tracker in trackerEvents:

        # Get type of the trackerEvent
        myEvent = str(type(tracker)).split('\'')[1].split('.')[3]

        # Get the timestamp of the trackerEvent
        timestamp = str(tracker).split()[0]

        # Ignores events that occur at timestamp 00:00
        if timestamp == "00.00":
            continue

        # Checks if the trackerEvent was a unitBornEvent
        elif (myEvent == "UnitBornEvent"):
            if len(str(tracker).split()) > 9:
                tempData, tempComments = getUnitBornEvent(players, tracker, testOrTrain)

        # Checks if the trackerEvent was a unitDiedEvent
        elif (myEvent == "UnitDiedEvent"):
            if len(str(tracker).split()) > 9:
                tempData, tempComments = getUnitDiedEvent(players, tracker, testOrTrain)

        # Checks if the trackerEvent was a unitTypeChangeEvent
        elif (myEvent == "UnitTypeChangeEvent"):
            if len(str(tracker).split()) > 9:
                tempData, tempComments = getUnitTypeChangeEvent(players, tracker, testOrTrain)

        # Checks if the trackerEvent was a unitTypeChangeEvent
        elif (myEvent == "UpgradeCompleteEvent"):
            if len(str(tracker).split()) > 9:
                tempData, tempComments = getUpgradeCompleteEvent(players, tracker, testOrTrain)

        comments.append(tempComments)
        data.append(tempData)

    return data[1:], comments[1:]


#
# function that print calls to get data to print
#
def getGameEvents(data, comments, players, Events, testOrTrain):
    # Get type of the trackerEvent
    for event in Events:
        myEvent = str(type(event)).split('\'')[1].split('.')[3]
        #print(myEvent)
        # Get the timestamp of the trackerEvent
        timestamp = str(event).split()[0]

        # Ignores events that occur at timestamp 00:00
        if timestamp == "00.00":
            continue

        elif myEvent == "UpdateTargetUnitCommandEvent":
            if len(str(event).split()) > 8:
                tempData, tempComments = getUpdateTargetUnitCommandEvent(players, event, testOrTrain)
                comments.append(tempComments)
                data.append(tempData)



    return data[1:], comments[1:]

def getPrintData(myReplay):

    sc2reader.engine.register_plugin(APMTracker())
    replay = sc2reader.load_replay(myReplay, load_level=4)
    data = [[]]
    unitStatusComments = [[]]

    players = initiatePlayers(replay)
    # printPlayers(players)

    data, unitStatusComments = getTrackerEvents(data, unitStatusComments,players, replay.tracker_events, "test")
    data, unitStatusComments = getGameEvents(data, unitStatusComments, players, replay.events, "test")
    # print(data)
    # print(unitStatusComments)

    return unitStatusComments[1:]

def getTrainHotVectorData(myReplay):

    sc2reader.engine.register_plugin(APMTracker())
    replay = sc2reader.load_replay(myReplay, load_level=4)
    data = [[]]
    unitStatusComments = [[]]

    players = initiatePlayers(replay)
    # printPlayers(players)

    data, unitStatusComments = getTrackerEvents(data, unitStatusComments,players, replay.tracker_events,"train")
    data, unitStatusComments = getGameEvents(data, unitStatusComments, players, replay.events,"train")
    #
    # for line in data:
    #     print(line)

    return data[1:]

def getTestHotVectorData(myReplay): # TODO: append team_id instead of Win/Loss

    sc2reader.engine.register_plugin(APMTracker())
    replay = sc2reader.load_replay(myReplay, load_level=4)
    data = [[]]
    unitStatusComments = [[]]

    players = initiatePlayers(replay)
    # printPlayers(players)

    data, unitStatusComments = getTrackerEvents(data, unitStatusComments,players, replay.tracker_events, "test")
    data, unitStatusComments = getGameEvents(data, unitStatusComments, players, replay.events, "test")



    return data[1:]


def getWinner(myReplay):

    sc2reader.engine.register_plugin(APMTracker())
    replay = sc2reader.load_replay(myReplay, load_level=4)

    #Traverse over all players
    for player in replay.people:

        name = str(player).split()
        playerName = name[3]

        # Get teamid  from the player's data
        teamid = player.team_id

        # If this particular player wins, return the teamid
        if player.result == "Win":
            return playerName

    # Returns -1 if none of the players won
    return -1

#Replay location
# myReplay = 'workingReplays/OneSideDominates.SC2Replay'
# a = getTrainHotVectorData(myReplay)
# #
# print(getWinner(myReplay))
# print (type(replay.game_events[0]) == sc2reader.events.game.CameraEvent)