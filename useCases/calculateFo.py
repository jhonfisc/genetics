from bag.data import sensitivityIndex, bag


def calculateFo(individual):
    idx = 0
    fo = 0
    while idx < len(individual):
        fo += bag[idx]["data"]["cost"] if individual[idx] == 1 else 0
        idx += 1
    return fo


def calculateBulk(individual):
    idx = 0
    fo = 0
    while idx < len(individual):
        fo += bag[idx]["data"]["bulk"] if individual[idx] == 1 else 0
        idx += 1
    return fo
