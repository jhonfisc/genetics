# This is a sample Python script.
from bag.constants import getTabuMemory, init, getTabuMemory2
from bag.data import bag, MAX_GENERATIONS
from useCases.calculateFo import calculateFo, calculateBulk
from useCases.createInitialPopulation import createInitialPopulation, heuristicMethod
from useCases.getIncumbents import getIncumbents
from useCases.graphics import graphs
from useCases.selection import selection

# Press the green button in the gutter to run the script.
results = []


def incumbents(poblation, final=0, generation=0):
    global results
    result = getIncumbents(population, final)
    incumbents = result[0]
    incumbentsFo = []
    for it in incumbents:
        incumbentsFo.append([calculateFo(it), calculateBulk(it)])
    if generation > 0:
        results.append([generation, len(poblation), incumbentsFo, result])


if __name__ == '__main__':
    init()
    idx = 0
    fo = 0
    bulk = 0
    test = [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1]
    while idx < len(bag):
        if test[idx] == 1:
            fo += bag[idx]["data"]["cost"]
            bulk += bag[idx]["data"]["bulk"]
        idx += 1
    population = createInitialPopulation()
    generations = 1
    while generations < MAX_GENERATIONS:
        incumbents(population, 1, generations)
        pro = 0
        for it in results:
            pro += it[2][0][0]
        population = selection(population, 0) #pro/len(population))
        generations += 1
        #sacar incumbente de la generacion
        print("Generation No: " + str(generations) + " Poblacion: " + str(len(population)))

    result2 = []
    result3 = []
    for it in results:
        result2.append(it[2][0][0])
        result3.append(it[3][1])
    graphs(result2, 2)
    graphs(result3, 1)
    print(*result2, sep="\n")
    print("---------------------------")
    print(max(result2))
    print(*getTabuMemory2(), sep="\n")



