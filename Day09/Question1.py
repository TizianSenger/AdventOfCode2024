print("Day1 Question1")

def readDataFromFile():
    file = open("AdventOfCode2024\Day1\source.txt", "r")
    content = file.read()
    print(content)
    file.close()

readDataFromFile()