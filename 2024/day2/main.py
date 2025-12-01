# Code for the 2nd day of adventofcode.com
# By Laura (Pre1ude0)

import math

def getReports() -> list[list[int]]:
    f = open("input.txt", "r")
    reports = f.readlines()
    f.close()

    reports = [[int(report) for report in report.split()] for report in reports]

    return reports


def part1() -> int:
    r = getReports()

    safeReports = 0

    for report in r:
        direction = None
        for i in range(len(report)):
            if i == 0:
                continue
            else:
                if report[i-1] == report[i]:
                    break

                if i == 1:
                    direction = "up" if report[i-1] < report[i] else "down"

                if abs(report[i-1] - report[i]) > 3:
                    break

                if direction == "up":
                    if report[i-1] > report[i]:
                        break
                elif direction == "down":
                    if report[i-1] < report[i]:
                        break

                if i == len(report) - 1:
                    safeReports += 1
                else:
                    report[i-1] = report[i]

    return safeReports

# def compareLevelValidity(lvl1, lvl2, direction):
#     if lvl1 == lvl2:
#         return False

#     if abs(lvl1 - lvl2) > 3:
#         return False

#     if direction == "up":
#         if lvl1 > lvl2:
#             return False
#     elif direction == "down":
#         if lvl1 < lvl2:
#             return False

#     return True

def validateReport(report):
    direction = math.copysign(1, report[1] - report[0])
    for i in range(len(report)-1):
        d = (report[i+1] - report[i]) * direction
        if d < 1 or d > 3:
            return False

    return True

def part2() -> int:
    r = getReports()

    safeReports = 0

    for report in r:
        if validateReport(report):
            safeReports += 1
        else:
            for i in range(len(report)):
                altReport = report.copy()
                del altReport[i]
                if validateReport(altReport):
                    safeReports += 1
                    break

    return safeReports

print(getReports())
print(part1())
print(part2())
