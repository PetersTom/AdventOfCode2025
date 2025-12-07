import os
import re

with open("input/day7.txt", "r") as f:
    lines = f.readlines()

start_beam = lines[0].find("S")

# count the number of ways in which a particle could reach this spot
beams = {0: {start_beam: 1}}
for i, line in enumerate(lines):
    if i == 0:
        continue
    else:
        beams[i] = {}
        for beam in beams[i-1]:
            # check if the beam propagates normally or splits
            if line[beam] == ".":
                # propagate
                # if there already was a beam, sum the total
                if beam in beams[i]:
                    beams[i][beam] += beams[i-1][beam]
                else:
                    beams[i][beam] = beams[i-1][beam]
            else:
                # split
                assert line[beam] == "^"
                if beam - 1 in beams[i]:
                    # the left already has a beam
                    beams[i][beam - 1] += beams[i-1][beam]
                else:
                    # the left did not have a beam yet
                    beams[i][beam - 1] = beams[i-1][beam]
                if beam + 1 in beams[i]:
                    # the right already has a beam
                    beams[i][beam + 1] += beams[i-1][beam]
                else:
                    # the right did not have a beam yet
                    beams[i][beam + 1] = beams[i-1][beam]       
    
print(sum(beams[len(lines) - 1].values()))