print("Day10 Question1")

arrTrail = []
zeorsLocation = []
ninesLocation = []
zerosWithScore = []

numbersLocationDict = {}
routeWithStartingpoint = {}

def readDataFromFile():
    global arrTrail
    file = open("AdventOfCode2024\Day10\source.txt", "r")
    content = file.read()
    content = content.split("\n")
    for line in content:
        lineArr = []
        for number in line:
            lineArr.append(int(number))
        arrTrail.append(lineArr)    
    file.close()


def locateAllZeros():
    global zeorsLocation
    global numbersLocationDict
    for number in range(10):
        numbersLocationDict[number] = []     
    for rowNumber in range(len(arrTrail)):
        for columnNumber in range(len(arrTrail[rowNumber])):
            temp = numbersLocationDict[arrTrail[rowNumber][columnNumber]]
            temp.append([rowNumber,columnNumber])       
    dictKeys = numbersLocationDict.keys()
    for number in dictKeys:
        print(str(number) + " located in: " + str(numbersLocationDict[number]))
    
def checkForOnlyUpOrDown(currentY, currentX, nextCords):
    if nextCords[0] == currentX or nextCords[1] == currentY:
        return True
    else:
        return False
    
def countScoreForEachZero():
    zeorsLocation = numbersLocationDict[0]
    for startingPoint in zeorsLocation:
        print ("Startingpoint calc start: " + str(startingPoint))
        temporaryLocationDict = numbersLocationDict
        # remove zero cause not needed for further calcultations
        temporaryLocationDict.pop(0, any)
        print(temporaryLocationDict)


readDataFromFile()
locateAllZeros()
countScoreForEachZero()