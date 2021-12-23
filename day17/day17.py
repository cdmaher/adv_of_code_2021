import heapq
import sys
from collections import defaultdict
from functools import reduce


GRID_DIMENSIONS = 600
GRID_HALF = int(GRID_DIMENSIONS / 2)


def processTargetArea(file):
    (xArea, yArea) = file.readline().rstrip().split(", ")
    (x1, x2) = xArea.split("=")[1].split("..")
    (y1, y2) = yArea.split("=")[1].split("..")
    return ((int(x1), int(x2)), (int(y1), int(y2)))


def createGridWithTargetArea(targetArea):
    grid = []
    for x in range(GRID_DIMENSIONS):
        grid.append(["."] * GRID_DIMENSIONS)
    placeInGrid(grid, 0, 0, "S")
    for i in range(targetArea[1][0], targetArea[1][1] + 1):
        for j in range(targetArea[0][0], targetArea[0][1] + 1):
            placeInGrid(grid, j, i, "T")
    return grid


def placeInGrid(grid, x, y, val):
    transX = x + GRID_HALF
    transY = (-1 * y) + GRID_HALF
    grid[transY][transX] = val


def getGridVal(grid, x, y):
    transX = x + GRID_HALF
    transY = (-1 * y) + GRID_HALF
    return grid[transY][transX]


def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end="")
        print("")


def isInBounds(location):
    transX = location[0] + GRID_HALF
    transY = (-1 * location[1]) + GRID_HALF
    return (
        transY >= 0
        and transY < GRID_DIMENSIONS
        and transX >= 0
        and transX < GRID_DIMENSIONS
    )


def isInTargetArea(location, targetArea):
    return (
        location[0] >= targetArea[0][0]
        and location[0] <= targetArea[0][1]
        and location[1] >= targetArea[1][0]
        and location[1] <= targetArea[1][1]
    )


def hasMissedTarget(location, targetArea):
    return location[1] < targetArea[1][0] or location[0] > targetArea[0][1]


def shotStep(grid, projectLoc, velX, velY, targetArea):
    nextStep = (projectLoc[0] + velX, projectLoc[1] + velY)
    isHit = False
    if isInTargetArea(nextStep, targetArea):
        isHit = True
        # placeInGrid(grid, nextStep[0], nextStep[1], "#")
    return (nextStep, isHit)


def shootProjectile(grid, velX, velY, targetArea):
    projectLoc = (0, 0)
    isHit = False
    highestY = 0
    while not hasMissedTarget(projectLoc, targetArea) and not isHit:
        (projectLoc, isHit) = shotStep(grid, projectLoc, velX, velY, targetArea)
        if projectLoc[1] > highestY:
            highestY = projectLoc[1]
        if velX > 0:
            velX -= 1
        elif velX < 0:
            velX += 1
        velY -= 1
    return (isHit, highestY)


def findMaxVelocity(grid, targetArea):
    curY = targetArea[1][0]
    xMult = 1 if targetArea[0][0] > 0 else -1
    xValHasHit = True
    heightDict = {}
    highestY = 0
    totalHits = 0
    while curY < 1000:
        xValHasHit = False
        for x in range(0, targetArea[0][1] + 1):
            (xValHasHit, curHighY) = shootProjectile(grid, x, curY, targetArea)
            if xValHasHit and curHighY > highestY:
                highestY = curHighY
            if xValHasHit:
                totalHits += 1
        curY += 1
    print("Found max y velocity " + str(curY - 1))
    print("Found highest y: " + str(highestY))
    print("Total hits " + str(totalHits))


def main(fileName):
    file = open(fileName, "r")

    targetArea = processTargetArea(file)

    grid = createGridWithTargetArea(targetArea)
    highestY = findMaxVelocity(grid, targetArea)


if __name__ == "__main__":
    main(sys.argv[1])
