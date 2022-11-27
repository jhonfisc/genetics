import random


def mutation(individual):
    points = int(random.uniform(1, 5))
    indv = individual.copy()
    for i in range(points):
        idx = int(random.uniform(1, len(indv)) - 1)
        indv[idx] = 1 if indv[idx] == 0 else 0
    return indv
