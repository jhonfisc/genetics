from bag.data import incumbent
from useCases.checkRestriction import checkRestriction


def getIncumbents(population, final):
    incumbents = []
    for individual in population:
        if checkRestriction(individual, incumbent):
            incumbents.append(individual)
    if final == 1:
        incumbents.sort(reverse=True)
        incumbents = incumbents[:1]
    print(len(incumbents))
    return incumbents
