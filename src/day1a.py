import os
with open("input/day1.txt","r") as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]
lines = [(l[:1] == 'R', int(l[1:])) for l in lines]

dial = 50
zeroes = 0

for (d, clicks) in lines:
    if d:
        dial = (dial + clicks) % 100
    else:
        dial = (dial - clicks) % 100
    if dial == 0:
        zeroes += 1
print(zeroes)