import copy
import heapq
import math
import sys
from collections import defaultdict
from functools import reduce


IMAGE_SIZE = 400

ENHANCEMENTS = 50


def processAlgorithmAndImage(file):
    algorithm = file.readline().rstrip()
    file.readline()
    line = file.readline().rstrip()
    image = []
    while line != "":
        image.append(list(line))
        line = file.readline().rstrip()
    return (algorithm, image)


def isInBounds(x, y, imageLen):
    return y >= 0 and y < imageLen and x >= 0 and x < imageLen


def getNewPixelVal(algorithm, image, x, y):
    binNum = ""
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if not isInBounds(j, i, len(image)):
                binNum += image[y][x]
            else:
                binNum += image[i][j]
    converted = int("".join(list(map(lambda x: "0" if x == "." else "1", binNum))), 2)
    return algorithm[converted]


def enhanceImage(algorithm, image):
    newImage = copy.deepcopy(image)
    for i in range(len(image)):
        for j in range(len(image[i])):
            val = getNewPixelVal(algorithm, image, j, i)
            newImage[i][j] = val
    return newImage


def extendImage(image):
    border = int((IMAGE_SIZE - len(image)) / 2)
    for x in range(len(image)):
        image[x] = (["."] * border) + image[x] + (["."] * border)
    for y in range(border):
        image.insert(0, (["."] * IMAGE_SIZE))
        image.append((["."] * IMAGE_SIZE))


def printImage(image):
    for line in image:
        for pixel in line:
            print(pixel, end="")
        print("")


def numLitPixels(image):
    numLit = 0
    for line in image:
        for pixel in line:
            if pixel == "#":
                numLit += 1
    return numLit


def runEnhancement(algorithm, image):
    for x in range(ENHANCEMENTS):
        image = enhanceImage(algorithm, image)
    return image


def main(fileName):
    file = open(fileName, "r")

    (algorithm, image) = processAlgorithmAndImage(file)
    extendImage(image)
    printImage(image)
    image = runEnhancement(algorithm, image)
    printImage(image)
    print("Num lit pixels " + str(numLitPixels(image)))


if __name__ == "__main__":
    main(sys.argv[1])
