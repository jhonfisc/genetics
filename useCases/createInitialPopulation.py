import random

from bag.data import bag, maxActives, sensitivityIndex, initialPopulation, ESQUEMA_LEFT, ESQUEMA_RIGHT
from useCases.checkRestriction import checkRestriction

heuCant = 0
def createInitialPopulation():
    return [generateIndividuals() for i in range(int(getPs()))]


def getPs():
    return initialPopulation #1.65 * (2 ** (0.2*len(bag)))


def generateIndividuals(tries=0, isHeuristic=False):
    global heuCant
    generateMethod = 1 if isHeuristic else 0
    if tries == 0 and heuCant < int(len(bag) * maxActives):
        generateMethod = 1
        heuCant += 1
    if tries == 10:
        return [0 for i in range(len(bag))]
    if generateMethod == 1:
        individual = heuristicMethod()
        if checkRestriction(individual):
            return individual
        else:
            generateIndividuals(tries + 1, isHeuristic)
    else:
        individual = [0 for i in range(len(bag))]
        max = int(len(bag) * maxActives)
        numActives = 0
        while numActives < max:
            idxRandom = random.randint(0, len(individual) - 1)
            individual[idxRandom] = 1
            numActives += 1
        if checkRestriction(individual):
            return individual
        else:
            generateIndividuals(tries + 1, generateMethod == 1)


def heuristicMethod():
    fo = []
    for it in sensitivityIndex:
        fo.append(it["value"])
    foCopy = fo.copy()
    foCopy.sort(reverse=True)
    candidate = foCopy[0]
    individual = [0 for i in range(len(sensitivityIndex))]
    idx = fo.index(candidate)
    if 0 < idx < len(fo):
        for i in range(ESQUEMA_LEFT + 1):
            if (idx + i) < len(fo):
                individual[idx + i] = 1
    if 0 < idx < len(fo):
        for i in range(ESQUEMA_RIGHT + 1):
            if (idx - i) > 0:
                individual[idx - i] = 1
    max = int(len(bag) * maxActives)
    numActives = ESQUEMA_LEFT + ESQUEMA_RIGHT
    while numActives < max:
        idxRandom = random.randint(0, len(individual) - 1)
        individual[idxRandom] = 1
        numActives += 1
    return individual
