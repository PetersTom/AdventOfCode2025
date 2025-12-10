import os
from collections import deque

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


def press(button, start) -> str:
    new_str = ""
    for i, s in enumerate(start):
        if i in button:
            if s == ".":
                new_str += "#"
            if s == "#":
                new_str += "."
        else:
            new_str += s
    return new_str
    
def nbrs(lights, buttons) -> [str]:
    nbrs = []
    for button in buttons:
        nbrs.append(press(button, lights))
    return nbrs


total_pressed = 0

for target_lights, buttons, _ in machines:
    # perform bfs on the lights as vertices, buttons as edges
    start = "." * len(target_lights)
    visited = set()
    steps_necessary = {start: 0}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        
        for nbr in nbrs(node, buttons):
            updated_steps = steps_necessary[node] + 1
            if nbr not in steps_necessary or steps_necessary[nbr] > updated_steps:
                steps_necessary[nbr] = steps_necessary[node] + 1
            queue.append(nbr)
    
    total_pressed += steps_necessary[target_lights]
    
print(total_pressed)