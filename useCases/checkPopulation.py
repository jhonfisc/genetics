from useCases.calculateFo import calculateFo


def checkPopulation(population):
    for it in population:
        calculateFo(it)