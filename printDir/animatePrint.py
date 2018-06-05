import time,sys
import os


history = [] ## Our global event array
STAR_LENGTH = 30

# Print the history 
def printHistory():
    for pastComment in history:
        print (pastComment)

    # printing the required data
    blank = ""
    seperator = ""
    for i in range(0,STAR_LENGTH):
        seperator += "*"
        blank += " "

    print(seperator)
    print(blank)
    print("          ")


# inputString  -> STRING that needs to be animated
# newLine -> BOOL specifies if new line is required at the end of the string
# speed -> specify fast, medium or slow animation

def commentate(inputString, newLine, speed):

    os.system('clear')
    printHistory()

    # making sure all inputs are valid
    start = time.time()


    #newLine needs to be a bool
    if type(newLine) != bool:
        raise Exception("Argument 2 bool expected")

    #speed needs to be a string
    if type(speed) != str:
        raise Exception("Argument 3 string expected")


    # add a newline if the user chooses newLine flag to be True
    if newLine == True:
        inputString += '\n'

    # convert the speed string to lowercase
    speed = speed.lower()

    # with fast animation, each new character is printed every 4 milliseconds
    if speed == "fast" or speed == "f":
        frequency = 0.01

    # with medium animation, each new character is printed every 8 milliseconds
    elif speed == "medium" or speed == "m":
        frequency = 0.035

    # with slow animation, each new character is printed every 12 milliseconds
    elif speed == "slow" or speed == "s":
        frequency  = 0.12

    # animate loop
    for character in inputString:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(frequency)
    end = time.time()

    history.append(inputString)
    return (end - start)


def moveOn(sleeptime):
    time.sleep(sleeptime)

def main():
    timeElapsed = commentate("Hey what man this shit is unreal", True, "f")
    print(timeElapsed)


#
# main()