from useCases.calculateFo import calculateFo
from useCases.checkRestriction import checkRestriction


def evaluateFo(son, father1, father2):
    foSon = calculateFo(son)
    return foSon >= calculateFo(father1) and foSon >= calculateFo(father2) and checkRestriction(son)
