import os
import re

with open("input/day7.txt", "r") as f:
    lines = f.readlines()

start_beam = lines[0].find("S")

beams = {0: {start_beam}}
splits = 0
for i, line in enumerate(lines):
    if i == 0:
        continue
    else:
        beams[i] = set()
        for beam in beams[i-1]:
            # check if the beam propagates normally or splits
            if line[beam] == ".":
                # propagate
                beams[i].add(beam)
            else:
                # split
                assert line[beam] == "^"
                splits += 1
                beams[i].add(beam - 1)
                beams[i].add(beam + 1)

print(splits)