import numpy as np
def generateInput(filepath):
# filepath = 'replayCollection.txt'
    x = [[]]
    with open(filepath) as fp:
       line = fp.readline()
       cnt = 1

       while line:

           # print("Line {}: {}".format(cnt, line.strip()))
           line = line.strip()
           vals = line.split(" ")

           # if cnt == 1:
           #     x = np.array(len(vals))


           for i in range(0,len(vals)):
            vals[i] = int(vals[i])

           # if cnt == 1:
           #     x = np.array(vals)
           # else:
           x += [vals]
           # READ THE NEXT LINE
           line = fp.readline()
           cnt += 1

    return x[1:]

input = generateInput('replayCollection.txt')
