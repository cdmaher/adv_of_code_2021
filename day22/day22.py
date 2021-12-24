import copy
import heapq
import math
import sys
from collections import Counter
from collections import defaultdict
from functools import reduce, lru_cache
from itertools import product
from typing import Tuple

GRID_BOUNDS = 150
GRID_HALF = int(GRID_BOUNDS / 2)


class Step:
    def __init__(self, onOff, x, y, z):
        self.onOff = onOff
        self.x = x
        self.y = y
        self.z = z

    def isNotInit(self):
        return (
            self.x[0] > 50
            or self.x[0] < -50
            or self.y[0] > 50
            or self.y[0] < -50
            or self.z[0] > 50
            or self.z[0] < -50
        )

    def __str__(self):
        return self.onOff + str(self.x) + "," + str(self.y) + "," + str(self.z)

    __repr__ = __str__


def processSteps(file):
    steps = []
    for line in file:
        splitLine = line.rstrip().split(" ")
        coords = splitLine[1].split(",")
        bounds = []
        for coord in coords:
            vals = coord.split("=")[1].split("..")
            bounds.append((int(vals[0]), int(vals[1])))
        steps.append(Step(splitLine[0], bounds[0], bounds[1], bounds[2]))
    return steps


def placeInGrid(grid, x, y, z, val):
    grid[x + GRID_HALF][y + GRID_HALF][z + GRID_HALF] = val


def activateGrid(step, grid):
    for x in range(step.x[0], step.x[1] + 1):
        for y in range(step.y[0], step.y[1] + 1):
            for z in range(step.z[0], step.z[1] + 1):
                if step.onOff == "on":
                    placeInGrid(grid, x, y, z, 1)
                else:
                    placeInGrid(grid, x, y, z, 0)


def runInitialSteps(steps, grid):
    for x in steps:
        if x.isNotInit():
            break
        else:
            activateGrid(x, grid)


def countOnCubes(grid):
    onCount = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            for z in range(len(grid[x][y])):
                if grid[x][y][z] == 1:
                    onCount += 1
    return onCount


def createGrid():
    grid = []
    for x in range(GRID_BOUNDS):
        grid.append([])
        for y in range(GRID_BOUNDS):
            grid[x].append([0] * GRID_BOUNDS)
    return grid


def main(fileName):
    file = open(fileName, "r")

    steps = processSteps(file)
    grid = createGrid()
    runInitialSteps(steps, grid)
    print("Total on " + str(countOnCubes(grid)))


if __name__ == "__main__":
    main(sys.argv[1])
