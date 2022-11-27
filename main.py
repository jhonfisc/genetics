# This is a sample Python script.
from bag.data import bag
from useCases.createInitialPopulation import createInitialPopulation
from useCases.roulette import roulette
from useCases.selection import selection

# Press the green button in the gutter to run the script.

MAX_GENERATIONS = 2

if __name__ == '__main__':
    population = createInitialPopulation()
    print(len(population))
    generations = 1
    while generations < MAX_GENERATIONS:
        population = selection(population)
        generations += 1
        print("Generation No: " + str(generations))
    print(len(population))
