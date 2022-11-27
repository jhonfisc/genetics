import random

from bag.data import whitTabu
from useCases.cross import cross
from useCases.evaluateFo import evaluateFo
from useCases.mutation import mutation
from useCases.roulette import roulette
from useCases.setTabu import setTabu


def selection(population):
    selecteds = []
    crosses = len(population) / 2
    newGeneration = []
    for idx in range(int(crosses)):
        father1 = roulette(population, selecteds)
        father2 = roulette(population, selecteds)
        if father1 is not None and father2 is not None and areBrothers(father1, father2):
            sons = cross(father1, father2)
            if whitTabu:
                setTabu(father1)
                setTabu(father2)
            mutatedSon = mutation(sons[0])
            mutatedSon2 = mutation(sons[1])
            if mutatedSon not in population and evaluateFo(mutatedSon, father1, father2):
                if mutatedSon not in population:
                    newGeneration.append(mutatedSon)
            if mutatedSon2 not in population and evaluateFo(mutatedSon2, father1, father2):
                if mutatedSon2 not in population:
                    newGeneration.append(mutatedSon2)
    population = population + newGeneration
    return population

def areBrothers(individual1, individual2):
    sum = 0
    for idx in range(len(individual1) - 1):
       sum += 1 if individual1[idx] != individual2[idx] else 0
    return sum > 2
