# intilatization


#init population
from operator import itemgetter

from evaluate import evaluate
from initPopulation import getPopulation
from mating import getOffspring
from selection import selecNewGeneration

print("Creating inital population...")
population = getPopulation()
#print(population)
iterations = 0
while (iterations < 500):
    evaltuions = evaluate(population)
    evaltuions = sorted(evaltuions, key=lambda evaluation: evaluation[1])
    #selection - choce type in selectio.py
    population = selecNewGeneration(evaltuions,iterations)
    iterations += 1
evaltuions = evaluate(population)
evaltuions = sorted(evaltuions, key=lambda evaluation: evaluation[1])
print(evaltuions[0])
    #print(evaltuions)
