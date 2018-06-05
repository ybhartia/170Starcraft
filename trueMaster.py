import parsing.parser as parser
import sys
import printDir.animatePrint as animate
import printDir.printHelper as helper
import SVM.svmHandler as svmHandler
from os import listdir
import os
import random

DIR_SEPARATOR = '/'
DIR_TEST = "HungsReplayTvZ.SC2Replay"
# commentOnList = [[18, 'Trentos', 'Probe', 'UnitBornEvent'], [19, 'Onion', 'Probe', 'UnitBornEvent'], [35, 'Trentos', 'Probe', 'UnitBornEvent'], [36, 'Onion', 'Probe', 'UnitBornEvent']]


#
# Comment given events and player predictions
#
def comment(commentOnList, p1Predictions, p2Predictions, replay):

    timeInSec = animate.commentate(helper.getIntro(), True, 'm')
    timeInSec += animate.commentate(helper.getTeamIntro(parser.getAllPlayers(replay)), True, 'm')
    for event in commentOnList:
        if(event == ""):
            continue
        while (timeInSec < (event[0]/1.4)):
            animate.moveOn(.5)
            timeInSec += .5
        commentLine = getLine(event, replay)

        timeInSec += animate.commentate(commentLine, True, 'm')

def getLine(event, replay):
    player = event[1]
    unit = event[2]
    if event[3] == 'UnitBornEvent':
        return helper.getUnitBornLine(player,unit)
    elif event[3] == 'UnitDiedEvent':
        return helper.getUnitDieLine(player,unit)
    elif event[3] == 'UnitTypeChangeEvent':
        faction = parser.getPlayer(player, replay).play_race
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
    testFile = DIR_TEST


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
    # comment(commentOnList, yOut1, yOut2, testFile)


DIR_NAME = "workingReplays"
# TEST_REPLAY = "workingReplays/OneSideDominates.SC2Replay"
# TEST_REPLAY_TWO = "workingReplays/ggtracker_93731.SC2Replay"

directoryName = "workingReplays"


testFile = trainSVM(directoryName)
runProject(DIR_NAME + DIR_SEPARATOR + testFile)
# TestSVM(DIR_NAME + DIR_SEPARATOR + testFile)
# print(testFile)
# runProject()

