from bag.data import bag, restriction


def checkRestriction(individual, percent=1):
    idx = 0
    bulk = 0
    while idx < len(individual):
        bulk += bag[idx]["data"]["bulk"] if individual[idx] == 1 else 0
        idx += 1
    return (percent == 1 or bulk <= restriction) and (percent == 1 or bulk >= restriction * percent)
