import os
import pulp

with open("input/day10.txt", "r") as f:
    lines = f.readlines()

machines = []
for line in lines:
    lights_index = line.find("]")
    joltage_index = line.find("{")
    line = line.strip()
    machine = [line[1:lights_index], line[lights_index+1:joltage_index].strip(), line[joltage_index+1:-1]]
    machine[2] = list(map(int, machine[2].split(",")))
    machine[1] = [list(map(int, x[1:-1].split(","))) for x in machine[1].split(" ")]
    machines.append(machine)


total_presses = []

for _, buttons, target_joltage in machines:
    problem = pulp.LpProblem("Pressing Joltage", pulp.LpMinimize)
    # Decision variables
    button_variables = []
    for i, button in enumerate(buttons):
        button_variable = pulp.LpVariable(f"button{i}", lowBound = 0, cat="Integer")
        button_variables.append(button_variable)
            
    # Objective
    problem += sum(button_variables)
    
    # Constraints
    # for each joltage value, the joltage is the sum of the variables that affect that joltage level
    for i, joltage in enumerate(target_joltage):
        affecting_buttons = []
        for b, button in enumerate(buttons):
            if i in button:
                affecting_buttons.append(button_variables[b])
        # add the sum as a constraint
        problem += sum(affecting_buttons) == joltage
    
    # Solve
    problem.solve()
    total_presses.append(pulp.value(problem.objective))

print(sum(total_presses))