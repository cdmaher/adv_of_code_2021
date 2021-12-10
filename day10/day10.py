import heapq
import sys
from collections import defaultdict
from functools import reduce


def processLines(file):
    lines = []
    for line in file:
        lines.append(list(line.rstrip()))
    return lines


def isOpenChunk(char):
    return char == '(' or char == '[' or char == '{' or char == '<'

def isMatching(open, close):
    if open == '(':
        return close == ')'
    if open == '{' :
        return close == '}'
    if open == '[':
        return close == ']'
    if open == '<':
        return close == '>'
    return False

def findIllegalLineScore(line):
    chunkStack = []
    for char in line:
        if isOpenChunk(char):
            chunkStack.append(char)
        else:
            toPop = chunkStack.pop()
            if not isMatching(toPop, char):
                return getErrorScore(char)
    return 0

def getIncompleteLine(lines):
    chunkStack = []
    for char in lines:
        if isOpenChunk(char):
            chunkStack.append(char)
        else:
            toPop = chunkStack.pop()
            if not isMatching(toPop, char):
                return None
    return chunkStack

def getCompletionScore(char):
    if char == '(':
        return 1
    if char == '[':
        return 2
    if char == '{':
        return 3
    if char == '<':
        return 4
    return 0

def getIncompleteLineScore(chunkStack):
    totalScore = 0
    while len(chunkStack) > 0:
        curChar = chunkStack.pop()
        totalScore  = totalScore * 5 + getCompletionScore(curChar)
    return totalScore

def partTwoAnswer(lines):
    lineScores = []
    for line in lines:
        incLine = getIncompleteLine(line)
        if incLine != None:
            lineScores.append(getIncompleteLineScore(incLine))
    lineScores.sort()
    return lineScores[int(len(lineScores) / 2)]


def getErrorScore(illegalChar):
    if illegalChar == ')':
        return 3
    if illegalChar == ']':
        return 57
    if illegalChar == '}':
        return 1197
    if illegalChar == '>':
        return 25137
    return 0

def partOneAnswer(lines):
    score = 0
    for line in lines:
        score += findIllegalLineScore(line)
    return score


def main(fileName):
    file = open(fileName, "r")

    lines = processLines(file)
    score = partOneAnswer(lines)
    print("Total Illegal Char score: " + str(score))

    partTwoScore = partTwoAnswer(lines)
    print('Middle Completion Score: ' + str(partTwoScore))


if __name__ == "__main__":
    main(sys.argv[1])
