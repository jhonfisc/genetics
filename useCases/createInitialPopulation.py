import random

from bag.data import bag, maxActives, sensitivityIndex, initialPopulation
from useCases.checkRestriction import checkRestriction


def createInitialPopulation():
    return [generateIndividuals() for i in range(int(getPs()))]


def getPs():
    return initialPopulation #1.65 * (2 ** (0.2*len(bag)))


def generateIndividuals(tries=0, isHeuristic=False):
    if tries == 10:
        return [0 for i in range(len(bag))]
    if isHeuristic:
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
            generateIndividuals(tries + 1, isHeuristic)


def heuristicMethod():
    fo = []
    for it in sensitivityIndex:
        fo.append(it["value"])
    foCopy = fo.copy()
    foCopy.sort(reverse=True)
    candidate = foCopy[:int(len(fo) * maxActives * random.uniform(1, 2))]
    individual = [0 for i in range(len(sensitivityIndex))]
    for it in candidate:
        individual[fo.index(it)] = 1
    print(individual)
