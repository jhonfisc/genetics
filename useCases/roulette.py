import random

from bag.data import sensitivityIndex


def roulette(population, selecteds):
    total = [0 for i in range(len(population) - 1)]
    probAcummu = getProbsAccumu(population, total)
    randomValue = random.uniform(0, 1)
    individualSelected = 0
    for it in probAcummu:
        if randomValue - it < 0 and individualSelected not in selecteds:
           break
        individualSelected += 1
    selecteds.append(individualSelected)
    return population[individualSelected]


def getAccumulate(population, total):
    index = 0
    for individual in population:
        indexIndividual = 0
        for it in individual:
            if index < len(total) and it != 0:
                total[index] += sensitivityIndex[indexIndividual]["value"]
            indexIndividual += 1
        index += 1
    return sum(total)


def getProbsAccumu(population, total):
    probs = calculatePorbs(population, total)
    probAcummu = [0.0 for i in range(len(probs))]
    idx = 0
    while idx < len(probs):
        if idx == 0:
            probAcummu[idx] = probs[idx]
        else:
            probAcummu[idx] = probs[idx] + probAcummu[idx - 1]
        idx += 1
    return probAcummu


def calculatePorbs(population, total):
    accumulate = getAccumulate(population, total)
    probs = [0.0 for i in range(len(total))]
    idx = 0
    while idx < len(total):
        probs[idx] = total[idx] / accumulate
        idx += 1
    return probs
