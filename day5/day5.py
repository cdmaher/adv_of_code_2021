import sys


def processVentLines(file):
    ventLines = []
    for line in file:
        coords = line.split(" -> ")
        first = coords[0].split(",")
        second = coords[1].split(",")
        ventLines.append(
            ((int(first[0]), int(first[1])), (int(second[0]), int(second[1])))
        )
    return ventLines


def drawVertLine(ventLine, grid):
    start = ventLine[0] if ventLine[0][1] < ventLine[1][1] else ventLine[1]
    end = ventLine[0] if start == ventLine[1] else ventLine[1]
    for i in range(start[1], end[1] + 1):
        grid[i][ventLine[0][0]] += 1


def drawHorizLine(ventLine, grid):
    start = ventLine[0] if ventLine[0][0] < ventLine[1][0] else ventLine[1]
    end = ventLine[0] if start == ventLine[1] else ventLine[1]
    for i in range(start[0], end[0] + 1):
        grid[ventLine[0][1]][i] += 1


def drawDiagonalLine(ventLine, grid):
    start = ventLine[0] if ventLine[0][0] < ventLine[1][0] else ventLine[1]
    end = ventLine[0] if start == ventLine[1] else ventLine[1]
    isGoingUp = end[1] < start[1]
    index = 0
    for i in range(start[0], end[0] + 1):
        yOffset = start[1] - index if isGoingUp else start[1] + index
        grid[yOffset][i] += 1
        index += 1


def drawLinesToGrid(ventLines, grid):
    for ventLine in ventLines:
        if ventLine[0][0] != ventLine[1][0] and ventLine[0][1] != ventLine[1][1]:
            drawDiagonalLine(ventLine, grid)
        elif ventLine[0][0] == ventLine[1][0]:
            drawVertLine(ventLine, grid)
        elif ventLine[0][1] == ventLine[1][1]:
            drawHorizLine(ventLine, grid)


def printGrid(grid):
    for line in grid:
        for spot in line:
            mark = "." if spot == 0 else str(spot)
            print(mark + " ", end="")
        print("")


def printVentLines(ventLines):
    for line in ventLines:
        print(line)


def getMaxDimensions(ventLines):
    maxX = maxY = 0
    for coords in ventLines:
        if coords[0][0] > maxX:
            maxX = coords[0][0]
        if coords[1][0] > maxX:
            maxX = coords[1][0]
        if coords[0][1] > maxY:
            maxY = coords[0][1]
        if coords[1][1] > maxY:
            maxY = coords[1][1]
    return (maxX + 1, maxY + 1)


def countDangerousAreas(grid):
    dangerCount = 0
    for line in grid:
        for spot in line:
            if spot >= 2:
                dangerCount += 1
    return dangerCount


def main(fileName):
    file = open(fileName, "r")
    ventLines = processVentLines(file)
    (x, y) = getMaxDimensions(ventLines)
    grid = []
    for i in range(y):
        grid.append([0] * x)
    drawLinesToGrid(ventLines, grid)
    printVentLines(ventLines)
    printGrid(grid)
    dangerCount = countDangerousAreas(grid)
    print("Answer: " + str(dangerCount))


if __name__ == "__main__":
    main(sys.argv[1])
