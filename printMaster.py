import master
import sys
import printDir.animatePrint as animate
import printDir.printHelper as helper

# commentOnList = [[18, 'Trentos', 'Probe', 'UnitBornEvent'], [19, 'Onion', 'Probe', 'UnitBornEvent'], [35, 'Trentos', 'Probe', 'UnitBornEvent'], [36, 'Onion', 'Probe', 'UnitBornEvent']]
commentOnList = master.getPrintData()

def comment(simpleEvents):
    timeInSec = 1
    for event in commentOnList:
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

comment(commentOnList)