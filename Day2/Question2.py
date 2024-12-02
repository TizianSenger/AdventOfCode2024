print("Day2 Question2")

listOfListsData = []
minDif = 1
maxDif = 3

def readDataFromFile():
    global listOfListsData
    file = open(r"Day2/source.txt", "r")
    for line in file:
        listOfListsData.append(list(map(int, line.split())))
    file.close()

def distance(a, b):
    return abs(a - b)

def signum(n):
    return (n > 0) - (n < 0)

def is_safe(report, bad_level_tolerated, signum_value):
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]

        if signum(diff) != signum_value or distance(report[i - 1], report[i]) > maxDif:
            if bad_level_tolerated:
                return False

            # entfene element try
            return (
                is_safe(report[:i] + report[i + 1:], True, signum_value) or
                is_safe(report[:i - 1] + report[i:], True, signum_value)
            )
    return True

def makeCalculations():
    countOfValid = 0
    for report in listOfListsData:
        # test sicher entweder asc oder desc
        if is_safe(report, False, 1) or is_safe(report, False, -1):
            countOfValid += 1

    print(countOfValid)

readDataFromFile()
makeCalculations()
