import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt

from bag.data import MAX_GENERATIONS


def graphs(list, i):
    if i == 1:
        graphEsquemas(list, i)
    elif i == 2:
        graphIncumbents(list, i)


def graphEsquemas(list, i):
    plt.figure(i)
    plt.plot(np.arange(MAX_GENERATIONS - 1), np.array(list))
    plt.xlabel("Esquemas")
    plt.ylabel("Generation")
    plt.show()


def graphIncumbents(list, i):
    plt.figure(i)
    plt.plot(np.arange(MAX_GENERATIONS - 1), np.array(list))
    plt.xlabel("Best F.O.")
    plt.ylabel("Generations")
    plt.show()