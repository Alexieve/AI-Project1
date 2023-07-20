import random

def normalCase(n, m, w, v):
    # Generate random weights and values for the items
    weights = [random.randint(1, w) for _ in range(n)]
    values = [random.randint(1, v) for _ in range(n)]
    
    # Generate random constraints for the items
    constraints = [random.randint(1, m) for _ in range(n)]
    
    # Generate a random weight capacity for the knapsack
    W = random.randint(sum(weights)//2, sum(weights))
    
    return W, m, weights, values, constraints

def noSolution(n, m, w, v):
    # Generate random weights and values for the items
    weights = [random.randint(1, w) for _ in range(n)]
    values = [random.randint(1, v) for _ in range(n)]

    # Generate constraints that make it impossible to find a feasible solution
    constraints = [random.randint(2, m) for _ in range(n)]

    # Generate a random weight capacity for the knapsack
    W = random.randint(sum(weights) // 2, sum(weights))

    return W, m, weights, values, constraints

def emptyKnapsack(n, m, w, v):
    # Generate random weights and values for the items
    weights = [random.randint(1, w) for _ in range(n)]
    values = [random.randint(1, v) for _ in range(n)]

    # Generate random constraints for the items
    constraints = [random.randint(1, m) for _ in range(n)]

    # Generate a random weight capacity for the knapsack
    W = 0  # Empty knapsack
 
    return W, m, weights, values, constraints

def fullCapacityKnapsack(n, m, w, v):
    # Generate random weights and values for the items
    weight = random.randint(1, w)
    value = random.randint(1, v)
    weights = [weight] * n
    values = [value] * n

    # Generate random constraints for the items
    constraints = [random.randint(1, m) for _ in range(n)]

    # Generate a random weight capacity for the knapsack
    W = sum(weights)

    return W, m, weights, values, constraints
