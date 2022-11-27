import random

from bag.data import bag, maxActives
from useCases.checkRestriction import checkRestriction


def createInitialPopulation():
    return [generateIndividuals() for i in range(int(getPs()))]


def getPs():
    return 40 #0.65 * (2 ** (0.2*len(bag)))


def generateIndividuals(tries=0):
    if tries == 10:
        return [0 for i in range(len(bag))]
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
        generateIndividuals(tries + 1)
