import animatePrint as animate
import printHelper as helper

commentOnList = [[18, 'Trentos', 'Probe', 'UnitBornEvent'], [19, 'Onion', 'Probe', 'UnitBornEvent'], [35, 'Trentos', 'Probe', 'UnitBornEvent'], [36, 'Onion', 'Probe', 'UnitBornEvent']]

def comment(simpleEvents):
    timeInSec = 1
    for event in commentOnList:
        if timeInSec > event[0] / 1000:
            commentLine = getLine(event)
            timeInSec += animate.commentate(commentLine, True, 'f')
        else:
            animate.moveOn(.5)

def getLine(event):
    if event[3] == 'UnitBornEvent':
        return helper.getUnitBornLine(event[1],event[2])
    else:
        return event[1] + ' ' + event[2] + ' ' + event[3]

comment(commentOnList)