import os
with open("input/day2.txt","r") as f:
    rules = f.read().split(",")
    
ranges = [r.split("-") for r in rules]
ranges = [(int(x), int(y)) for (x, y) in ranges]

def is_invalid(i) -> bool:
    i = str(i)
    if len(i) % 2 != 0:
        return False
    middle = len(i) // 2
    left, right = i[:middle], i[middle:]
    return left == right

count = 0
for r in ranges:
    for i in range(r[0], r[1]+1):
        if is_invalid(i):
            count += i
print(count)
    
