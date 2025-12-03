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
    batteries_left_to_chose_after_this = 11 # 1 less than the number of batteries required
    value = ""
    previous_index = -1
    while batteries_left_to_chose_after_this >= 0:
        digit, index = find_heighest(b, previous_index + 1, len(b) - batteries_left_to_chose_after_this)
        batteries_left_to_chose_after_this -= 1
        previous_index = index
        value += str(digit)
    count += int(value)
        
print(count)
    
        
    