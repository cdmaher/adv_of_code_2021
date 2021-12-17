import heapq
import sys
from collections import defaultdict
from functools import reduce


class CavePos:
    def __init__(self, x, y, risk):
        self.x = x
        self.y = y
        self.risk = risk
        self.cameFrom = None
        self.gScore = 999999999
        self.fScore = 999999999

    def setFScore(self, fScore):
        if fScore < self.fScore:
            self.fScore = fScore

    def setGScore(self, gScore):
        if gScore < self.gScore:
            self.gScore = gScore

    def getGScore(self):
        return self.gScore

    def setCameFrom(self, cameFrom):
        self.cameFrom = cameFrom

    def __lt__(self, other):
        return self.x > other.x


def processMaze(file):
    maze = []
    lineNum = 0
    for line in file:
        maze.append([])
        splitLine = list(line.rstrip())
        for x in range(len(splitLine)):
            maze[lineNum].append(CavePos(x, lineNum, int(splitLine[x])))
        lineNum += 1
    return maze


def manhattanDistanceToGoal(maze, x, y):
    return (len(maze) - x) + (len(maze) - y)


def getNeighbors(maze, x, y):
    neighbors = []
    if x > 0:
        neighbors.append(maze[y][x - 1])
    if x < len(maze[y]) - 1:
        neighbors.append(maze[y][x + 1])
    if y > 0:
        neighbors.append(maze[y - 1][x])
    if y < len(maze) - 1:
        neighbors.append(maze[y + 1][x])
    return neighbors


def isGoal(maze, x, y):
    return y == len(maze) - 1 and x == len(maze[y]) - 1


def addUpRiskScore(goalPos):
    current = goalPos
    score = 0
    while current is not None:
        if current.cameFrom is not None:
            score += current.risk
        current = current.cameFrom
    return score


def createPartTwoMaze(origMaze):
    maze = []
    for newY in range(len(origMaze) * 5):
        maze.append([0] * len(origMaze) * 5)
    for yScale in range(5):
        for xScale in range(5):
            for i in range(len(origMaze)):
                for j in range(len(origMaze[i])):
                    newX = len(origMaze) * xScale + j
                    newY = len(origMaze) * yScale + i
                    newScore = origMaze[i][j].risk + yScale + xScale
                    if newScore > 9:
                        newScore -= 9
                    maze[newY][newX] = CavePos(newX, newY, newScore)
    return maze


def findIdealPath(maze):
    spotsToCheck = []
    gStart = manhattanDistanceToGoal(maze, 0, 0)
    maze[0][0].setFScore(gStart)
    maze[0][0].setGScore(0)
    heapq.heappush(spotsToCheck, (gStart, maze[0][0]))
    while len(spotsToCheck) > 0:
        (fScore, current) = heapq.heappop(spotsToCheck)
        if isGoal(maze, current.x, current.y):
            return addUpRiskScore(current)

        neighbors = getNeighbors(maze, current.x, current.y)
        for neighbor in neighbors:
            newGScore = current.getGScore() + neighbor.risk
            if newGScore < neighbor.getGScore():
                neighbor.setGScore(newGScore)
                fScore = newGScore + manhattanDistanceToGoal(
                    maze, neighbor.x, neighbor.y
                )
                neighbor.setFScore(fScore)
                neighbor.setCameFrom(current)
                heapq.heappush(spotsToCheck, (fScore, neighbor))

    return None


def main(fileName):
    file = open(fileName, "r")

    maze = processMaze(file)

    # PART TWO
    maze = createPartTwoMaze(maze)

    score = findIdealPath(maze)
    print("Best Path: " + str(score))


if __name__ == "__main__":
    main(sys.argv[1])
