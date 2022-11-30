import random

from bag.data import MUTATION_POINTS


def mutation(individual):
    points = int(random.uniform(1, MUTATION_POINTS))
    indv = individual.copy()
    for i in range(points):
        idx = int(random.uniform(1, len(indv)))
        indv[idx] = 1 if indv[idx - 1] == 0 else 1
    return indv
