import animatePrint as animate
import printHelper as helper
import os

def printHistory(history):
    for pastComment in history:
        print (pastComment)
    # print(history)

def Comment(history, comment):
    os.system('clear')
    printHistory(history)
    length = len(comment)

    blank = ""
    seperator = ""
    for i in range(0,length + 10):
        seperator += "*"
        blank += " "

    print(seperator)
    print(blank)
    print("          ")
    animate.commentate(comment,True,'s')
    print(blank)
    print(seperator)

    history.append(comment)

    return history



history = []
# a = helper.introLine()
a = []
a += ["comment 1"]
a += ["comment 2"]
a += ["comment 3"]
a += ["comment 4"]
a += ["comment 5"]
a += ["comment 6"]
a += ["comment 7"]
a += ["comment 8"]

for i in a:
    history = Comment(history, i)