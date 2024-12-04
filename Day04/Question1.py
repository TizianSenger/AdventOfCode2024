print("Day4 Question1")

fileContent = []
seaWord = "XMAS"
lenOfWord = len(seaWord)

def readDataFromFile():
    global fileContent
    with open("Day04/source.txt", "r") as file:
        fileContent[:] = [list(line.strip()) for line in file.readlines()]

def inBounds(x, y):
    return 0 <= x < len(fileContent) and 0 <= y < len(fileContent[0])

def searchWord(layerIndex, caracterIndex, dx, dy):
    for i in range(lenOfWord):
        nx, ny = layerIndex + i * dx, caracterIndex + i * dy
        if not inBounds(nx, ny) or fileContent[nx][ny] != seaWord[i]:
            return False
    return True

def organizeDataAndReplaceX():
    directions = [
        (0, 1),  # rechts
        (0, -1),  # links
        (-1, 0),  # oben
        (1, 0),  # unten
        (1, 1),  # diagonal rechts unten
        (-1, 1),  # diagonal rechts oben
        (1, -1),  # diagonal links unten
        (-1, -1)  # diagonal links oben
    ]
    counter = 0
    for layerIndex in range(len(fileContent)):
        for caracterIndex in range(len(fileContent[layerIndex])):
            for dx, dy in directions:
                if searchWord(layerIndex, caracterIndex, dx, dy):
                    counter += 1
                    #print("gefunden")
    print(counter)


readDataFromFile()
organizeDataAndReplaceX()
