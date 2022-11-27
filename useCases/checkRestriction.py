from bag.data import bag, restriction


def checkRestriction(individual):
    idx = 0
    bulk = 0
    while idx < len(individual):
        bulk += bag[idx]["data"]["bulk"] if individual[idx] == 1 else 0
        idx += 1
    return bulk <= restriction