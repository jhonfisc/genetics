# This is a sample Python script.
from bag.data import bag, MAX_GENERATIONS
from useCases.calculateFo import calculateFo
from useCases.createInitialPopulation import createInitialPopulation, heuristicMethod
from useCases.getIncumbents import getIncumbents
from useCases.roulette import roulette
from useCases.selection import selection

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    population = createInitialPopulation()
    generations = 1
    while generations < MAX_GENERATIONS:
        population = selection(population)
        generations += 1
        #sacar incumbente de la generacion
        print("Generation No: " + str(generations) + " Poblacion: " + str(len(population)))
    print(len(population))
    incumbents = getIncumbents(population)
    print(*incumbents, sep="\n")
    incumbentsFo = []
    for it in incumbents:
        incumbentsFo.append(calculateFo(it))
    print(*incumbentsFo, sep="\n")
