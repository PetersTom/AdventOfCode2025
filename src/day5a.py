import os

with open("input/day5.txt", "r") as f:
    inp = f.read()
inp = inp.split("\n\n")
rules = inp[0].split("\n")
rules = [tuple(x.split("-")) for x in rules]
rules = [(int(a), int(b)) for (a, b) in rules]

ingredients = inp[1].split("\n")
print(ingredients)
ingredients = [int(a) for a in ingredients]


def in_range(valid_range, ingredient) -> bool:
    return ingredient >= valid_range[0] and ingredient <= valid_range[1]
    
    
count = 0
for ingredient in ingredients:
    for r in rules:
        if in_range(r, ingredient):
            print(f"{ingredient} in {r}")
            count += 1
            break
print(count)