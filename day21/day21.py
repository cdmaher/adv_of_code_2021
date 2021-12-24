import copy
import heapq
import math
import sys
from collections import Counter
from collections import defaultdict
from functools import reduce, lru_cache
from itertools import product
from typing import Tuple

WINNING_SCORE = 1000

DIRAC_SCORE = 21

ROLLS_ARR = [
    3,
    4,
    5,
    4,
    5,
    6,
    5,
    6,
    7,
    4,
    5,
    6,
    5,
    6,
    7,
    6,
    7,
    8,
    5,
    6,
    7,
    6,
    7,
    8,
    7,
    8,
    9,
]


def processStartingPositions(file):
    player1 = int(file.readline().rstrip()[-1])
    player2 = int(file.readline().rstrip()[-1])
    return (player1, player2)


def playerTurn(curSpot, die):
    toMove = die
    die = die + 1 if die < 100 else 1
    toMove += die
    die = die + 1 if die < 100 else 1
    toMove += die
    die = die + 1 if die < 100 else 1
    newSpot = curSpot + (toMove % 10)
    if newSpot > 10:
        newSpot -= 10
    return (newSpot, die)


def playGame(player1Spot, player2Spot):
    die = 1
    dieRolls = 0
    p1Score = p2Score = 0
    while p1Score < WINNING_SCORE and p2Score < WINNING_SCORE:
        (player1Spot, die) = playerTurn(player1Spot, die)
        p1Score += player1Spot
        dieRolls += 3
        if p1Score >= WINNING_SCORE:
            declareWinner(p2Score, dieRolls)
            return
        (player2Spot, die) = playerTurn(player2Spot, die)
        p2Score += player2Spot
        dieRolls += 3
        if p2Score >= WINNING_SCORE:
            declareWinner(p1Score, dieRolls)
            return


def getPossibleRolls():
    roll1 = [1, 2, 3]
    roll2 = []
    for i in range(1, 4):
        for x in roll1:
            roll2.append(i + x)
    roll3 = []
    for i in range(1, 4):
        for x in roll2:
            roll3.append(i + x)
    print(str(roll3))


def diracPlayerTurn(curSpot):
    newSpots = []
    for roll in ROLLS_ARR:
        newSpots.append(curSpot + (roll % 10))
        if newSpots[-1] > 10:
            newSpots[-1] -= 10
    return newSpots


def playDiracGame(curPlayerTurn, playerScore, otherPlayerTurn, otherPlayerScore):
    curPlayerWins = otherPlayerWins = 0
    player1Spots = diracPlayerTurn(curPlayerTurn)
    for spot in player1Spots:
        if playerScore + spot >= DIRAC_SCORE:
            curPlayerWins += 1
        else:
            (otherWins, curWins) = playDiracGame(
                otherPlayerTurn, otherPlayerScore, spot, playerScore + spot
            )
            curPlayerWins += curWins
            otherPlayerWins += otherWins
    return (curPlayerWins, otherPlayerWins)


def playDiracGameCaching(
    player1Spot, player1Score, player2Spot, player2Score, turn, cacheState
):
    if (player1Spot, player1Score, player2Spot, player2Score, turn) in cacheState:
        return cacheState[(player1Spot, player1Score, player2Spot, player2Score, turn)]
    player1Wins = player2Wins = 0
    playerSpots = diracPlayerTurn(player1Spot if turn == 1 else player2Spot)
    for spot in playerSpots:
        if turn == 1 and player1Score + spot >= DIRAC_SCORE:
            player1Wins += 1
        elif turn == 2 and player2Score + spot >= DIRAC_SCORE:
            player2Wins += 1
        else:
            (wins1, wins2) = playDiracGameCaching(
                player1Spot,
                player1Score,
                player2Spot,
                player2Score,
                1 if turn == 2 else 2,
                cacheState,
            )
            player1Wins += wins1
            player2Wins += wins2
    cacheState[(player1Spot, player1Score, player2Spot, player2Score, turn)] = (
        player1Wins,
        player2Wins,
    )
    return (player1Wins, player2Wins)


def declareWinner(loserScore, dieRolls):
    print("Lost with " + str(loserScore) + " and " + str(dieRolls) + " die rolls")
    print("Answer: " + str(loserScore * dieRolls))


def main(fileName):
    file = open(fileName, "r")

    (player1, player2) = processStartingPositions(file)

    # PART ONE
    # playGame(player1, player2)

    # PART TWO
    (win1, win2) = playDiracGameCaching(player1, 0, player2, 0, 1, {})
    print("Player 1 Wins: " + str(win1) + " Player 2 Wins: " + str(win2))


if __name__ == "__main__":
    main(sys.argv[1])
