import sys
from collections import defaultdict


DAYS_TO_SIM = 256


def processLanternFish(file):
    starters = file.readline().rstrip().split(",")
    fishes = defaultdict(int)
    for startFish in starters:
        fishes[int(startFish)] += 1
    return fishes


def simulateDays(fish, daysToSim):
    for i in range(daysToSim):
        numZeros = fish[0]
        for x in range(1, 9):
            fish[x - 1] = fish[x]
            fish[x] = 0
        fish[8] = numZeros
        fish[6] += numZeros
    return fish


def countFish(fish):
    total = 0
    for k in fish:
        total += fish[k]
    return total


def main(fileName):
    file = open(fileName, "r")
    fish = processLanternFish(file)
    fish = simulateDays(fish, DAYS_TO_SIM)
    print("the fish", fish)
    print("After " + str(DAYS_TO_SIM) + " days, num fish: " + str(countFish(fish)))


if __name__ == "__main__":
    main(sys.argv[1])
