import numpy as np
import svmImplementation as svmImplem
import inputSVM as input
import math


X, Y = input.generateInput('replayCollection.txt')
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




