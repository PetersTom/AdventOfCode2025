import os
import matplotlib.pyplot as plt

with open("input/day9.txt", "r") as f:
    lines = f.readlines()
   
lines = [tuple(x.strip().split(",")) for x in lines]
points = [tuple(map(int, x)) for x in lines]

def rect(a, b):
    dx = abs(a[0] - b[0]) + 1
    dy = abs(a[1] - b[1]) + 1
    return dx * dy 

x, y = zip(*points)
plt.plot(x, y, marker='o')
plt.show()

# the points are in a rough circle with a split
# find the split
dx = [x[i+1] - x[i] for i in range(len(x) - 1)]
max_diff_index = dx.index(max(dx))

top_split = points[max_diff_index+1][1]
bottom_split = points[max_diff_index+2][1]

print(points[max_diff_index+1])
print(points[max_diff_index+2])

sorted_on_x = sorted(points, key=lambda p: p[0])

def red_point_inside(i, j):
    min_x = min(points[i][0], points[j][0])
    max_x = max(points[i][0], points[j][0])
    min_y = min(points[i][1], points[j][1])
    max_y = max(points[i][1], points[j][1])
    
    min_x_index = next((i for i, p in enumerate(sorted_on_x) if p[0] == min_x), None)
    max_x_index = next((len(sorted_on_x) - 1 - i for i, p in enumerate(reversed(sorted_on_x)) if p[0] == max_x), None)
    
    for k in range(min_x_index, max_x_index + 1):
        p = sorted_on_x[k]
        # x coordinate is in between for sure
        if p[1] > min_y and p[1] < max_y:
            return True
    return False

# check all rectangles, but only if they are both above or both below the split
max_size = 0
for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        if points[i][1] >= top_split and points[j][1] <= bottom_split:
            continue
        if points[i][1] <= bottom_split and points[j][1] >= top_split:
            continue
        # not a valid rect if there is another red point inside
        if red_point_inside(i, j):
            continue
        
        size = rect(points[i], points[j])
        if size > max_size:
            print(f"current max: {points[i]} {i}, {points[j]} {j}")
            max_size = size
           
print(max_size)