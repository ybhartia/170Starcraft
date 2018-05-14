import numpy as np
import svmImplementation as svmImplem
import math

#
# A function that generates a 2D matrix which consists of all the parameters of the replays and the win or lost state
# We create a row for each vector with ~ all data points
#
# len(x[0]) = input layer size
# R = Number of Replays for training purposes
#
def generateInput(filepath):
# filepath = 'replayCollection.txt'
    x = [[]]
    y = []
    with open(filepath) as fp:
       line = fp.readline()
       cnt = 1

       while line:

           line = line.strip()
           vals = line.split(" ")

           for i in range(0,len(vals)):
            vals[i] = int(vals[i])

           x += [vals]
           y += [cnt%2]

           # READ THE NEXT LINE
           line = fp.readline()
           cnt += 1

    return x[1:], y

X, Y = generateInput('replayCollection.txt')
total = len(X)
trainLen = 0.75 * total
print total
print int(trainLen)
trainingX = X[0:int(trainLen)]
trainingY = Y[0:int(trainLen)]

testingX = X[int(trainLen):]
testingY = Y[int(trainLen):]

print(len(trainingX), len(trainingY))
print(len(testingX), len(testingY))


svmImplem.trainReplays(trainingX,trainingY)
bestModel, bestScore = svmImplem.pickBestModel(testingX,testingY)

newInput = [123, 123, 2341, 13241, 13451343, 12, 345, 123, 5, 12354]
print(svmImplem.checkForWin(newInput,bestModel))



