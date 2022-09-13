import random
from itertools import *
import numpy as np
from operator import attrgetter
from utils.correctUploadedFile import isCorrectUploadedFile


data = [[0, 43,56,3,6,34],
    [43,0,34,523,23, 53],
    [56,34,0,23,43,52],
    [3,523,23,0,34,3423],
    [6,23,43,34,0,23],
    [34,53,52,3423,23,0]]

def selRandom(individuals, k):
    return [random.choice(individuals) for i in range(k)]

def selTournament(individuals, k, tournsize, fit_attr="fitness"):
    chosen = []
    for i in range(k):
        aspirants = selRandom(individuals, tournsize)
        chosen.append(max(aspirants, key=attrgetter(fit_attr)))
    return chosen

class Individual:
    def __init__(self, ind, fitness):
        self.individual = ind
        self.fitness = fitness

def cx(child1, child2):

    if (len(child1) != len(child2)):
        raise ValueError('Не идентичные по размеру родители')

    s = random.randint(2, len(child1)-3)
    child1cp, child2cp = child1, child2
    ch1, ch2 = child1[:s], child2[:s]
    arr = []
    for i in range(0, s):
        arr.append(child1cp[i])
    for i in range(s, len(child1)):
        if (child2cp[i] not in ch1):
            ch1.append(child2cp[i])
        arr.append(child2cp[i])
    for i in child1cp:
        if (i not in arr):
            ch1.append(i)
    arr = []
    for i in range(0, s):
        arr.append(child2cp[i])
    for i in range(s, len(child2)):
        if (child1cp[i] not in ch2):
            ch2.append(child1cp[i])
        arr.append(child1cp[i])
    for i in child2cp:
        if (i not in arr):
            ch2.append(i)
    child1, child2 = ch1, ch2

    if (len(child1) != len(child2)):
        raise ValueError('Не идентичные по размеру потомки')

    return child1, child2

def mut(mutant):
    pos1 = 0
    pos2 = 0

    while (pos1 == pos2):
        pos1 = random.randint(0, len(mutant) - 1)
        pos2 = random.randint(0, len(mutant) - 1)
    mutant1 = mutant.copy()

    mutant1[pos1] = mutant[pos2]
    mutant1[pos2] = mutant[pos1]
    mutant = mutant1

    return mutant

def startGenAlg(data, citiesCount, npop=200, ngen=40000, cxpb=0.9, mutpb=0.2):
    arr = []
    for i in range(0, citiesCount):
        arr.append(i)
    population = []
    for i in range(npop):
        population.append(random.sample(arr, citiesCount))
    # вся популяция из объектов
    populationAll = []
    for i in population:
        fitness = 0
        for j in range(len(i)-1):
            fitness += data[i[j]][i[j+1]]
        fitness += data[i[-1]][i[0]]
        ind = Individual(i, fitness)
        populationAll.append(ind)


    populationAll.sort(key=lambda x: x.fitness)


    # Два случайных родителя
    k=0
    while (k != ngen):
        parents = selTournament(populationAll, k=2, tournsize=10)
        parentInd1 = parents[0].individual
        parentInd2 = parents[1].individual

        # скрестили родителей, получили детей
        if (random.randint(0, 100) / 100 < cxpb):
            child1, child2 = cx(parentInd1, parentInd2)
        else:
            child1, child2 = parentInd1, parentInd2

        # мутация детей
        if (random.randint(0, 100) / 100 < mutpb):
            mutChild1 = mut(child1)
        else:
            mutChild1 = child1
        if (random.randint(0, 100) / 100 < mutpb):
            mutChild2 = mut(child2)
        else:
            mutChild2 = child2


        # добавляем одного ребенка
        fitness = 0
        for j in range(len(mutChild1)-1):
            fitness += data[mutChild1[j]][mutChild1[j+1]]
        fitness += data[mutChild1[-1]][mutChild1[0]]
        ind = Individual(mutChild1, fitness)
        populationAll.append(ind)

        # и второго

        fitness = 0
        for j in range(len(mutChild2)-1):
            fitness += data[mutChild2[j]][mutChild2[j+1]]
        fitness += data[mutChild2[-1]][mutChild2[0]]
        ind = Individual(mutChild2, fitness)
        populationAll.append(ind)

        populationAll.sort(key=lambda x: x.fitness)
        populationAll = populationAll[:(len(populationAll)-2)]
        k += 1


    arr = populationAll[0].individual

    while arr[0] != 0:
        arr = np.roll(arr, 1)
    best_ind = arr
    print(best_ind)
    print(populationAll[0].fitness)

    return best_ind, populationAll[0].fitness



