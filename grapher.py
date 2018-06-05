import parsing.parser as parser
import sys
import printDir.animatePrint as animate
import printDir.printHelper as helper
import SVM.svmHandler as svmHandler
from os import listdir
import os
import random
import sc2reader
from sc2reader.engine.plugins import APMTracker


DIR_SEPARATOR = '/'
# commentOnList = [[18, 'Trentos', 'Probe', 'UnitBornEvent'], [19, 'Onion', 'Probe', 'UnitBornEvent'], [35, 'Trentos', 'Probe', 'UnitBornEvent'], [36, 'Onion', 'Probe', 'UnitBornEvent']]


#
# Comment given events and player predictions
#
def comment(commentOnList, p1Predictions, p2Predictions):
    timeInSec = animate.commentate(helper.getIntro(), True, 'm')
    for event in commentOnList:
        if(event == ""):
            continue
        while (timeInSec < event[0]):
            animate.moveOn(.5)
            timeInSec += .5
        commentLine = getLine(event)

        timeInSec += animate.commentate(commentLine, True, 'm')

def getLine(event):
    player = event[1]
    unit = event[2]
    if event[3] == 'UnitBornEvent':
        return helper.getUnitBornLine(player,unit)
    elif event[3] == 'UnitDiedEvent':
        return helper.getUnitDieLine(player,unit)
    elif event[3] == 'UnitTypeChangeEvent':
        faction = parser.getPlayer(player, TEST_REPLAY).play_race
        return helper.getTypeChangeLine(player,unit,faction)
    elif event[3] == 'UpgradeCompleteEvent':
        return helper.getUpgradeCompleteLine(player,unit, "")
    else:
        return player + ' ' + unit + ' ' + event[3]



# #
# # going through the replay directory and train through replays
# #
# def trainSVM():

#     # initialize the variables
#     xTrainData =[[]]
#     yTrainData = []

#     # going through the directory
#     for filename in listdir(DIR_NAME):


#         # Setting right path to filename
#         filename = DIR_NAME + DIR_SEPARATOR + filename

#         # Not training with the test replay
#         if(filename != TEST_REPLAY) and filename[len(DIR_NAME) + len(DIR_SEPARATOR)] != '.':

#             hotVectorData = parser.getTrainHotVectorData(filename)
#             print filename
#             xTempTrainData, yTempTrainData = svmHandler.callTrainSVM(hotVectorData)

#             for temp in xTempTrainData:
#                 xTrainData.append(temp)
#             yTrainData += yTempTrainData


#     svmHandler.callTrainReplays(xTrainData[1:], yTrainData)


#
# going through the replay directory and train through replays
#
def trainSVM(directoryName):

    # initialize the variables
    xTrainData =[[]]
    yTrainData = []

    testFile = listdir(directoryName)[random.randint(1,len(listdir(directoryName))-1 ) ]


    # going through the directory
    for filename in listdir(directoryName):


        # Setting right path to filename
        filename = directoryName + DIR_SEPARATOR + filename

        # Not training with the test replay
        if(filename != testFile) and filename[len(directoryName) + len(DIR_SEPARATOR)] != '.':

            hotVectorData = parser.getTrainHotVectorData(filename)
            print filename
            xTempTrainData, yTempTrainData = svmHandler.callTrainSVM(hotVectorData)

            for temp in xTempTrainData:
                xTrainData.append(temp)
            yTrainData += yTempTrainData


    svmHandler.callTrainReplays(xTrainData[1:], yTrainData)
    return testFile

def TestSVM(filename):
    commentOnList = parser.getPrintData(filename)
    hotVectorData = parser.getTestHotVectorData(filename)
    
    yOut1,yOut2 = svmHandler.callTestSVM(hotVectorData)
    
    sc2reader.engine.register_plugin(APMTracker())
    replay = sc2reader.load_replay(filename, load_level=4)

    players = parser.initiatePlayers(replay)

    team1 = []
    team2 = []

    for player in players:
        if player.teamid == 1:
            team1.append([player.playerName])
        else:
            team2.append([player.playerName])

    print("Player 1 : ",yOut1, yOut1[len(yOut1)-1])
    print("Player 2 : ", yOut2, yOut2[len(yOut2)-1])
    print("According to reality " + parser.getWinner(filename)+ " actually won the game")
    if yOut1[len(yOut1)-1] > yOut2[len(yOut2)-1]:
        print(team1)
    else:
        print(team2)

DIR_NAME = "workingReplays"
# TEST_REPLAY = "workingReplays/OneSideDominates.SC2Replay"
# TEST_REPLAY_TWO = "workingReplays/ggtracker_93731.SC2Replay"

directoryName = "workingReplays"


testFile = trainSVM(directoryName)
TestSVM(DIR_NAME + DIR_SEPARATOR + testFile)
# print(testFile)
# runProject()

