import sys
from collections import defaultdict


def processEntries(file):
    entries = []
    for line in file:
        (inputs, outputs) = line.rstrip().split("|")
        entries.append((inputs.split(), outputs.split()))
    return entries


def countUniqueOutputDigits(entries):
    numUnique = 0
    for entry in entries:
        for signal in entry[1]:
            if (
                len(signal) == 2
                or len(signal) == 4
                or len(signal) == 3
                or len(signal) == 7
            ):
                numUnique += 1
    return numUnique


def deduceMappingConfig(entryLine):
    startingSet = set("abcdefg")
    mapping = [
        startingSet,
        startingSet,
        startingSet,
        startingSet,
        startingSet,
        startingSet,
        startingSet,
    ]
    totalSignals = entryLine[0] + entryLine[1]
    for inp in totalSignals:
        inpSet = set(inp)
        if len(inp) == 2:
            mapping[0] = mapping[0].difference(inpSet)
            mapping[1] = mapping[1].difference(inpSet)
            mapping[2] = mapping[2].intersection(inpSet)
            mapping[3] = mapping[3].difference(inpSet)
            mapping[4] = mapping[4].difference(inpSet)
            mapping[5] = mapping[5].intersection(inpSet)
            mapping[6] = mapping[6].difference(inpSet)
        elif len(inp) == 4:
            mapping[0] = mapping[0].difference(inpSet)
            mapping[1] = mapping[1].intersection(inpSet)
            mapping[2] = mapping[2].intersection(inpSet)
            mapping[3] = mapping[3].intersection(inpSet)
            mapping[4] = mapping[4].difference(inpSet)
            mapping[5] = mapping[5].intersection(inpSet)
            mapping[6] = mapping[6].difference(inpSet)
        elif len(inp) == 3:
            mapping[0] = mapping[0].intersection(inpSet)
            mapping[1] = mapping[1].difference(inpSet)
            mapping[2] = mapping[2].intersection(inpSet)
            mapping[3] = mapping[3].difference(inpSet)
            mapping[4] = mapping[4].difference(inpSet)
            mapping[5] = mapping[5].intersection(inpSet)
            mapping[6] = mapping[6].difference(inpSet)
    for inp in totalSignals:
        inpSet = set(inp)
        if len(inp) == 6:
            # Try 0
            zeroAttempt = mapping[3].difference(inpSet)
            if len(zeroAttempt) == 0:
                # Try 6
                sixAttempt = mapping[2].difference(inpSet)
                if len(sixAttempt) == 0:
                    # Must be 9
                    mapping[0] = mapping[0].intersection(inpSet)
                    mapping[1] = mapping[1].intersection(inpSet)
                    mapping[2] = mapping[2].intersection(inpSet)
                    mapping[3] = mapping[3].intersection(inpSet)
                    mapping[4] = mapping[4].difference(inpSet)
                    mapping[5] = mapping[5].intersection(inpSet)
                    mapping[6] = mapping[6].intersection(inpSet)
                else:
                    mapping[0] = mapping[0].intersection(inpSet)
                    mapping[1] = mapping[1].intersection(inpSet)
                    mapping[2] = mapping[2].difference(inpSet)
                    mapping[3] = mapping[3].intersection(inpSet)
                    mapping[4] = mapping[4].intersection(inpSet)
                    mapping[5] = mapping[5].intersection(inpSet)
                    mapping[6] = mapping[6].intersection(inpSet)
            else:
                mapping[0] = mapping[0].intersection(inpSet)
                mapping[1] = mapping[1].intersection(inpSet)
                mapping[2] = mapping[2].intersection(inpSet)
                mapping[3] = mapping[3].difference(inpSet)
                mapping[4] = mapping[4].intersection(inpSet)
                mapping[5] = mapping[5].intersection(inpSet)
                mapping[6] = mapping[6].intersection(inpSet)
    toStrMap = list(map(lambda x: list(x)[0], mapping))
    return getDigitMapping(toStrMap)


def getDigitMapping(mapping):
    digitMap = {}
    digitMap[
        mapping[0] + mapping[1] + mapping[2] + mapping[4] + mapping[5] + mapping[6]
    ] = 0
    digitMap[mapping[2] + mapping[5]] = 1
    digitMap[mapping[0] + mapping[2] + mapping[3] + mapping[4] + mapping[6]] = 2
    digitMap[mapping[0] + mapping[2] + mapping[3] + mapping[5] + mapping[6]] = 3
    digitMap[mapping[1] + mapping[2] + mapping[3] + mapping[5]] = 4
    digitMap[mapping[0] + mapping[1] + mapping[3] + mapping[5] + mapping[6]] = 5
    digitMap[
        mapping[0] + mapping[1] + mapping[3] + mapping[4] + mapping[5] + mapping[6]
    ] = 6
    digitMap[mapping[0] + mapping[2] + mapping[5]] = 7
    digitMap[
        mapping[0]
        + mapping[1]
        + mapping[2]
        + mapping[3]
        + mapping[4]
        + mapping[5]
        + mapping[6]
    ] = 8
    digitMap[
        mapping[0] + mapping[1] + mapping[2] + mapping[3] + mapping[5] + mapping[6]
    ] = 9
    sortedMap = {}
    for digit in digitMap:
        sortedMap["".join(sorted(digit))] = digitMap[digit]
    return sortedMap


def partTwoAnswer(entries):
    digitSum = 0
    for entry in entries:
        mapping = deduceMappingConfig(entry)
        digitSum += decodeOutput(entry[1], mapping)
    return digitSum


def decodeOutput(output, digitMap):
    outNum = ""
    for digit in output:
        outNum += str(digitMap["".join(sorted(digit))])
    return int(outNum)


def main(fileName):
    file = open(fileName, "r")
    entries = processEntries(file)

    # PART ONE
    # uniqueDigits = countUniqueOutputDigits(entries)
    # print("Unique digit appearances: ", uniqueDigits)

    answer = partTwoAnswer(entries)
    print("Part two answer: ", answer)


if __name__ == "__main__":
    main(sys.argv[1])
