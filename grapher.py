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
            xTempTrainData, yTempTrainData = svmHandler.callTrainSVM(hotVectorData)

            for temp in xTempTrainData:
                xTrainData.append(temp)
            yTrainData += yTempTrainData


    svmHandler.callTrainReplays(xTrainData[1:], yTrainData)
    return testFile

def TestSVMLinear(filename):
    commentOnList = parser.getPrintData(filename)
    hotVectorData = parser.getTestHotVectorData(filename)
    
    yOut1,yOut2 = svmHandler.callTestSVMLinear(hotVectorData)
    
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

    # print("Player 1 : ",yOut1, yOut1[len(yOut1)-1])
    # print("Player 2 : ", yOut2, yOut2[len(yOut2)-1])
    # print("According to reality " + parser.getWinner(filename)+ " actually won the game")
    if yOut1[len(yOut1)-1] > yOut2[len(yOut2)-1]:
        # print(team1)
        winner = 1
    else:
        # print(team2)
        winner = 2

    if winner == 1:
        if [parser.getWinner(filename)] in team1:
            return 1
    elif winner == 2:
        if [parser.getWinner(filename)] in team2:
            return 1
    else:
        return 0

def TestSVMPoly(filename):
    commentOnList = parser.getPrintData(filename)
    hotVectorData = parser.getTestHotVectorData(filename)
    
    yOut1,yOut2 = svmHandler.callTestSVMPoly(hotVectorData)
    
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

    if yOut1[len(yOut1)-1] > yOut2[len(yOut2)-1]:
        winner = 1
    else:
        winner = 2

    if winner == 1:
        if [parser.getWinner(filename)] in team1:
            return 1
    elif winner == 2:
        if [parser.getWinner(filename)] in team2:
            return 1
    else:
        return 0

def TestSVMSigmoid(filename):
    commentOnList = parser.getPrintData(filename)
    hotVectorData = parser.getTestHotVectorData(filename)
    
    yOut1,yOut2 = svmHandler.callTestSVMSigmoid(hotVectorData)
    
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

    # print("Player 1 : ",yOut1, yOut1[len(yOut1)-1])
    # print("Player 2 : ", yOut2, yOut2[len(yOut2)-1])
    # print("According to reality " + parser.getWinner(filename)+ " actually won the game")
    if yOut1[len(yOut1)-1] > yOut2[len(yOut2)-1]:
        # print(team1)
        winner = 1
    else:
        # print(team2)
        winner = 2

    if winner == 1:
        if [parser.getWinner(filename)] in team1:
            return 1
    elif winner == 2:
        if [parser.getWinner(filename)] in team2:
            return 1
    else:
        return 0

#
# going through the replay directory and train through replays
#
def trainGiven(trainFilenames, directoryName):

    # initialize the variables
    xTrainData =[[]]
    yTrainData = []

    # going through the directory
    for fileName in trainFilenames:

        # Setting right path to filename
        filename = directoryName + DIR_SEPARATOR + fileName

        # Not training with the test replay
        if fileName[0] != '.':

            hotVectorData = parser.getTrainHotVectorData(filename)
            xTempTrainData, yTempTrainData = svmHandler.callTrainSVM(hotVectorData)

            for temp in xTempTrainData:
                xTrainData.append(temp)

            yTrainData += yTempTrainData


    svmHandler.callTrainReplays(xTrainData[1:], yTrainData)


def TESTall(testingFiles, directoryName):

    successLinear = 0.0
    successSigmoid = 0.0
    successPoly = 0.0

    accuracyLinear = 0.0
    accuracySigmoid = 0.0
    accuracyPoly = 0.0


    for testFile in testingFiles:
        if(testFile[0] != '.'):
            resultLinear = TestSVMLinear(directoryName + DIR_SEPARATOR + testFile)
            resultSigmoid = TestSVMSigmoid(directoryName + DIR_SEPARATOR + testFile)
            resultPoly = TestSVMPoly(directoryName + DIR_SEPARATOR + testFile)
                    
            if resultLinear == 1:
                successLinear = successLinear + 1 
            if resultPoly == 1:
                successPoly = successPoly + 1 
            if resultSigmoid == 1:
                successSigmoid = successSigmoid + 1 


    accuracyLinear = successLinear / len(testingFiles)
    accuracySigmoid = successSigmoid / len(testingFiles)
    accuracyPoly = successPoly / len(testingFiles)
    
    print "Linear",accuracyLinear
    print "Poly",accuracyPoly           
    print "Sigmoid",accuracyLinear

directoryName = "workingReplays"
numReplays = len(listdir(directoryName))


# TRAINING 
# print(" HEY LETS TRAIN LIKE CUNTS")
# testFile = trainSVM(directoryName)


#################TEST ALL FILES AND EVALUATE
# Replays = listdir(directoryName)
# Replays = sorted(Replays)

# for i in range(56,len(Replays)):
#     print i, Replays[i]
#     if Replays[i][0] != '.':
#         TestSVMLinear(directoryName + DIR_SEPARATOR + Replays[i])


########## TESTING TO GENERATE ACCURACY with different training
Replays = listdir(directoryName)
Replays = sorted(Replays)


for trainCounter in [5,10,15,20,25,30,35,40,45,50,55,60,65,70]:

    trainReplays = Replays[25:25+trainCounter]
    testReplays = Replays[:10]
    print trainCounter
    trainGiven(trainReplays, directoryName)
    # print testReplays
    TESTall(testReplays, directoryName)

