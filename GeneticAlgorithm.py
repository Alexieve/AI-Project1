import random

class geneticAlgorithm:
    populationSize = 500
    mutationRate = 0.1

    def __init__(self, W: int, m: int, w, v, c):
        self.n = len(w)
        self.W = W
        self.m = m
        self.w = w
        self.v = v
        self.c = c
        self.population = [random.getrandbits(
            self.n) for _ in range(geneticAlgorithm.populationSize)]
        self.bestChrom = 0
        self.bestV = 0

    def fitness(self, chromosome):
        totalV = 0
        totalW = 0
        classCount = set()
        for i in range(self.n):
            bit = (chromosome & (1 << i))
            if not bit:
                continue

            totalV += self.v[-1 - i]
            totalW += self.w[-1 - i]
            if totalW > self.W:
                return 0
            classCount.add(self.c[-1 - i])

        if len(classCount) != self.m:
            return 0

        if totalV > self.bestV:
            self.bestV = totalV
            self.bestChrom = chromosome

        return totalV

    def selection(self, fitnesses):
        choices = random.sample(range(len(self.population)), 4)
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

        return self.population[parent1], self.population[parent2]

    def crossover(self, parent1, parent2):
        c = random.randrange(self.n)
        offspring1 = (parent1 & ((1 << c) - 1)) + \
            (parent2 & (((1 << (self.n - c)) - 1) << c))
        offspring2 = (parent2 & ((1 << c) - 1)) + \
            (parent1 & (((1 << (self.n - c)) - 1) << c))
        return offspring1, offspring2

    def mutate(self, chromosome):
        c = random.randrange(0, self.n)
        return chromosome ^ (1 << c)

    def bitBest(self):
        _ = [self.fitness(chrom) for chrom in self.population]
        return self.bestV, self.bestChrom

    def solve(self, maxGen):
        for _ in range(maxGen):
            fitnesses = [self.fitness(chrom) for chrom in self.population]
            newPopulation = []

            newPopulation.append(self.bestChrom)

            for _ in range(0, geneticAlgorithm.populationSize, 2):
                parent1, parent2 = self.selection(fitnesses)
                offspring1, offspring2 = self.crossover(parent1, parent2)

                if random.random() < geneticAlgorithm.mutationRate:
                    offspring1 = self.mutate(offspring1)
                if random.random() < geneticAlgorithm.mutationRate:
                    offspring2 = self.mutate(offspring2)

                newPopulation.append(offspring1)
                newPopulation.append(offspring2)

            del self.population
            self.population = newPopulation

        solution = self.bitBest()
        state = ", ".join(bin(solution[1])[2:].rjust(self.n, '0'))
        return str(solution[0]), state


if __name__ == "__main__":
    # N = 10
    # for i in range(N):
        i = 8
        with open(f"./Testcases/Input/input{i}.txt") as fi:
            lines = fi.readlines()
            W = int(lines[0])
            m = int(lines[1])
            w = [int(l) for l in lines[2].strip().split(', ')]
            v = [int(l) for l in lines[3].strip().split(', ')]
            c = [int(l) for l in lines[4].strip().split(', ')]
        bestV = 0
        bestSolution = None
        maxIter = 1
        for _ in range(maxIter):
            gen = geneticAlgorithm(W, m, w, v, c)
            solution = gen.solve(maxGen=200)
            if int(solution[0]) > bestV:
                bestV = int(solution[0])
                bestSolution = solution

        with open(f"./Testcases/Output/output{i}.txt", 'w') as fo:
            res = bestSolution[0]
            state = bestSolution[1]
            fo.write(f"{bestSolution[0]}\n")
            fo.write(f"{bestSolution[1]}")
