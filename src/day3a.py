import os

with open("input/day3.txt","r") as f:
    batteries = f.readlines()

batteries = [b.strip() for b in batteries]

# find the largest number in the string of numbers s
# starting at index start and ending at index end (not included)
def find_heighest(s, start, end) -> int:
    # the maximum value and its index
    m = 0
    p = -1
    for i in range(start, end):
        x = int(s[i])
        if x > m:
            m = x
            p = i
    return m, p

count = 0
for b in batteries:
    # -1 necessary because we need to find a substring of length at least 2
    first_digit, first_index = find_heighest(b, 0, len(b) - 1)
    second_digit, second_index = find_heighest(b, first_index + 1, len(b))
    value = int(str(first_digit) + str(second_digit))
    count += value
print(count)
    
        
    