import os
with open("input/day1.txt","r") as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]
lines = [(l[:1] == 'R', int(l[1:])) for l in lines]

dial = 50
zeroes = 0
for (d, clicks) in lines:
    print(dial, zeroes, d, clicks)
    if d:
        after = dial + clicks
        zeroes += after // 100
        dial = after % 100
    else:
        start_dial = dial
        dial -= clicks
        count = abs(dial // 100)
        dial = dial % 100
        # edge cases
        if dial == 0:
            count += 1
        if start_dial == 0:
            count -= 1
        zeroes += count
print(zeroes)