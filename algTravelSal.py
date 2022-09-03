
import random
import json
import matplotlib.pyplot as plt
import numpy as np

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

# gr*.json contains the distance map in list of list style in JSON format
# Optimal solutions are : gr17 = 2085, gr24 = 1272, gr120 = 6942
class GeneticsAlg:
    def __init__(self, countCity, cityDist):
        self.toolbox = base.Toolbox()

        class Foo(list):
            spam = 1
            def __init__(self):
                self.bar = dict()

        IND_SIZE = countCity
        self.distance_map = cityDist

        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

    # Attribute generator
        self.toolbox.register("indices", random.sample, range(IND_SIZE), IND_SIZE)

    # Structure initializers
        self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.indices)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        self.toolbox.register("mate", tools.cxPartialyMatched)
        self.toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
        self.toolbox.register("select", tools.selTournament, tournsize=3)
        self.toolbox.register("evaluate", self.evalTSP)

    def evalTSP(self, individual):
        distance = self.distance_map[individual[-1]][individual[0]]
        for gene1, gene2 in zip(individual[0:-1], individual[1:]):
            distance += self.distance_map[gene1][gene2]
        return distance,

    def start(self):

        pop = self.toolbox.population(n=300)

        hof = tools.HallOfFame(1)
        algorithms.eaSimple(pop, self.toolbox, 0.7, 0.2, 100, halloffame=hof)

        arr = hof[0]

        while arr[0] != 0:
            arr = np.roll(arr, 1)
        best_ind = arr

        return best_ind