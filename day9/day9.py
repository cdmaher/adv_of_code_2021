import heapq
import sys
from collections import defaultdict
from functools import reduce


def processHeightMap(file):
    heightMap = []
    for line in file:
        horiz = list(map(int, list(line.rstrip())))
        heightMap.append(horiz)
    return heightMap


def processHeightMapPartTwo(file):
    heightMap = []
    for line in file:
        horiz = list(map(lambda x: (int(x), False), list(line.rstrip())))
        heightMap.append(horiz)
    return heightMap


def printHeightMap(heightMap):
    for line in heightMap:
        for num in line:
            print(str(num), end="")
        print("")


def findLowPoints(heightMap):
    lowPoints = []
    for i in range(len(heightMap)):
        for j in range(len(heightMap[i])):
            if isLowPoint(heightMap, j, i):
                lowPoints.append(heightMap[i][j])
    return lowPoints


def isLowPoint(heightMap, x, y):
    point = heightMap[y][x]
    if x > 0 and point >= heightMap[y][x - 1]:
        return False
    if x < len(heightMap[y]) - 1 and point >= heightMap[y][x + 1]:
        return False
    if y > 0 and point >= heightMap[y - 1][x]:
        return False
    if y < len(heightMap) - 1 and point >= heightMap[y + 1][x]:
        return False
    return True


def partOneAnswer(heightMap):
    lowPoints = findLowPoints(heightMap)
    lowPoints = list(map(lambda x: x + 1, lowPoints))
    return reduce(lambda a, b: a + b, lowPoints)


def shouldExplore(heightMap, x, y):
    return (
        y >= 0
        and y < len(heightMap)
        and x >= 0
        and x < len(heightMap[y])
        and heightMap[y][x][0] != 9
        and not heightMap[y][x][1]
    )


def calculateBasinSize(heightMap, x, y):
    curSize = 1
    heightMap[y][x] = (heightMap[y][x][0], True)
    if shouldExplore(heightMap, x - 1, y):
        curSize += calculateBasinSize(heightMap, x - 1, y)
    if shouldExplore(heightMap, x + 1, y):
        curSize += calculateBasinSize(heightMap, x + 1, y)
    if shouldExplore(heightMap, x, y - 1):
        curSize += calculateBasinSize(heightMap, x, y - 1)
    if shouldExplore(heightMap, x, y + 1):
        curSize += calculateBasinSize(heightMap, x, y + 1)
    return curSize


def findBasins(heightMap):
    basinSizes = []
    for i in range(len(heightMap)):
        for j in range(len(heightMap[i])):
            if heightMap[i][j][0] != 9 and not heightMap[i][j][1]:
                basinSizes.append(calculateBasinSize(heightMap, j, i))
    basinSizes.sort()
    return basinSizes


def partTwoAnswer(heightMap):
    basinSizes = findBasins(heightMap)
    answer = 1
    for i in range(3):
        answer *= basinSizes.pop()
    return answer


def main(fileName):
    file = open(fileName, "r")

    # PART ONE
    # heightMap = processHeightMap(file)
    # answer = partOneAnswer(heightMap)
    # print("Part one answer: ", str(answer))

    # PART TWO
    heightMap = processHeightMapPartTwo(file)
    answer = partTwoAnswer(heightMap)
    print("Part two answer: " + str(answer))


if __name__ == "__main__":
    main(sys.argv[1])
