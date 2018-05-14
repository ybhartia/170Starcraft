import numpy as np
import svmImplementation as svmImplem
import inputSVM as input
import math


#
# Collects data from inputSVM
#
X, Y = input.generateInput('replayCollection.txt')

#
# Calculates the values used to split the data into training and testing
#
total = len(X)
trainLen = 0.75 * total

#
# Split the data into training and testing based on values above
#
trainingX = X[0:int(trainLen)]
trainingY = Y[0:int(trainLen)]
testingX = X[int(trainLen):]
testingY = Y[int(trainLen):]

#
# Trains all our models
#
svmImplem.trainReplays(trainingX,trainingY)

#
# picks the best model and gets the score for that model
#
bestModel, bestScore = svmImplem.pickBestModel(testingX,testingY)

#
# Creates a test case to check if the test case wins
#
newInput = [123, 123, 2341, 13241, 13451343, 12, 345, 123, 5, 12354]

#
# Checks if the test case wins
#
print(svmImplem.checkForWin(newInput,bestModel))




