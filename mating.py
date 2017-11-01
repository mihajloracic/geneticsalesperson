from random import randrange

from scipy.stats import randint

from initPopulation import upperBound

def getMutProb(asd):
    return -99.0/500.0 * asd + 100

def getOffspring(g1,g2,interation):
    genom1 = g1[:]
    genom2 = g2[:]
    startOfGenom = randrange(0,10)
    child = []
    child = genom1[0:startOfGenom]
    for i in child:
        genom2.remove(i)

    startOfGenom = randrange(0, 10)
    for i in genom2[0:startOfGenom]:
        child.append(i)
    for i in child:
        genom1.remove(i)
    for i in genom1:
        child.append(i)
    swap1 = randrange(0,len(child))
    swap2 = randrange(0,len(child))
    isMutation = randrange(0,1000)
    if(isMutation <getMutProb(interation)):
        glass = child[swap1]
        child[swap1] = child[swap2]
        child[swap2] = glass
    return child

    
