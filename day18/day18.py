import copy
import heapq
import math
import sys
from collections import defaultdict
from functools import reduce


class Pair:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.parent = None

    def setParent(self, parent):
        self.parent = parent

    def getLeftMag(self):
        if isinstance(self.left, int):
            return 3 * self.left
        else:
            return 3 * self.left.getMagnitude()

    def getRightMag(self):
        if isinstance(self.right, int):
            return 2 * self.right
        else:
            return 2 * self.right.getMagnitude()

    def getMagnitude(self):
        return self.getLeftMag() + self.getRightMag()

    def __str__(self):
        return "[" + str(self.left) + "," + str(self.right) + "]"

    __repr__ = __str__


def processPairList(file):
    pairList = []
    for line in file:
        pairList.append(processPair(line.rstrip())[0])
    return pairList


def processPair(line):
    if line[0] == "[":
        (left, length) = processPair(line[1:])
        (right, rLength) = processPair(line[length + 2 :])
        toReturn = Pair(left, right)
        if not isinstance(left, int):
            left.setParent(toReturn)
        if not isinstance(right, int):
            right.setParent(toReturn)
        return (toReturn, length + rLength + 3)
    else:
        regNum = int(line[0])
        return (regNum, 1)


def explodePair(pair):
    prevPair = pair
    curPair = pair.parent
    while curPair is not None and curPair.left == prevPair:
        prevPair = curPair
        curPair = curPair.parent
    if curPair is None:
        pass
    elif isinstance(curPair.left, int):
        curPair.left += pair.left
    else:
        nextLeft = curPair.left
        while not isinstance(nextLeft.right, int):
            nextLeft = nextLeft.right
        nextLeft.right += pair.left

    prevPair = pair
    curPair = pair.parent
    while curPair is not None and curPair.right == prevPair:
        prevPair = curPair
        curPair = curPair.parent
    if curPair is None:
        pass
    elif isinstance(curPair.right, int):
        curPair.right += pair.right
    else:
        nextRight = curPair.right
        while not isinstance(nextRight.left, int):
            nextRight = nextRight.left
        nextRight.left += pair.right

    if pair.parent.left == pair:
        pair.parent.left = 0
    else:
        pair.parent.right = 0


def explodeIfNecessary(pair, depth):
    hasExploded = False
    if depth == 4:
        explodePair(pair)
        return True
    if not isinstance(pair.left, int):
        hasExploded = explodeIfNecessary(pair.left, depth + 1)
    if not hasExploded and not isinstance(pair.right, int):
        hasExploded = explodeIfNecessary(pair.right, depth + 1)
    return hasExploded


def splitPair(splitNum):
    newLeft = int(math.floor(splitNum / 2.0))
    newRight = int(math.ceil(splitNum / 2.0))
    return Pair(newLeft, newRight)


def splitIfNecessary(pair):
    hasSplit = False
    if isinstance(pair.left, int):
        if pair.left >= 10:
            pair.left = splitPair(pair.left)
            pair.left.setParent(pair)
            return True
    else:
        hasSplit = splitIfNecessary(pair.left)
    if not hasSplit and isinstance(pair.right, int):
        if pair.right >= 10:
            pair.right = splitPair(pair.right)
            pair.right.setParent(pair)
            return True
    elif not hasSplit:
        hasSplit = splitIfNecessary(pair.right)
    return hasSplit


def snailReduce(pair):
    if explodeIfNecessary(pair, 0):
        snailReduce(pair)
    if splitIfNecessary(pair):
        snailReduce(pair)


def addPairs(first, second):
    newPair = Pair(first, second)
    first.setParent(newPair)
    second.setParent(newPair)
    snailReduce(newPair)
    return newPair


def addList(pairList):
    if len(pairList) == 1:
        return pairList[0]
    newPair = addPairs(pairList[0], pairList[1])
    for x in range(2, len(pairList)):
        newPair = addPairs(newPair, pairList[x])
    return newPair


def findLargestMag(pairList):
    largest = 0
    for x in range(len(pairList)):
        for y in range(len(pairList)):
            clone = copy.deepcopy(pairList)
            if x != y:
                added = addPairs(clone[x], clone[y])
                mag = added.getMagnitude()
                if mag > largest:
                    largest = mag
    return largest


def main(fileName):
    file = open(fileName, "r")

    pairList = processPairList(file)

    # PART ONE
    # newPair = addList(pairList)
    # print("Reduced Pair " + str(newPair))
    # print("Magnitude: " + str(newPair.getMagnitude()))

    # PART TWO
    largest = findLargestMag(pairList)
    print("Largest Magnitude: " + str(largest))


if __name__ == "__main__":
    main(sys.argv[1])
