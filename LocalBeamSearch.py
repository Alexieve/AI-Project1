import random
import heapq
import numpy

class localBeamSearch:

    def __init__(self, W, m, w, v, c) -> None:
        self.n = len(w)
        self.W = W
        self.m = m
        self.w = w
        self.v = v
        self.c = c
        
    def evaluate(self, state):
        totalW = 0
        totalV = 0
        classCount = 0

        for i in range(self.n):
            if (state >> i) & 1 == 1:
                totalW += self.w[i]
                if totalW > W:
                    return self.W - totalW
                
                totalV += self.v[i]
                classCount |= (1 << (self.c[i] - 1))
        
        if (classCount + 1) != (1 << self.m):
            return 0
        
        return totalV

    def generateState(self):
        state = 0
        for i in range(self.n):
            bit = random.randint(0, 1)
            state |= (bit << i) # Reverse bit
        return (self.evaluate(state), state)
    
    def generateSuccessors(self, prevState, h):
        for i in range(self.n):
            successor = prevState ^ (1 << i) # reverse bit
            value = self.evaluate(successor)
            heapq.heappush(h, (value * -1, successor))

    def solve(self, beamWidth):
        beamDepth = 100
        h = [self.generateState()]
        for _ in range(beamDepth):
            for k in range(beamWidth):
                self.generateSuccessors(h[k][1], h)
            
            bestSuccessors = [heapq.heappop(h) for _ in range(beamWidth)]
            h = bestSuccessors
        
        return h[0][0] * (-1), h[0][1]

    def checkConstraint(self):
        if W == 0 or len(numpy.unique(self.c)) != m:
            return True
        return False

if __name__ == "__main__":
    # N = 8
    # for i in range(N):
        i = 8
        with open(f"./Testcases/Input/input{i}.txt") as fi:
            lines = fi.readlines() 
            W = int(lines[0])
            m = int(lines[1])
            w = [int(l) for l in lines[2].strip().split(', ')]
            v = [int(l) for l in lines[3].strip().split(', ')]
            c = [int(l) for l in lines[4].strip().split(', ')]
        
        solution = (0, 0)
        knapSacks = localBeamSearch(W, m, w, v, c)
        if not knapSacks.checkConstraint():
            solution = localBeamSearch(W, m, w, v, c).solve(beamWidth=20)
            
        
        with open(f"./Testcases/Output/output{i}.txt", 'w') as fo:
            fo.write(f"{solution[0]}\n")
            sequence = '{0:b}'.format(solution[1])
            fo.write(f"{', '.join(sequence)}")
