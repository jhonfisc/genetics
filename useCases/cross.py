import random


def cross(father1, father2):
    limit = len(father1)
    crossPoint = int(random.uniform(1, limit))
    idx = 0
    son1 = [0 for i in range(limit)]
    son2 = [0 for i in range(limit)]
    for i in range(limit - 1):
        son1[idx] = father1[idx] if idx < crossPoint else father2[idx]
        son2[idx] = father2[idx] if idx < crossPoint else father1[idx]
        idx += 1
    return [son1, son2]
