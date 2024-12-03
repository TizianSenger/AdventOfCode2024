import re
print("Day1 Question1")

scrambledString = ""
multiplicants = []
regexPattern = r'mul\(\d+,\d+\)'

def readDataFromFile():
    global scrambledString
    file = open("AdventOfCode2024\Day03\source.txt", "r")
    content = file.read()
    scrambledString = content
    file.close()

def cleanExtractData():
    global multiplicants
    extractedMuls = re.findall(regexPattern, scrambledString)
    for element in extractedMuls:
        element = element.replace("mul(", "")
        element = element.replace(")", "")
        element = element.split(",")
        element[0] = int(element[0])
        element[1] = int(element[1])
        multiplicants.append(element)

def clacData():
    endValue = 0
    for element in multiplicants:
        endValue = endValue + element[0]*element[1]
    print(endValue)

readDataFromFile()
cleanExtractData()
clacData()
