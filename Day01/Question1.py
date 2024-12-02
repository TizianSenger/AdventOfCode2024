print("Day1 Question1")

inputData = []
leftList = []
rightList= []
listOfDifs = []

def readDataFromFile():
    global inputData
    file = open("Day01\source.txt", "r")
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
    global listOfDifs
    counter = 0
    while counter < len(leftList):
        numberLeft = int(leftList[counter])
        numberRight = int(rightList[counter])
        if numberLeft >= numberRight:
            listOfDifs.append(numberLeft-numberRight)
        else:
            listOfDifs.append(numberRight-numberLeft)
        counter = counter + 1
    sumOFDifs = 0
    for element in listOfDifs:
        sumOFDifs = sumOFDifs + element
    print(sumOFDifs)

readDataFromFile()
prepareData()
makeCalculations()

