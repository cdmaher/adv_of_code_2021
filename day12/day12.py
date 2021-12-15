import heapq
import sys
from collections import defaultdict
from functools import reduce

TOTAL_STEPS = 100


class Cave:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.visited = False

    def addConnection(self, cave):
        self.connections.append(cave)

    def getConnections(self):
        return self.connections

    def isGoal(self):
        return self.name == "end"

    def isSmall(self):
        return not self.name.isupper()

    def markVisited(self):
        self.visited = True

    def canVisit(self, curPath):
        if self.name == "start":
            return False
        if not self.isSmall():
            return True
        occurences = 0
        for cave in curPath:
            if cave.name == self.name:
                occurences += 1
        if occurences == 0:
            return True
        if hasSingleSmallVisits(curPath):
            return False
        return occurences == 1

    def __str__(self):
        return self.name

    __repr__ = __str__


def processCaves(file):
    caves = {}
    for line in file:
        (caveA, caveB) = line.rstrip().split("-")
        if caveA not in caves:
            caves[caveA] = Cave(caveA)
        if caveB not in caves:
            caves[caveB] = Cave(caveB)
        caves[caveA].addConnection(caves[caveB])
        caves[caveB].addConnection(caves[caveA])
    return caves


def findPaths(caves):
    caveStart = caves["start"]
    return findPathsImpl(caves, caveStart, [caveStart])


def findPathsImpl(caves, currentCave, curPath):
    currentCave.markVisited()
    paths = []
    for connection in currentCave.getConnections():
        if connection.isGoal():
            paths.append(curPath + [connection])
        elif connection.canVisit(curPath):
            paths = paths + findPathsImpl(caves, connection, curPath + [connection])
    return paths


def hasSingleSmallVisits(curPath):
    smalls = set()
    for cave in curPath:
        if cave.isSmall() and cave.name in smalls:
            return True
        else:
            smalls.add(cave.name)
    return False


def printPaths(paths):
    for path in paths:
        print(str(path))


def main(fileName):
    file = open(fileName, "r")

    caves = processCaves(file)

    paths = findPaths(caves)
    printPaths(paths)
    print("Total paths " + str(len(paths)))


if __name__ == "__main__":
    main(sys.argv[1])
