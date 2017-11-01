from random import randrange

import math

from mating import getOffspring

# helps select element for roullete selection
def getSelected(population):
    maxRand = len(population) * (len(population) + 1) / 2
    rand = randrange(1, maxRand)
    a = 1
    b = 1
    c = -2 * rand
    retVal = len(population) - math.ceil((-b + math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a))
    #print(len(population), " ", maxRand, " ", rand,retVal)
    return population[retVal][0]

def selectNewGenerationRoulette(evaltuions,iterations):
    newPopulation = []
    getSelected(evaltuions)
    for i in range(0,150):
            newPopulation.append(getOffspring(getSelected(evaltuions),getSelected(evaltuions),iterations))
    return newPopulation

def selecNewGeneration(evaltuions,iterations):
    return selectNewGenerationRoulette(evaltuions,iterations)