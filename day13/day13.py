import heapq
import sys
from collections import defaultdict
from functools import reduce


def processCoordsAndFolds(file):
    coords = []
    line = file.readline().rstrip()
    while line != "":
        (x, y) = line.split(",")
        coords.append((int(x), int(y)))
        line = file.readline().rstrip()
    instructions = []
    line = file.readline().rstrip()
    while line:
        cutLine = line[11:].split("=")
        instructions.append((cutLine[0], int(cutLine[1])))
        line = file.readline().rstrip()
    return (coords, instructions)


def createGrid(coords, dims):
    grid = []
    for y in range(dims[1]):
        grid.append(["."] * dims[0])
    for coord in coords:
        grid[coord[1]][coord[0]] = "#"
    return grid


def printGrid(grid):
    for line in grid:
        for spot in line:
            print(spot + " ", end="")
        print("")


def findDims(instructions):
    xDim = yDim = 0
    for ins in instructions:
        if ins[0] == "x" and xDim == 0:
            xDim = ins[1] * 2 + 1
        if ins[0] == "y" and yDim == 0:
            yDim = ins[1] * 2 + 1
    return (xDim, yDim)


def foldLeft(grid, line):
    newGrid = []
    for y in range(len(grid)):
        newGrid.append([])
        for x in range(line):
            newGrid[y].append(grid[y][x])
    for y in range(len(grid)):
        for x in range(line + 1, len(grid[y])):
            mirrorX = line - abs(line - x)
            if mirrorX >= 0 and grid[y][x] == "#":
                newGrid[y][mirrorX] = grid[y][x]
    return newGrid


def foldUp(grid, line):
    newGrid = []
    for y in range(line):
        newGrid.append([])
        for x in range(len(grid[y])):
            newGrid[y].append(grid[y][x])
    for y in range(line + 1, len(grid)):
        for x in range(len(grid[y])):
            mirrorY = line - abs(line - y)
            if mirrorY >= 0 and grid[y][x] == "#":
                newGrid[mirrorY][x] = grid[y][x]
    return newGrid


def performInstruction(grid, instruction):
    if instruction[0] == "x":
        grid = foldLeft(grid, instruction[1])
    if instruction[0] == "y":
        grid = foldUp(grid, instruction[1])
    return grid


def countVisibleDots(grid):
    dots = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "#":
                dots += 1
    return dots


def partTwo(grid, instructions):
    for ins in instructions:
        grid = performInstruction(grid, ins)
    return grid


def main(fileName):
    file = open(fileName, "r")

    (coords, instructions) = processCoordsAndFolds(file)
    grid = createGrid(coords, findDims(instructions))
    printGrid(grid)

    # PART ONE
    # newGrid = performInstruction(grid, instructions[0])
    # print("After First Fold")
    # answer = countVisibleDots(newGrid)
    # printGrid(newGrid)
    # print("Visible dots: " + str(answer))

    # PART TWO
    grid = partTwo(grid, instructions)
    print("After all folds")
    printGrid(grid)


if __name__ == "__main__":
    main(sys.argv[1])
