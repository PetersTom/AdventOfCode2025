import os
from math import sqrt, ceil

with open("input/day2.txt","r") as f:
    rules = f.read().split(",")
    
ranges = [r.split("-") for r in rules]
ranges = [(int(x), int(y)) for (x, y) in ranges]

def dividers(x) -> list[int]:
    if x == 1:
        return {}
    d = set()
    # only search for dividers up to the sqrt
    end = ceil(sqrt(x))
    # compensate for the fact that if the square root is an integer, we need to include that integer
    if end * end == x:
        end += 1
    for i in range(1, end):
        if x % i == 0:
            d.add(i)
            if i != 1:
                d.add(x // i)
    return d

def is_repeat(s, l) -> bool:
    if len(s) % l != 0:
        return False
    check = s[:l]
    i = 0
    while i < len(s):
        if s[i:i+l] != check:
            return False
        i += l
    return True

def is_invalid(i) -> bool:
    i = str(i)
    divid = dividers(len(i))
    for d in divid:
        if is_repeat(str(i), d):
            return True
    return False

count = 0
for r in ranges:
    for i in range(r[0], r[1]+1):
        if is_invalid(i):
            print(i)
            count += i

print(count)
