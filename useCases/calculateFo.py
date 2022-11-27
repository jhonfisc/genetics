from bag.data import sensitivityIndex


def calculateFo(individual):
    idx = 0
    fo = 0
    while idx < len(individual):
        fo += sensitivityIndex[idx]["value"] if individual[idx] == 1 else 0
        idx += 1
    return fo