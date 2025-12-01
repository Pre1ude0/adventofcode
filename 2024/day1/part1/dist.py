# Code for the 2nd day of adventofcode.com
# By Laura (Pre1ude0)

left = []
right = []
distance = 0

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        left.append(line.split()[0])
        right.append(line.split()[1])

left.sort()
right.sort()

for i in range(len(left)):
    distance += abs(int(left[i]) - int(right[i]))

print(distance)
