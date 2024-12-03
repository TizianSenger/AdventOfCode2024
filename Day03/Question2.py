import re
print("Day1 Question1")

scrambledString = ""
multiplicants = []
regexPattern = r'mul\(\d+,\d+\)'

print("regex is complete shit just dont use it i hate my life")

def readDataFromFile():
    global scrambledString
    file = open("AdventOfCode2024\Day03\source.txt", "r")
    content = file.read()
    scrambledString = content
    file.close()

def cleanExtractData():
    global multiplicants
    extractedMuls = re.findall(regexPattern, scrambledString)
    enabled = True
    for element in extractedMuls:
        if "do()" in element:
            enabled = True
            element = element.replace("do()", "")
        elif "dont()" in element:
            enabled = False
        if enabled == True:
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
