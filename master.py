from __future__ import print_function
import sc2reader
from sc2reader.engine.plugins import APMTracker

# format of the vector

# [time, isProtoss, isZerg, isTerran, didBuildUnit, , , , , result]

myReplay = '/Users/sakshambhalla/Downloads/ggtracker_93731.SC2Replay'

class Player:
    def __init__(self):
        self.teamid = ""
        self.playerName = ""
        self.protoss = 0
        self.zerg = 0
        self.terran = 0
        self.result = -1

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


def initiatePlayers(replay):
    players = []
    for player in replay.clients:
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

def getplayerNumber(name,players):

    for i in range(0,len(players) - 1):
        if name == players[i].playerName:
            return i

    return -1

def initiateDataVector(player):

    vec = []
    k = 6
    for i in range(0,k):
        vec.append(0)

    if player.protoss == 1:
        vec[1] = 1
    if player.zerg == 1:
        vec[2] = 1
    if player.terran == 1:
        vec[3] = 1

    if player.result == 1:
        vec[len(vec) - 1 ] = 1

    return vec[:]

def getTrackerEvents(data, comments, players, trackerEvents):

    for tracker in trackerEvents:
        myEvent = str(type(tracker)).split('\'')[1].split('.')[3]
        timestamp = str(tracker).split()[0]


        if str(timestamp) == "00.00":
            continue

        elif (myEvent == "UnitBornEvent"):
            if len(str(tracker).split()) > 9:

                timestamp = str(tracker.second).split()[0]
                name = str(tracker).split()[4]
                bot = str(tracker).split()[9]

                vec = initiateDataVector(players[getplayerNumber(name,players)])
                vec[0] = int(timestamp)
                vec[4] = 1

                comment = timestamp+ " " + name + " built a " + bot
                comments.append([comment])
                data.append(vec)

    return data, comments

sc2reader.engine.register_plugin(APMTracker())
replay = sc2reader.load_replay(myReplay, load_level=4)
data = [[]]
unitStatusComments = [[]]

players = initiatePlayers(replay)
# printPlayers(players)

data, unitStatusComments = getTrackerEvents(data, unitStatusComments,players, replay.tracker_events)

print(data)


# print (type(replay.game_events[0]) == sc2reader.events.game.CameraEvent)