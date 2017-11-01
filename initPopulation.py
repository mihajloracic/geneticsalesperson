from random import uniform, randrange, shuffle

lowerBound = 0.0;
upperBound = 20.0;

genomLength = 20;

populationSize = 10;

def lowerBound():
    return lowerBound

def upperBond():
    return upperBound


#change here if needed for example for traelling salesman smarter random function is needed
def generateRandomGenom():
    genom = []
    for i in range(1,genomLength):
        genom.append(i)
    shuffle(genom)
    return genom

def getPopulation():
    population = []
    for i in range(1,populationSize):
        population.append(generateRandomGenom())
    return population;