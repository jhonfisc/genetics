from bag.data import incumbent
from useCases.checkRestriction import checkRestriction
from useCases.haveEsquema import haveEsquema


def getIncumbents(population, final):
    incumbents = []
    numEsquemas = 0
    for individual in population:
        if checkRestriction(individual, incumbent):
            incumbents.append(individual)
        numEsquemas += 1 if haveEsquema(individual) else 0
    if final == 1:
        incumbents.sort(reverse=True)
        incumbents = incumbents[:1]
    return [incumbents, numEsquemas]
