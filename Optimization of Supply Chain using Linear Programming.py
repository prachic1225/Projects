# Python Code Using PuLP
import pulp

# Create a linear programming problem (Minimization problem)
problem = pulp.LpProblem("Supply_Chain_Optimization", pulp.LpMinimize)

# Define the decision variables (amounts to be transported)
x11 = pulp.LpVariable('x11', lowBound=0, cat='Continuous')  # W1 to S1
x12 = pulp.LpVariable('x12', lowBound=0, cat='Continuous')  # W1 to S2
x13 = pulp.LpVariable('x13', lowBound=0, cat='Continuous')  # W1 to S3
x21 = pulp.LpVariable('x21', lowBound=0, cat='Continuous')  # W2 to S1
x22 = pulp.LpVariable('x22', lowBound=0, cat='Continuous')  # W2 to S2
x23 = pulp.LpVariable('x23', lowBound=0, cat='Continuous')  # W2 to S3  

# Objective function: Minimize total transportation cost
problem += 4 * x11 + 6 * x12 + 8 * x13 + 5 * x21 + 7 * x22 + 9 * x23, "Total_Transportation_Cost"

# Supply constraints (maximum supply at each warehouse)
problem += x11 + x12 + x13 <= 100, "Supply_W1"
problem += x21 + x22 + x23 <= 150, "Supply_W2"

# Demand constraints (meet demand at each store)
problem += x11 + x21 >= 80, "Demand_S1"
problem += x12 + x22 >= 120, "Demand_S2"
problem += x13 + x23 >= 150, "Demand_S3"

# Solve the problem
problem.solve()

# Print the results
print(f"Status: {pulp.LpStatus[problem.status]}")
print("Optimal Transportation amounts:")
print(f"From W1 to S1: {x11.varValue} units")
print(f"From W1 to S2: {x12.varValue} units")
print(f"From W1 to S3: {x13.varValue} units")
print(f"From W2 to S1: {x21.varValue} units")
print(f"From W2 to S2: {x22.varValue} units")
print(f"From W2 to S3: {x23.varValue} units")

# Total transportation cost
print(f"Total Transportation Cost: ${pulp.value(problem.objective)}")


# Python Code Using scipy.optimize.linprog
from scipy.optimize import linprog

# Coefficients for the objective function (cost coefficients)
c = [4, 6, 8, 5, 7, 9]

# Coefficients for the inequality constraints (supply constraints)
A = [
    [1, 1, 1, 0, 0, 0],  # W1 supply constraint
    [0, 0, 0, 1, 1, 1]   # W2 supply constraint
]

# Right-hand side values for the inequality constraints
b = [100, 150]

# Coefficients for the equality constraints (demand constraints)
A_eq = [
    [1, 0, 0, 1, 0, 0],  # S1 demand constraint
    [0, 1, 0, 0, 1, 0],  # S2 demand constraint
    [0, 0, 1, 0, 0, 1]   # S3 demand constraint
]

# Right-hand side values for the equality constraints
b_eq = [80, 120, 150]

# Bounds for the decision variables (non-negative)
x_bounds = [(0, None) for _ in range(6)]

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=x_bounds, method='simplex')

# Print the results
print(f"Status: {result.success}")
print("Optimal Transportation amounts:")
for i in range(6):
    print(f"Variable x{i+1}: {result.x[i]} units")

# Total transportation cost
print(f"Total Transportation Cost: ${result.fun}")









