import numpy as np
import svmImplementation as svmImplem
import math

#
# A function that generates a 2D matrix which consists of all the parameters of the replays and the win or lost state
# We create a row for each vector with ~ all data points
#
# len(x[0]) = input layer size
# len(y) = total number of observations
#
def generateInput(filepath):
    x = [[]]
    y = []

    #
    # File with all data
    #
    with open(filepath) as fp:
       line = fp.readline()
       cnt = 1

       #
       # Per Line
       #
       while line:

           #
           # Vals
           #
           line = line.strip()
           vals = line.split(" ")

           for i in range(0,len(vals)):
            vals[i] = int(vals[i])

           x += [vals]
           y += [cnt%2]

           # READ THE NEXT LINE
           line = fp.readline()
           cnt += 1


    #
    # Completed dataset and output list
    #
    return x[1:], y
