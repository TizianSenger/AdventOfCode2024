print("Day11 Question1")

inputArr = []
blinks = 25

def readDataFromFile():
    global inputArr
    file = open("AdventOfCode2024\Day11\source.txt", "r")
    content = file.read()
    inputArr = content.split(" ")
    # print(content)
    file.close()
    
def rearangeAndRecalcStones(counter):
    global inputArr
    tempArr = []
    print("Stones getting rearanged " + str(counter))
    for element in inputArr:
        if element == "0":
            element = "1"
            tempArr.append(element)
        elif len(element) % 2 == 0:
            middle = len(element)/2
            leftHalf = element[:int(middle)]
            rightHalf = element[int(middle):]
            # print(leftHalf + "|" + rightHalf)
            element[0:int(middle)]
            tempArr.append(str(int(leftHalf)))
            tempArr.append(str(int(rightHalf)))
        else:
            tempArr.append(str(int(element) * 2024))
    inputArr = tempArr
    # print(inputArr)
    

def calculateForBilnks():
    print("calculating stones for " +  str(blinks) + " blinks")
    counter = 0
    while counter < blinks:
        counter = counter + 1     
        rearangeAndRecalcStones(counter)
    print(str(len(inputArr)) + " Stones")
    
readDataFromFile()
calculateForBilnks()

