import heapq
import sys
from collections import defaultdict
from functools import reduce

TOTAL_STEPS = 100


def processOctos(file):
    octos = []
    for line in file:
        octos.append(list(map(int, list(line.rstrip()))))
    return octos


def increaseEnergy(octos):
    for i in range(len(octos)):
        for j in range(len(octos[i])):
            octos[i][j] += 1
            if octos[i][j] > 9:
                octos[i][j] = -1


def performFlash(octos, i, j):
    flashes = 1
    octos[i][j] = 0
    for y in range(i - 1, i + 2):
        for x in range(j - 1, j + 2):
            if (
                y >= 0
                and y < len(octos)
                and x >= 0
                and x < len(octos[y])
                and octos[y][x] > 0
            ):
                octos[y][x] += 1
                if octos[y][x] > 9:
                    octos[y][x] = -1
                    flashes += performFlash(octos, y, x)
    return flashes


def runFlashStep(octos):
    totalFlashes = 0
    increaseEnergy(octos)
    for i in range(len(octos)):
        for j in range(len(octos[i])):
            if octos[i][j] == -1:
                totalFlashes += performFlash(octos, i, j)
    return totalFlashes


def runSteps(octos):
    totalFlashes = 0
    for x in range(TOTAL_STEPS):
        totalFlashes += runFlashStep(octos)
    return totalFlashes

def printOctos(octos):
    for line in octos:
        for octo in line:
            print(str(octo), end='')
        print('')


def runPartTwo(octos):
    step = 0
    while not isSimulFlash(octos):
        runFlashStep(octos)
        step += 1
    return step

def isSimulFlash(octos):
    for i in range(len(octos)):
        for j in range(len(octos[i])):
            if octos[i][j] != 0:
                return False
    return True

def main(fileName):
    file = open(fileName, "r")

    lines = processOctos(file)

    # PART ONE
    # flashes = runSteps(lines)
    # print("Total flashes: " + str(flashes))

    # PART TWO
    steps = runPartTwo(lines)
    print("Total steps: " + str(steps))


if __name__ == "__main__":
    main(sys.argv[1])
