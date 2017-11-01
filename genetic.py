# intilatization


#init population
from operator import itemgetter

from evaluate import evaluate
from initPopulation import getPopulation
from mating import getOffspring

print("Creating inital population...")
population = getPopulation()
#print(population)
evaltuions = evaluate(population)
evaltuions = sorted(evaltuions, key=lambda student: student[1])
getOffspring(evaltuions[0][0],evaltuions[1][0])
#print(evaltuions)