import copy
import heapq
import math
import sys
from collections import defaultdict
from functools import reduce


def processScanners(file):
    scanners = []
    line = ""
    while len(scanners) == 0 or len(beacons) > 0:
        beacons = processBeacons(file)
        if len(beacons) > 0:
            scanners.append(beacons)
    return scanners


def processBeacons(file):
    file.readline()
    line = file.readline().rstrip()
    beacons = []
    while line != "":
        coords = line.split(",")
        beacons.append((int(coords[0]), int(coords[1]), int(coords[2])))
        line = file.readline().rstrip()
    return beacons


def orientations(beacon):
    (a, b, c) = beacon
    yield from [
        (+a, +b, +c),
        (+a, +c, -b),
        (+a, -b, -c),
        (+a, -c, +b),
        (+b, +a, -c),
        (+b, +c, +a),
        (+b, -a, +c),
        (+b, -c, -a),
        (+c, +a, +b),
        (+c, +b, -a),
        (+c, -a, -b),
        (+c, -b, +a),
        (-a, +b, -c),
        (-a, +c, +b),
        (-a, -b, +c),
        (-a, -c, -b),
        (-b, +a, +c),
        (-b, +c, -a),
        (-b, -a, -c),
        (-b, -c, +a),
        (-c, +a, -b),
        (-c, +b, +a),
        (-c, -a, +b),
        (-c, -b, -a),
    ]


def getDifference(beaconOne, beaconTwo):
    return tuple(map(lambda i, j: i - j, beaconTwo, beaconOne))

def findCommonBeacons(firstScanner, secondScanner):
    foundBeacons = 0
    for
    for x in range(len(firstScanner)):
        for y in range(len(secondScanner)):



def main(fileName):
    file = open(fileName, "r")

    scanners = processScanners(file)


if __name__ == "__main__":
    main(sys.argv[1])
