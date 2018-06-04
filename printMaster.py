import parsing.master as parser
import sys
import printDir.animatePrint as animate
import printDir.printHelper as helper
import SVM.svmHandler as svmHandler


DIR_NAME = "workingReplays"
DIR_SEPARATOR = '/'
TEST_REPLAY = "workingReplays/OneSideDominates.SC2Replay"
# commentOnList = [[18, 'Trentos', 'Probe', 'UnitBornEvent'], [19, 'Onion', 'Probe', 'UnitBornEvent'], [35, 'Trentos', 'Probe', 'UnitBornEvent'], [36, 'Onion', 'Probe', 'UnitBornEvent']]

#
#
#
def comment(simpleEvents):
    timeInSec = 1
    for event in commentOnList:
        if(event == ""):
            continue
        while (timeInSec < event[0]/ 1000):
            animate.moveOn(.5)
            timeInSec += .5
        commentLine = getLine(event)
        timeInSec += animate.commentate(commentLine, True, 'f')

def getLine(event):
    if event[3] == 'UnitBornEvent':
        return helper.getUnitBornLine(event[1],event[2])
    else:
        return event[1] + ' ' + event[2] + ' ' + event[3]



#
# going through the replay directory and train through replays
#
def trainSVM():

    # initialize the variables
    xTrainData =[[]]
    yTrainData = []

    # going through the directory
    for filename in listdir(DIR_NAME):

        # Setting right path to filename
        filname = DIR_NAME + DIR_SEPARATOR + filename

        # Not training with the test replay
        if(filename != TEST_REPLAY):
            hotVectorData = parser.getTrainData(filename)
            xTempTrainData, yTempTrainData = svmHandler.callTrainSVM(hotVectorData)
            xTrainData += [xTempTrainData]
            yTrainData += [yTrainData]

    svmHandler.callTrainReplays(xTrainData[1:], yTrainData)


#
#
#.MAIN FUNCTION THAT IS GOING TO DO EVERYTHING
#
#
def runProject():
    commentOnList = parser.getPrintData(TEST_REPLAY)
    hotVectorData = parser.getHotVectorData(TEST_REPLAY)
    yOut1,yOut2 = svmHandler.callTestSVM(hotVectorData)
    print("Player 1 : ",yOut1)
    print("Player 2 : ", yOut2)
    comment(commentOnList)

trainSVM()
runProject()

