import random

from bag.constants import getTabuMemory, getTabuMemory2
from bag.data import TABU1_GENERATIONS, withTabu, PROB_TABU1_GENERATIONS

tabuGeneration = []


def setTabu(individual):
    tabu1(individual)


def setTabu1(individual):
    getTabuMemory().append([individual, TABU1_GENERATIONS])
    found = False
    for ind in getTabuMemory2():
        if individual in ind:
            ind[1] += TABU1_GENERATIONS
            found = True
    if not found:
        getTabuMemory2().append([individual, TABU1_GENERATIONS])



def tabu1(individual):
    if random.randint(0,100) < PROB_TABU1_GENERATIONS:
        found = False
        remove = False
        elementToDelete = []
        for ind in getTabuMemory():
            if individual in ind and ind[1] > 0:
                found = True
                break
            elif individual in ind and ind[1] <= 0:
                remove = True
                elementToDelete = ind.copy()
        if remove:
            getTabuMemory().remove(elementToDelete)
        if not found:
            setTabu1(individual)


def checkTabu(individual):
    found = False
    if withTabu:
        for ind in getTabuMemory():
            if individual in ind:
                if ind[1] > 0:
                    ind[1] -= 1
                    found = True
                    break
    return found
