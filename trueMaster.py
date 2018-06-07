import parsing.parser as parser
import sys
import printDir.animatePrint as animate
import printDir.printHelper as helper
import SVM.svmHandler as svmHandler
from os import listdir
import os
import random
import math
import sys

DIR_SEPARATOR = '/'
DIR_TEST = "HungsReplayTvZ.SC2Replay"
# commentOnList = [[18, 'Trentos', 'Probe', 'UnitBornEvent'], [19, 'Onion', 'Probe', 'UnitBornEvent'], [35, 'Trentos', 'Probe', 'UnitBornEvent'], [36, 'Onion', 'Probe', 'UnitBornEvent']]


#
# Comment given events and player predictions
#
def comment(commentOnList, p1Predictions, p2Predictions, replay):
    AICommentCount = 1
    timeInSec = animate.commentate(helper.getIntro(), True, 'm', "basic")
    timeInSec += animate.commentate(helper.getTeamIntro(parser.getAllPlayers(replay)), True, 'm', "basic")
    for event in commentOnList:
        if(event == ""):
            continue
        while (timeInSec < (event[0]/1.4)):
            animate.moveOn(.5)
            timeInSec += .5
            timeInSec += animate.updateTime(getTime(timeInSec*1.4))
        commentLine = getLine(event, replay)
        if (timeInSec > 60*AICommentCount):
            if AICommentCount - 1 < len(p1Predictions):
                outcome = p1Predictions[AICommentCount - 1] - p2Predictions[AICommentCount - 1]
                timeInSec += animate.commentate(getTime(event[0]) + "  " + helper.getAIPrint(outcome, parser.getAllPlayers(replay)) + 
                    getScores(p1Predictions[AICommentCount - 1], p2Predictions[AICommentCount - 1]), True, 'm', "ai")
                AICommentCount += 1
        timeInSec += animate.updateTime(getTime(timeInSec*1.4))
        timeInSec += animate.commentate(getTime(event[0]) + "  " + commentLine, True, 'm', "basic")
    animate.commentate(helper.getClosing(), True, 'm', "closing")

def getScores(p1Score, p2Score):
    return " [Team 1: " + str(p1Score) + " Team 2: " + str(p2Score) + " ]"

#
# Get time in the bet order
#
def getTime(time):
    time = time/1.4
    minutes = int(math.floor(time/60))
    seconds = int(math.floor(time)%60)

    if(minutes < 10):
        minutes =  "0" + str(minutes)

    if(seconds < 10):
        seconds =  "0" + str(seconds)

    return str(minutes) + ":" + str(seconds)


def getLine(event, replay):
    player = event[1]
    unit = event[2]
    if event[3] == 'UnitBornEvent':
        return helper.getUnitBornLine(player,unit, event)
    elif event[3] == 'UnitDiedEvent':
        return helper.getUnitDieLine(player,unit, event)
    elif event[3] == 'UnitTypeChangeEvent':
        faction = parser.getPlayer(player, replay).play_race
        return helper.getTypeChangeLine(player,unit,faction, event)
    elif event[3] == 'UpgradeCompleteEvent':
        return helper.getUpgradeCompleteLine(player,unit, "", event)
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
    testFile = DIR_TEST


    # going through the directory
    for filename in listdir(directoryName):


        # Setting right path to filename
        filename = directoryName + DIR_SEPARATOR + filename

        # Not training with the test replay
        if(filename != testFile) and filename[len(directoryName) + len(DIR_SEPARATOR)] != '.':

            print filename
            hotVectorData = parser.getTrainHotVectorData(filename)
            xTempTrainData, yTempTrainData = svmHandler.callTrainSVM(hotVectorData)

            for temp in xTempTrainData:
                xTrainData.append(temp)
            yTrainData += yTempTrainData


    svmHandler.callTrainReplays(xTrainData[1:], yTrainData)
    return testFile


#
#
#.MAIN FUNCTION THAT IS GOING TO DO EVERYTHING
#
#
def runProject(testFile):

    #
    commentOnList = parser.getPrintData(testFile)
    hotVectorData = parser.getTestHotVectorData(testFile)

    yOut1,yOut2 = svmHandler.callTestSVM(hotVectorData)
    print("Player 1 : ",yOut1)
    print("Player 2 : ", yOut2)
    print("and player", parser.getWinner(testFile), "actually won the game")

    commentOnList = parser.mergeComments(commentOnList)
    comment(commentOnList, yOut1, yOut2, testFile)




DIR_NAME = "workingReplays"
# TEST_REPLAY = "workingReplays/OneSideDominates.SC2Replay"
# TEST_REPLAY_TWO = "workingReplays/ggtracker_93731.SC2Replay"

directoryName = "workingReplays"


# testFile = trainSVM(directoryName)
testFile = "TerranDoAll.SC2Replay"

## runProject(DIR_NAME + DIR_SEPARATOR + testFile)

# TestSVM(DIR_NAME + DIR_SEPARATOR + testFile)
# print(testFile)
# runProject()


try:
    if(len(sys.argv) > 1):
        runProject(sys.argv[1])
    else:
        print "A replay file needs to be provided."
except:
    print "File needs to be a replay file (.SC2Replay)."