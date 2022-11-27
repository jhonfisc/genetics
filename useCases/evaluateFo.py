from bag.data import sensitivityIndex


def evaluateFo(son, father1, father2):
    foSon = calculateFo(son)
    return foSon >= calculateFo(father1) and foSon >= calculateFo(father2)


def calculateFo(individual):
    idx = 0
    fo = 0
    while idx < len(individual):
        fo += sensitivityIndex[idx]["value"] if individual[idx] == 1 else 0
        idx += 1
    return fo
