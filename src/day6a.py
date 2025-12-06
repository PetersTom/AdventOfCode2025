import os

with open("input/day6.txt", "r") as f:
    lines = f.readlines()

lines = [[x.strip() for x in l.split(" ") if len(x.strip()) > 0] for l in lines]
numbers = [[int(x) for x in l] for l in lines[:-1]]
operators = lines[-1]

print(numbers)

def prod(i, s):
    total = 1
    for x in s:
        total = total * x[i]
    return total
    
def sum(i, s):
    total = 0
    for x in s:
        total = total + x[i]
    return total

number_of_sums = len(lines[0])
total = 0
for i in range(number_of_sums):
    if operators[i] == "+":
        result = sum(i, numbers)
    else:
        result = prod(i, numbers)
    total += result
    
print(total)