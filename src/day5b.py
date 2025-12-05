import os

with open("input/day5.txt", "r") as f:
    inp = f.read()
inp = inp.split("\n\n")
rules = inp[0].split("\n")
rules = [tuple(x.split("-")) for x in rules]
rules = [(int(a), int(b)) for (a, b) in rules]

rules.sort()

new_rules = []
# merge all rules if they overlap
current_min = -1
current_max = -1
for r in rules:
    # if the next start is after our last end, we start a new one
    if r[0] > current_max:
        new_rules.append((current_min, current_max))
        current_min = r[0]
        current_max = r[1]
    else:
        # we need to merge
        assert current_min <= r[0]
        current_max = max(current_max, r[1])
# add the last interval and delete the -1, -1
new_rules.append((current_min, current_max))
new_rules = new_rules[1:]

# count the fresh ingredients
count = 0
for r in new_rules:
    count += r[1] - r[0] + 1  # +1 because the ranges are inclusive
print(count)