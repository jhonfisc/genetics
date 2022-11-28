from bag.data import TABU1_GENERATIONS, withTabu

tabuMemory = []
tabuGeneration = []


def setTabu(individual):
    tabu1(individual)


def setTabu1(individual):
    global tabuMemory, tabuGeneration
    tabuMemory.append([individual, TABU1_GENERATIONS])


def tabu1(individual):
    found = False
    for ind in tabuMemory:
        if individual in ind:
            found = True
            break
    if not found:
        setTabu1(individual)


def checkTabu(individual):
    found = False
    if withTabu:
        for ind in tabuMemory:
            if individual in ind:
                if ind[1] > 0:
                    ind[1] -= 1
                    found = True
                    break
    return found
