print("Day1 Question2")

inputData = []
leftList = []
rightList= []

def readDataFromFile():
    global inputData
    file = open("Day1\source.txt", "r")
    content = file.read()
    content = content.split("\n")
    for element in content:
        splitElement = element.split(" ")
        while "" in splitElement:
            splitElement.remove("")
        inputData.append(splitElement)
    file.close()

def prepareData():
    global leftList
    global rightList
    for element in inputData:
        leftList.append(element[0])
        rightList.append(element[1])
    leftList.sort()
    rightList.sort()

def makeCalculations():
    sumOfSimCount = 0
    counter = 0
    while counter < len(leftList):
        simCount = 0
        for element in rightList:
            if leftList[counter] == element:
                simCount = simCount + 1
        sumOfSimCount = sumOfSimCount + int(leftList[counter]) * simCount
        counter = counter + 1
    print(sumOfSimCount)

readDataFromFile()
prepareData()
makeCalculations()

