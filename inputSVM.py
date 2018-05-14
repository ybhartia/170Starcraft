import numpy as np
import svmImplementation as svmImplem
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

trainingX, trainingY = generateInput('replayCollection.txt')
print(len(trainingX), len(trainingY))
svmImplem.trainReplays(trainingX,trainingY)