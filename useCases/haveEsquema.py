import random

from bag.data import ACCEPT_IF_HAVE_ESQUEMA


def haveEsquema(indivdual, prob=0):
    if prob == 0:
        return indivdual[10] == 1 and indivdual[11] == 1 and indivdual[12] == 1
    else:
        if random.randint(0, 11) < ACCEPT_IF_HAVE_ESQUEMA:
            return indivdual[10] == 1 and indivdual[11] == 1 and indivdual[12] == 1
        else:
            return True
