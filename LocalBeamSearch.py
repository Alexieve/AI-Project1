import random
import heapq
import numpy
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
    
def evaluate(data, state):
    totalW = 0
    totalV = 0
    classCount = set()

    for i in range(data.n):
        if (state >> i) & 1 == 1:
            totalW += data.w[i]
            if totalW > data.W:
                return 0
            
            totalV += data.v[i]
            classCount.add(data.c[i])
    
    if len(classCount) != data.m:
        return 0
    
    if totalV > data.res:
        data.res = totalV
        data.state = state

    return totalV

def generateState(data):
    state = 0
    for i in range(data.n):
        bit = random.randint(0, 1)
        if bit:
            state = (1 << i) | state
    return (-evaluate(data, state), state)

def generateSuccessors(data, parent, heap):
    for i in range(data.n):
        successor = (1 << i) ^ parent
        value = evaluate(data, successor)
        heapq.heappush(heap, (-value, successor))

def solve(data, beamWidth):
    beamDepth = 100
    heap = [generateState(data)]
    for _ in range(beamDepth):
        for i in range(beamWidth):
                generateSuccessors(data, heap[i][1], heap)
        
        tmp = [heapq.heappop(heap) for _ in range(beamWidth)]
        del heap
        heap = tmp
    
    if -heap[0][0] > data.res:
        data.res = -heap[0][0]
        data.state = heap[0][1]

def checkConstraint(data):
    if len(numpy.unique(data.c)) != data.m:
        return True
    return False

if __name__ == "__main__":
    #TLE on input9
    #TLE on input8 with beamWidth = 20
    N = 8
    for testID in range(N):
        with open(f"./Testcases/Input/input{testID}.txt") as fi:
            lines = fi.readlines() 
            W = int(lines[0])
            m = int(lines[1])
            w = [int(l) for l in lines[2].strip().split(', ')]
            v = [int(l) for l in lines[3].strip().split(', ')]
            c = [int(l) for l in lines[4].strip().split(', ')]
        
        data = knapSack(W, m, w, v, c)
        
        start = time.time()
        if not checkConstraint(data):
            maxIter = 3
            if testID > 7:
                maxIter = 1
            for iteration in range(maxIter):
                tmp = solve(data, beamWidth=20)
 
        end = time.time()
        duration = end - start
        print(f"Test {testID} " + "Elapsed time: {:.2f} seconds".format(duration))
            
        with open(f"./Testcases/Output/output{testID}.txt", 'w') as fo:
            fo.write(f"{data.res}\n")
            sequence = '{0:b}'.format(data.state)
            fo.write(f"{', '.join(sequence)}")