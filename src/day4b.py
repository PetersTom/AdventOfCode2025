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
    

def update_neighbors(surround_count, y, x):
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
            if surround_count[y + dy][x + dx] >= 0:
                surround_count[y + dy][x + dx] -= 1
 

# create the grid
surround_count = []
for y in range(0, len(grid)):
    surround_count.append([])
    for x in range(0, len(grid[y])):
        if grid[y][x] == ".":
            surround_count[y].append(-1)
        else:
            surround_count[y].append(adjacent(grid, y, x))


removed_blocks_total = 0
# do-while loop check at least once
while True:
    removed_blocks_this_round = 0
    # check all positions if they are less than 4
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            # if there is a block that can be removed, remove it and update all its neighbors
            if surround_count[y][x] < 4 and surround_count[y][x] >= 0:
                removed_blocks_this_round += 1
                surround_count[y][x] = -1
                
                update_neighbors(surround_count, y, x)
    
    removed_blocks_total += removed_blocks_this_round
    if removed_blocks_this_round == 0:
        break
print(removed_blocks_total)