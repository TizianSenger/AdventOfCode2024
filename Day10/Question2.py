print("Day10 Question2")

ArrTrail = []

def readDataFromFile():
    global ArrTrail
    file = open("AdventOfCode2024\Day10\source.txt", "r")
    content = file.read()
    content = content.split("\n")
    for line in content:
        lineArr = []
        for number in line:
            lineArr.append(int(number))
        ArrTrail.append(lineArr)    
    file.close()


readDataFromFile()
counterNines = 0
for element in ArrTrail:
    for number in element:
        if number == 0:
            counterNines = counterNines + 1
print(counterNines)