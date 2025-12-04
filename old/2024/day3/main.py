# Code for the 3nd day of adventofcode.com
# By Laura (Pre1ude0)

import re

def getData():
    with open("input.txt", "r") as f:
        return f.read()


def part1() -> int:
    d = getData() # all data in string format

    sums = re.findall(r"mul\(\d{1,3},\d{1,3}\)", d)

    for i in range(len(sums)):
        sums[i] = sums[i].replace("mul(", "").replace(")", "").split(",")
        sums[i] = [int(sums[i][0]), int(sums[i][1])]
        sums[i] = sums[i][0] * sums[i][1]

    return sum(sums)

def part2() -> int:
    d = getData() # all data in string format

    donts = re.findall(r"don't\(\).*?do\(\)", d, re.DOTALL)
    for dont in donts:
        d = d.replace(dont, "")

    # finalDont = re.findall(r"don't\(\).*", d, re.DOTALL)

    # if finalDont:
    #     d = d.replace(finalDont[0], "")

    sums = re.findall(r"mul\(\d{1,3},\d{1,3}\)", d)

    for i in range(len(sums)):
        sums[i] = sums[i].replace("mul(", "").replace(")", "").split(",")
        sums[i] = [int(sums[i][0]), int(sums[i][1])]
        sums[i] = sums[i][0] * sums[i][1]

    return sum(sums)


print(part2())
