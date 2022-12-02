import random

from bag.data import withTabu, TABU2, MATING_PROB, IS_GROW_RATE, KIL_TABU
from useCases.calculateFo import calculateFo
from useCases.cross import cross
from useCases.evaluateFo import evaluateFo
from useCases.haveEsquema import haveEsquema
from useCases.killTabu import killTabu
from useCases.mutation import mutation
from useCases.roulette import roulette
from useCases.setTabu import setTabu, checkTabu

numFathers = 0

def selection(population, avg=0):
    selecteds = []
    crosses = len(population) / 2
    newGeneration = []
    for idx in range(int(crosses)):
        if random.uniform(1, 100) < MATING_PROB:
            father1 = roulette(population, selecteds)
            father2 = roulette(population, selecteds)
            if father1 is not None and father2 is not None and areBrothers(father1, father2) and not checkTabu(father1) \
                    and not checkTabu(father2):
                sons = cross(father1, father2)
                if withTabu:
                    if random.randint(1, 100) < KIL_TABU:
                        killTabu(population, father1)
                    else:
                        setTabu(father1)
                    if random.randint(1, 100) < KIL_TABU:
                        killTabu(population, father2)
                    else:
                        setTabu(father2)
                mutatedSon = mutation(sons[0])
                mutatedSon2 = mutation(sons[1])
                if mutatedSon not in population and evaluateFo(mutatedSon, father1, father2) and \
                        haveEsquema(mutatedSon, 1) and (avg == 0 or calculateFo(mutatedSon) >= avg):
                    newGeneration.append(mutatedSon)
                    if not IS_GROW_RATE:
                        population.remove(father1)
                if mutatedSon2 not in population and evaluateFo(mutatedSon2, father1, father2) and \
                        haveEsquema(mutatedSon2, 1) and (avg == 0 or calculateFo(mutatedSon2) >= avg):
                    newGeneration.append(mutatedSon2)
                    if not IS_GROW_RATE:
                        population.remove(father2)
    population = population + newGeneration
    return population


def areBrothers(individual1, individual2):
    sum = 0
    for idx in range(len(individual1) - 1):
        sum += 1 if individual1[idx] != individual2[idx] else 0
    tabu = random.uniform(0, 100)
    return sum > 2 or (tabu <= TABU2 and withTabu)
