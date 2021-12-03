import sys


def processFile(file):
    numList = []
    for line in file:
        numList.append(line.rstrip())
    return numList


def getGammaRate(numList):
    gamma = ""
    for i in range(0, len(numList[0])):
        ones = 0
        zeros = 0
        for j in range(0, len(numList)):
            if numList[j][i] == "1":
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            gamma += "1"
        else:
            gamma += "0"
    return gamma


def getEpsilonRate(gammaRate):
    return str((1 << len(gammaRate)) - 1 - int(gammaRate, 2))


def getOxygenGeneratorRating(numList):
    filterList = list(numList)
    currentBit = 0
    while len(filterList) != 1:
        newList = []
        zeros = ones = 0
        mostCommon = ""
        for j in range(0, len(filterList)):
            if filterList[j][currentBit] == "1":
                ones += 1
            else:
                zeros += 1
        if ones >= zeros:
            mostCommon = "1"
        else:
            mostCommon = "0"
        for j in range(0, len(filterList)):
            if filterList[j][currentBit] == mostCommon:
                newList.append(filterList[j])
        currentBit += 1
        filterList = list(newList)
    return filterList[0]


def getCO2ScrubberRating(numList):
    filterList = list(numList)
    currentBit = 0
    while len(filterList) != 1:
        newList = []
        zeros = ones = 0
        leastCommon = ""
        for j in range(0, len(filterList)):
            if filterList[j][currentBit] == "1":
                ones += 1
            else:
                zeros += 1
        if zeros <= ones:
            leastCommon = "0"
        else:
            leastCommon = "1"
        for j in range(0, len(filterList)):
            if filterList[j][currentBit] == leastCommon:
                newList.append(filterList[j])
        currentBit += 1
        filterList = list(newList)
    return filterList[0]


def main(fileName):
    file = open(fileName, "r")
    numList = processFile(file)

    # Part ONE
    # gamma = getGammaRate(numList)
    # print("Gamma rate: " + gamma)
    # epsilon = getEpsilonRate(gamma)
    # print("Epsilon rate: " + epsilon)
    # print("answer: " + str(int(gamma, 2) * int(epsilon)))

    # Part TWO
    oxygenRating = getOxygenGeneratorRating(numList)
    print("Oxygen Generator Rating: " + oxygenRating)
    co2Rating = getCO2ScrubberRating(numList)
    print("CO2 Scrubber Rating: " + co2Rating)
    print("answer: " + str(int(oxygenRating, 2) * int(co2Rating, 2)))


if __name__ == "__main__":
    main(sys.argv[1])
