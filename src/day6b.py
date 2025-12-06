import os
import re

with open("input/day6.txt", "r") as f:
    lines = f.readlines()

lines = [re.sub(r'\n', '', l) for l in lines]

# this function finds the first index after i where every line has a space
# return the index after the line in case there is no next
def find_next_all_space(i, lines):
    for j in range(i, len(lines[0])):
        if all(l[j] == " " for l in lines):
            return j
    return len(lines[0])


def prod(s):
    total = 1
    for i in s:
        total *= i
    return total

total = 0

current_start = 0
current_end = find_next_all_space(0, lines)
while True:
    # find the numbers first
    this_sum = [l[current_start:current_end] for l in lines]
    operand = this_sum[-1].strip()
    numbers = this_sum[:-1]
    
    parsed_numbers = []
    # rotate all the numbers
    for i in range(len(this_sum[0])):
        current_number = int(''.join([s[i] for s in numbers]).strip())
        parsed_numbers.append(current_number)
    
    # perform the sum
    result = 0
    if operand == "*":
        result = prod(parsed_numbers)
    else:
        result = sum(parsed_numbers)
    total += result
    
    # update the boundary variables to get the next math problem
    current_start = current_end + 1
    current_end = find_next_all_space(current_start, lines)
    
    # stop if we would try to find the next math problem out of bounds
    if current_start > len(lines[0]):
        break

    
print(total)
