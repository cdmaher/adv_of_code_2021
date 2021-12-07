import sys


def processNumberDraws(file):
    firstLine = file.readline()
    return list(map(int, firstLine.rstrip().split(",")))


def processBoards(file):
    file.readline()
    boards = []
    while curLine := file.readline():
        curBoard = []
        for _ in range(0, 5):
            curNums = list(map(lambda x: (int(x), False), curLine.split()))
            curBoard.append(curNums)
            curLine = file.readline().rstrip()
        boards.append(curBoard)
    return boards


def printBoardLine(boardLine):
    for spot in boardLine:
        markIndicator = "X" if spot[1] else "_"
        print(str(spot[0]) + markIndicator + " ", end="")
    print("")


def printBoards(boards):
    for board in boards:
        for line in board:
            printBoardLine(line)
        print("")


def markBoards(boards, markNum):
    for board in boards:
        for line in board:
            index = 0
            for spot in line:
                if spot[0] == markNum:
                    line[index] = (spot[0], True)
                index += 1


def announceWinner(board, winningNum):
    unMarkedSum = 0
    print("Winner!")
    printBoards([board])
    for line in board:
        for spot in line:
            if not spot[1]:
                unMarkedSum += spot[0]
    print("Unmarked sum: " + str(unMarkedSum))
    print("Num drawn: " + str(winningNum))
    print("Answer: " + str(unMarkedSum * winningNum))


def checkHorizLines(board):
    for line in board:
        canWin = True
        for spot in line:
            if not spot[1]:
                canWin = False
                break
        if canWin:
            return True
    return False


def checkVertLines(board):
    for i in range(0, 5):
        canWin = True
        for line in board:
            if not line[i][1]:
                canWin = False
                break
        if canWin:
            return True
    return False


def checkBoards(boards, numToDraw):
    winners = []
    index = 0
    for board in boards:
        if checkHorizLines(board) or checkVertLines(board):
            # PART ONE
            # announceWinner(board, numToDraw)
            winners.append(index)
        index += 1
    winners.reverse()
    return winners


def playBingo(numDraws, boards):
    currentBoards = list(boards)
    for numToDraw in numDraws:
        markBoards(currentBoards, numToDraw)
        winners = checkBoards(currentBoards, numToDraw)
        if len(winners) > 0:
            if len(winners) == 1 and len(currentBoards) == 1:
                announceWinner(currentBoards[0], numToDraw)
                break
            else:
                for ind in winners:
                    currentBoards.pop(ind)


def main(fileName):
    file = open(fileName, "r")
    draws = processNumberDraws(file)
    boards = processBoards(file)
    printBoards(boards)
    playBingo(draws, boards)


if __name__ == "__main__":
    main(sys.argv[1])
