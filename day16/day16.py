import heapq
import sys
from collections import defaultdict
from functools import reduce


class Packet:
    def __init__(self, version, typeID, length):
        self.version = version
        self.type = typeID
        self.length = length

    def getVersionSum(self):
        return self.version

    def getValue(self):
        return 0

    def __str__(self):
        return "Must be implemented!"


class Operator(Packet):
    def __init__(self, version, typeID, length, lengthType, subPackets):
        Packet.__init__(self, version, typeID, length)
        self.lengthType = lengthType
        self.subPackets = subPackets

    def getVersionSum(self):
        vSum = self.version
        for sub in self.subPackets:
            vSum += sub.getVersionSum()
        return vSum

    def getValue(self):
        value = 0
        if self.type == 0:
            for sub in self.subPackets:
                value += sub.getValue()
        elif self.type == 1:
            value = 1
            for sub in self.subPackets:
                value *= sub.getValue()
        elif self.type == 2:
            value = 99999999999
            for sub in self.subPackets:
                val = sub.getValue()
                if val < value:
                    value = val
        elif self.type == 3:
            for sub in self.subPackets:
                val = sub.getValue()
                if val > value:
                    value = val
        elif self.type == 5:
            if self.subPackets[0].getValue() > self.subPackets[1].getValue():
                value = 1
            else:
                value = 0
        elif self.type == 6:
            if self.subPackets[0].getValue() < self.subPackets[1].getValue():
                value = 1
            else:
                value = 0
        elif self.type == 7:
            if self.subPackets[0].getValue() == self.subPackets[1].getValue():
                value = 1
            else:
                value = 0
        return value

    def __str__(self):
        retStr = "Operator( "
        for subPack in self.subPackets:
            retStr += str(subPack)
        retStr += ")"
        return retStr

    __repr__ = __str__


class Literal(Packet):
    def __init__(self, version, typeID, length, value):
        Packet.__init__(self, version, typeID, length)
        self.value = value

    def getValue(self):
        return self.value

    def __str__(self):
        return "Lit " + str(self.value) + " "

    __repr__ = __str__


def processOuterPackets(file):
    packets = []
    for line in file:
        packets.append(convertToBinary(line.rstrip()))
    return packets


def convertToBinary(hexString):
    binString = ""
    for x in hexString:
        binNum = bin(int(x, 16))[2:]
        while len(binNum) < 4:
            binNum = "0" + binNum
        binString += binNum
    return binString


def packetVersionSum(packet):
    packetLength = 6
    version = int(packet[0:3], 2)
    typeID = int(packet[3:6], 2)
    if typeID == 4:
        (length, value) = processLiteral(packet[6:])
        packetLength += length
        return Literal(version, 4, packetLength, value)
    else:
        lengthType = packet[6]
        if lengthType == "0":
            (length, subPackets) = processTotalLengthOperator(packet[7:])
        else:
            (length, subPackets) = processSubPacketNumberOperator(packet[7:])
        packetLength += length + 1
        return Operator(version, typeID, packetLength, lengthType, subPackets)


def processTotalLengthOperator(packetStr):
    totalLength = int(packetStr[:15], 2)
    subPacks = []
    readLength = 0
    curOffset = 15
    while readLength < totalLength:
        packet = packetVersionSum(packetStr[curOffset:])
        subPacks.append(packet)
        readLength += packet.length
        curOffset += packet.length
    return (curOffset, subPacks)


def processSubPacketNumberOperator(packetStr):
    numSubPackets = int(packetStr[:11], 2)
    subPacks = []
    curOffset = 11
    while numSubPackets > 0:
        packet = packetVersionSum(packetStr[curOffset:])
        subPacks.append(packet)
        curOffset += packet.length
        numSubPackets -= 1
    return (curOffset, subPacks)


def processLiteral(literalVal):
    curBits = literalVal[:5]
    literal = ""
    counter = 0
    while curBits[0] != "0":
        counter += 5
        literal += curBits[1:]
        curBits = literalVal[counter : counter + 5]
    literal += curBits[1:]
    return (counter + 5, int(literal, 2))


def processPacket(packet):
    packet = packetVersionSum(packet)
    print("Packet: " + str(packet))
    print("Version sum: " + str(packet.getVersionSum()))
    print("Packet value: " + str(packet.getValue()))


def main(fileName):
    file = open(fileName, "r")

    packets = processOuterPackets(file)

    for packet in packets:
        processPacket(packet)


if __name__ == "__main__":
    main(sys.argv[1])
