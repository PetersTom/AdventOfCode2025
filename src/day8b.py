import os
import itertools
from math import sqrt

with open("input/day8.txt", "r") as f:
    lines = f.readlines()
    
points = [l.strip().split(",") for l in lines]
points = [tuple(map(int, x)) for x in points]

def dist(i, j, points):
    p1 = points[i]
    p2 = points[j]
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    return sqrt(dx*dx + dy*dy + dz*dz)

edges = [(x, dist(x[0], x[1], points)) for x in itertools.combinations(range(len(points)), 2)]
sorted_edges = sorted(edges, key=lambda x: x[1]) # sort the edges on the distance

def find_set_containing(i, sets):
    for j, s in enumerate(sets):
        if i in s:
            return j

circuits = [{i} for i in range(len(points))]
last_connection = (-1, -1)
i = 0
while len(circuits) > 1:
    # take the ith smallest edge and merge their circuits
    ((p1, p2), weight) = sorted_edges[i]
    i += 1
    p1_set = find_set_containing(p1, circuits)
    p2_set = find_set_containing(p2, circuits)
    
    # no merging if they are already in the same set
    if p1_set == p2_set:
        continue
    
    # merge p1_set and p2_set
    circuits[p1_set].update(circuits[p2_set])
    # remove p2_set
    circuits.pop(p2_set)
    
    last_connection = (p1, p2)
    
result = points[last_connection[0]][0] * points[last_connection[1]][0]
print(result)