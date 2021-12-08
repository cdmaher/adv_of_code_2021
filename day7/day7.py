import sys
from collections import defaultdict


def processPositions(file):
    positions = file.readline().rstrip().split(",")
    return list(map(int, positions))


def findOptimalFuel(positions, maxV):
    optimalFuel = -1
    for i in range(maxV):
        currentFuel = 0
        for pos in positions:
            n = abs(i - pos)
            currentFuel += int((n * n + n) / 2)
        if currentFuel < optimalFuel or optimalFuel == -1:
            optimalFuel = currentFuel
    return optimalFuel


def getMaxVal(positions):
    maxV = 0
    for pos in positions:
        if pos > maxV:
            maxV = pos
    return maxV


def main(fileName):
    file = open(fileName, "r")
    positions = processPositions(file)
    fuel = findOptimalFuel(positions, getMaxVal(positions))
    print("Optimal fuel ", fuel)


if __name__ == "__main__":
    main(sys.argv[1])
