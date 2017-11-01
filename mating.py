from random import randrange

from scipy.stats import randint

from initPopulation import upperBound


def getOffspring(genom1,genom2):
    startOfGenom = randrange(0,10)
    child = []
    print("genom 1",genom1)
    child = genom1[0:startOfGenom]
    for i in child:
        genom2.remove(i)
    print("child after first append" , child)
    print("genom 2",genom2)
    startOfGenom = randrange(0, 10)
    for i in genom2[0:startOfGenom]:
        child.append(i)
    print("offpring after second" , genom2)
    return child
