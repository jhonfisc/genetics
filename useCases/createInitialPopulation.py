import random

from bag.data import bag


def createInitialPopulation():
    return [generateIndividuals() for i in range(int(getPs()))]


def getPs():
    return 1.65 * (2 ** (0.2*len(bag)))


def generateIndividuals():
    return [random.randint(0, 1) for i in range(len(bag))]
