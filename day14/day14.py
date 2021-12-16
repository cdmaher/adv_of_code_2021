import heapq
import sys
from collections import defaultdict
from functools import reduce


TOTAL_STEPS = 40


def processTemplateAndRules(file):
    template = file.readline().rstrip()
    file.readline()
    line = file.readline().rstrip()
    rules = {}
    while line != "":
        splitLine = line.split(" -> ")
        rules[splitLine[0]] = splitLine[1]
        line = file.readline().rstrip()
    return (template, rules)


def runStep(template, rules):
    newTemp = ""
    for x in range(len(template) - 1):
        curPair = template[x : x + 2]
        newTemp += curPair[0] + rules[curPair]
    return newTemp + template[-1]


def runPairInsertionSteps(template, rules):
    for x in range(TOTAL_STEPS):
        template = runStep(template, rules)
    return template


def partTwoInsertionSteps(template, rules):
    pairDict = defaultdict(int)
    for x in range(len(template) - 1):
        curPair = template[x : x + 2]
        pairDict[curPair] += 1
    print(str(pairDict))
    for step in range(TOTAL_STEPS):
        pairDict = partTwoStep(pairDict, rules)
        print(str(pairDict))
    return pairDict


def partTwoStep(pairDict, rules):
    newPairDict = defaultdict(int)
    for key in pairDict:
        insertionChar = rules[key]
        newPairDict[key[0] + insertionChar] += pairDict[key]
        newPairDict[insertionChar + key[1]] += pairDict[key]
    return newPairDict


def countPartTwoAnswer(pairDict, origTemplate):
    letterCount = defaultdict(int)
    for key in pairDict:
        letterCount[key[0]] += pairDict[key]
    letterCount[origTemplate[-1]] += 1
    heap = []
    for key in letterCount:
        heap.append(letterCount[key])
    heap.sort()
    print(str(letterCount))
    print(str(heap))
    return heap[-1] - heap[0]


def partOneAnswer(template):
    letterCount = {}
    for x in range(len(template)):
        if template[x] in letterCount:
            letterCount[template[x]] += 1
        else:
            letterCount[template[x]] = 1
    heap = []
    for key in letterCount:
        heap.append(letterCount[key])
    heap.sort()
    print(str(letterCount))
    print(str(heap))
    return heap[-1] - heap[0]


def main(fileName):
    file = open(fileName, "r")

    (template, rules) = processTemplateAndRules(file)

    # PART ONE
    # template = runPairInsertionSteps(template, rules)
    # answer = partOneAnswer(template)
    # print("Part one answer: " + str(answer))

    # PART TWO
    pairDict = partTwoInsertionSteps(template, rules)
    answer = countPartTwoAnswer(pairDict, template)
    print("Part one answer: " + str(answer))


if __name__ == "__main__":
    main(sys.argv[1])
