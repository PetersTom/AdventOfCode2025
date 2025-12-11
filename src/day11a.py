with open("input/day11.txt", "r") as f:
    lines = f.readlines()

nodes = {}
for line in lines:
    node, edges = line.split(":")
    edges = edges.strip().split(" ")
    nodes[node] = edges


incoming_edges = {}
for node, nbrs in nodes.items():
    for nbr in nbrs:
        if nbr not in incoming_edges:
            incoming_edges[nbr] = set()
        incoming_edges[nbr].add(node)
    if node not in incoming_edges:
        incoming_edges[node] = set()


# Topological sort
L = []  # empty list that will contain the sorted elements
S = {x for x in incoming_edges.keys() if len(incoming_edges[x]) == 0}

edges = {k: {x for x in v} for k, v in nodes.items()}
incoming_edges_copy = {k: {x for x in v} for k, v in incoming_edges.items()}

while len(S) > 0:
    n = S.pop()
    L.append(n)
    if n not in edges:
        continue
    for m in edges[n]:
        incoming_edges_copy[m].remove(n)
        if len(incoming_edges_copy[m]) == 0:
            S.add(m)

# L contains a topological order now
# loop over them in order and count the number of ways you can reach that state from "you"
def paths_from(x, y):
    reachable_ways = {}

    for node in L:
        if node == x:
            reachable_ways[node] = 1
        else:
            reachable_ways[node] = 0
        for pre in incoming_edges[node]:
            if pre in reachable_ways:
                reachable_ways[node] += reachable_ways[pre]

    return reachable_ways[y]

print(paths_from("you", "out"))


