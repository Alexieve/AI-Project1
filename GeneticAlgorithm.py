import random
import heapq
import time

class knapSack:
    def __init__(self, W, m, w, v, c) -> None:
        self.n = len(w)
        self.W = W
        self.m = m
        self.w = w
        self.v = v
        self.c = c
        self.res = 0
        self.state = 0

def fitness(data, ind):
    totalV = 0
    totalW = 0
    classCount = set()
    for i in range(data.n):
        if (ind >> i) & 1 == 1:
            totalW += data.w[i]
            if totalW > data.W:
                return 0
            totalV += data.v[i]
            classCount.add(data.c[i])

    if len(classCount) != data.m:
        return 0

    if totalV > data.res:
        data.res = totalV
        data.state = ind

    return totalV

def selection(data, fitnesses):
    choices = random.sample(range(len(data.population)), 4)
    parent1 = 0
    maxFitness = -1
    for i in choices[:2]:
        if fitnesses[i] > maxFitness:
            parent1 = i
            maxFitness = fitnesses[i]

    parent2 = 0
    maxFitness = -1
    for i in choices[2:]:
        if fitnesses[i] > maxFitness:
            parent2 = i
            maxFitness = fitnesses[i]

    return data.population[parent1], data.population[parent2]

def bitExtracted(number, k):
    return ((1 << k) - 1) & number

def crossover(data, parent1, parent2):
    pos = random.randrange(data.n)
    p11 = bitExtracted(parent1, pos)
    p12 = parent1 >> pos
    p21 = bitExtracted(parent2, pos)
    p22 = parent2 >> pos
    offspring1 = p11 | (p22 << pos)
    offspring2 = p21 | (p12 << pos)
    return offspring1, offspring2

def mutate(data, ind):
    pos = random.randrange(0, data.n)
    return (1 << pos) ^ ind

def solve(data, maxGen, populationSize, mutationRate):
    population = [random.getrandbits(data.n) for _ in range(populationSize)]
    for _ in range(maxGen):
        fitnesses = []
        for ind in population:
            fitnesses.append((-fitness(data, ind), ind))
        newPopulation = []

        for _ in range(0, populationSize, 2):
            parent1 = heapq.heappop(fitnesses)[1]
            parent2 = heapq.heappop(fitnesses)[1]
            offspring1, offspring2 = crossover(data, parent1, parent2)

            if random.random() < mutationRate:
                offspring1 = mutate(data, offspring1)
            if random.random() < mutationRate:
                offspring2 = mutate(data, offspring2)

            newPopulation.append(offspring1)
            newPopulation.append(offspring2)

        del population
        population = newPopulation

    _ = [fitness(data, ind) for ind in population]

if __name__ == "__main__":
    N = 10
    for testID in range(N):
        with open(f"./Testcases/Input/input{testID}.txt") as fi:
            lines = fi.readlines()
            W = int(lines[0])
            m = int(lines[1])
            w = [int(l) for l in lines[2].strip().split(', ')]
            v = [int(l) for l in lines[3].strip().split(', ')]
            c = [int(l) for l in lines[4].strip().split(', ')]

        data = knapSack(W, m, w, v, c)
        res = 0
        state = 0
        maxIter = 5
        start = time.time()
        for _ in range(maxIter):
            solve(data, maxGen=200, populationSize=500, mutationRate=0.1)
            if data.res > res:
                res = data.res
                state = data.state
        end = time.time()
        duration = end - start
        print(f"Test {testID} " + "Elapsed time: {:.2f} seconds".format(duration))

        with open(f"./Testcases/Output/output{testID}.txt", 'w') as fo:
            fo.write(f"{res}\n")
            sequence = '{0:b}'.format(state)
            fo.write(f"{', '.join(sequence)}")
