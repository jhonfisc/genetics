# This is a sample Python script.
from bag.data import bag, MAX_GENERATIONS
from useCases.calculateFo import calculateFo, calculateBulk
from useCases.createInitialPopulation import createInitialPopulation, heuristicMethod
from useCases.getIncumbents import getIncumbents
from useCases.roulette import roulette
from useCases.selection import selection

# Press the green button in the gutter to run the script.


def incumbents(poblation, final=0):
    incumbents = getIncumbents(population, final)
    print(*incumbents, sep="\n")
    incumbentsFo = []
    for it in incumbents:
        incumbentsFo.append([calculateFo(it), calculateBulk(it)])
    print(*incumbentsFo, sep="\n")


if __name__ == '__main__':
    idx = 0
    fo = 0
    bulk = 0
    test = [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1]
    while idx < len(bag):
        if test[idx] == 1:
            fo += bag[idx]["data"]["cost"]
            bulk += bag[idx]["data"]["bulk"]
        idx += 1
    print(fo)
    print(bulk)
    population = createInitialPopulation()
    print(*population, sep="\n")
    generations = 1
    while generations < MAX_GENERATIONS:
        population = selection(population)
        generations += 1
        #sacar incumbente de la generacion
        print("Generation No: " + str(generations) + " Poblacion: " + str(len(population)))
        incumbents(population, 1)
    print(len(population))


