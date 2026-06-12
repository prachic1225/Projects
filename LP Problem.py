import pandas as pd
from pulp import *

# Warehouses and Stores
warehouses = ["W1", "W2"]
stores = ["S1", "S2", "S3"]

# Supply and Demand
supply = {"W1": 100, "W2": 150}
demand = {"S1": 80, "S2": 120, "S3": 50}

# Cost matrix
costs = {
    ("W1", "S1"): 2, ("W1", "S2"): 4, ("W1", "S3"): 5,
    ("W2", "S1"): 3, ("W2", "S2"): 1, ("W2", "S3"): 7
}

# Create LP problem
model = LpProblem("Supply_Chain_Optimization", LpMinimize)

# Decision variables
x = LpVariable.dicts("ship",
                     [(w, s) for w in warehouses for s in stores],
                     lowBound=0,
                     cat='Continuous')

# Objective function
model += lpSum(costs[(w, s)] * x[(w, s)] for w in warehouses for s in stores)

# Supply constraints
for w in warehouses:
    model += lpSum(x[(w, s)] for s in stores) <= supply[w]

# Demand constraints
for s in stores:
    model += lpSum(x[(w, s)] for w in warehouses) == demand[s]

# Solve
model.solve()

# Results
print("Status:", LpStatus[model.status])
for v in model.variables():
    print(v.name, "=", v.varValue)

print("Total Cost =", value(model.objective))
