# intilatization


#init population
from operator import itemgetter

from evaluate import evaluate
from initPopulation import getPopulation
from mating import getOffspring

print("Creating inital population...")
population = getPopulation()
#print(population)
iterations = 0
while (iterations < 500):
    evaltuions = evaluate(population)
    evaltuions = sorted(evaltuions, key=lambda evaluation: evaluation[1])
    #combines two trajctories
    newPopulation = []
    #selection - combines top five of population
    for i in range(0,5):
        for j in range(i,5):
            newPopulation.append(getOffspring(evaltuions[i][0],evaltuions[j][0],iterations))
    population = newPopulation
    iterations += 1
evaltuions = evaluate(population)
evaltuions = sorted(evaltuions, key=lambda evaluation: evaluation[1])
print(evaltuions[0])
    #print(evaltuions)
