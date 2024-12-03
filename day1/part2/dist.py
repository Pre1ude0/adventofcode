# Code for the 2nd day of adventofcode.com
# By Laura (Pre1ude0)

left = []
right = []

dist = 0

with open("input.txt", "r") as f:
    lines = f.readlines()
    left = [line.split()[0] for line in lines]
    right = [line.split()[1] for line in lines]

for i in range(len(left)):
    mult = 0
    for id in right:
        if id == left[i]:
            mult += 1

    dist += mult * int(left[i])

print(dist)
