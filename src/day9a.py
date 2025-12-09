import os

with open("input/day9.txt", "r") as f:
    lines = f.readlines()
   
lines = [tuple(x.strip().split(",")) for x in lines]
points = [tuple(map(int, x)) for x in lines]

def rect(a, b):
    dx = abs(a[0] - b[0]) + 1
    dy = abs(a[1] - b[1]) + 1
    return dx * dy 

max_size = 0
for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        size = rect(points[i], points[j])
        print(points[i], points[j], size)
        if size > max_size:
            max_size = size
print(max_size)