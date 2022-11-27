import random

from useCases.cross import cross
from useCases.evaluateFo import evaluateFo
from useCases.mutation import mutation
from useCases.roulette import roulette


def selection(population):
    selecteds = []
    crosses = len(population) / 2
    newGeneration = []
    for idx in range(int(crosses)):
        father1 = roulette(population, selecteds)
        father2 = roulette(population, selecteds)
        if father1 is not None and father2 is not None:
            son = cross(father1, father2)
            mutatedSon = mutation(son)
            if evaluateFo(mutatedSon, father1, father2):
                newGeneration.append(mutatedSon)
    population = population + newGeneration
    return population
