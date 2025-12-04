import os

with open("input/day4.txt","r") as f:
    grid = f.readlines()

grid = [list(l.strip()) for l in grid]

def adjacent(grid, y, x):
    surround_count = 0
    for (dy, dx) in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]:
        if y + dy < 0 or y + dy >= len(grid) or x + dx < 0 or x + dx >= len(grid[0]):
            continue
        if grid[y + dy][x + dx] == "@":
            surround_count += 1
    return surround_count       

for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        if grid[y][x] == ".":
            continue
        if adjacent(grid, y, x) < 4:
            print(y, x)
            count += 1
print(count)