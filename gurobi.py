from cplex import Cplex

# Create a new model
model = Cplex()

# Set objective to maximize
model.objective.set_sense(model.objective.sense.maximize)

# Define variables
names = ["x", "y"]
objective = [2.0, 3.0]
lb = [0.0, 0.0]  # Lower bounds
ub = [cplex.infinity, cplex.infinity]  # Upper bounds
model.variables.add(obj=objective, lb=lb, ub=ub, names=names)

# Define constraints
constraints = [
    [["x", "y"], [1.0, 1.0]],  # x + y <= 4
    [["x", "y"], [1.0, -1.0]]  # x - y >= 1
]
rhs = [4.0, 1.0]
senses = ["L", "G"]  # 'L' for <=, 'G' for >=
model.linear_constraints.add(lin_expr=constraints, senses=senses, rhs=rhs)

# Optimize model
model.solve()

# Print results
solution = model.solution
print(f'x: {solution.get_values("x")}')
print(f'y: {solution.get_values("y")}')
print(f'Objective: {solution.get_objective_value()}')
