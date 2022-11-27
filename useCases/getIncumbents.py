from bag.data import incumbent
from useCases.checkRestriction import checkRestriction


def getIncumbents(population):
    incumbents = []
    for individual in population:
        if checkRestriction(individual, incumbent):
            incumbents.append(individual)
    print(len(incumbents))
