from math import sqrt

cities = []
def addCity(x,y):
    cities.append((x,y))
addCity(60, 200)
addCity(180, 200)
addCity(80, 180)
addCity(140, 180)
addCity(20, 160)
addCity(100, 160)
addCity(200, 160)
addCity(140, 140)
addCity(40, 120)
addCity(100, 120)
addCity(180, 100)
addCity(60, 80)
addCity(120, 80)
addCity(180, 60)
addCity(20, 40)
addCity(100, 40)
addCity(200, 40)
addCity(20, 20)
addCity(60, 20)
addCity(160, 20)
print(len(cities))
def evalGenmoe(genom):
    distance = 0
    for i in range(2,len(genom)):

        xDistance = abs(cities[genom[i]][0] - cities[genom[i-1]][0])
        yDistance =  abs(cities[genom[i]][1] - cities[genom[i-1]][1])
        distance += sqrt((xDistance * xDistance) + (yDistance * yDistance));
    return distance

def evaluate(population):
    evals = []
    for individual in population:
        evals.append((individual, evalGenmoe(individual)))

    return evals
