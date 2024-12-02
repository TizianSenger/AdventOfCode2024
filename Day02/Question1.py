print("Day2 Question1")

listOfListsData = []
filteredAscDesc = []
minDif = 1
maxDif = 3

def readDataFromFile():
    global listOfListsData
    file = open(r"Day02/source.txt", "r")
    content = file.read().splitlines()
    for element in content:
        tempArr = list(map(int, element.split()))
        listOfListsData.append(tempArr)

def distance(a, b):
    return abs(a - b)

def checkForOrder():
    global filteredAscDesc
    for entry in listOfListsData:
        if all(entry[i] <= entry[i + 1] for i in range(len(entry) - 1)) or all(entry[i] >= entry[i + 1] for i in range(len(entry) - 1)):
            filteredAscDesc.append(entry)

def makeCalculations():
    countOfValid = 0
    for entry in filteredAscDesc:
        valid = True
        for i in range(len(entry) - 1):
            if not (minDif <= distance(entry[i], entry[i + 1]) <= maxDif):
                valid = False
                break
        if valid:
            countOfValid = countOfValid + 1
    print(countOfValid)

readDataFromFile()
checkForOrder()
makeCalculations()
