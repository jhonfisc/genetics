from bag.data import ONLY_SON_BETTER_FATHERS
from useCases.calculateFo import calculateFo
from useCases.checkRestriction import checkRestriction


def evaluateFo(son, father1, father2):
    if ONLY_SON_BETTER_FATHERS:
        foSon = calculateFo(son)
        return checkRestriction(son, 0) and foSon >= calculateFo(father1) and foSon >= calculateFo(father2)
    else:
        return checkRestriction(son, 0)
