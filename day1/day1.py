import sys


def processFile(file):
    increaseNum = 0
    prev = None
    for line in file:
        curNum = int(line)
        if prev is not None:
            if curNum > prev:
                increaseNum += 1
        prev = curNum
    return increaseNum


def processFile2(file):
    lineNums = []
    for line in file:
        curNum = int(line)
        lineNums.append(curNum)
    windows = []
    for i in range(0, len(lineNums) - 2):
        windows.append(lineNums[i] + lineNums[i + 1] + lineNums[i + 2])

    increaseNum = 0
    prev = None
    for wind in windows:
        if prev is not None:
            if wind > prev:
                increaseNum += 1
        prev = wind

    return increaseNum


def main(fileName):
    file = open(fileName, "r")
    incNum = processFile2(file)
    print("Total increases: " + str(incNum))


if __name__ == "__main__":
    main(sys.argv[1])
