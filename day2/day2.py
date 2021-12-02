import sys


def processFile(file):
    instructions = []
    for line in file:
        splitLine = line.split(" ")
        instructions.append((splitLine[0], int(splitLine[1])))

    depth = horiz = 0
    for ins in instructions:
        if ins[0] == "forward":
            horiz += ins[1]
        elif ins[0] == "up":
            depth -= ins[1]
        else:  # must be down
            depth += ins[1]
    return (horiz, depth)


def processFile2(file):
    instructions = []
    for line in file:
        splitLine = line.split(" ")
        instructions.append((splitLine[0], int(splitLine[1])))

    depth = horiz = aim = 0
    for ins in instructions:
        if ins[0] == "forward":
            horiz += ins[1]
            depth += ins[1] * aim
        elif ins[0] == "up":
            aim -= ins[1]
        else:  # must be down
            aim += ins[1]
    return (horiz, depth)


def main(fileName):
    file = open(fileName, "r")
    (horiz, depth) = processFile2(file)
    print("horiz: " + str(horiz))
    print("depth: " + str(depth))
    print("Answer: " + str(horiz * depth))


if __name__ == "__main__":
    main(sys.argv[1])
