# Code for the 4th day of adventofcode.com
# By Laura (Pre1ude0)

def getData():
    with open("input.txt", "r") as f:
        return f.read()

data = getData().split("\n\n")

coordinates = [coordinate.split("|") for coordinate in data[0].split("\n")]
pagesInline = data[1].replace("\n", "").split(",")
pages = [line.split(",") for line in data[1].split("\n")]


def part1():

    middlePages = []

    for page in pages:
        flag = True
        for p in page:
            if not flag:
                break
            for coordinate in coordinates:
                if p == coordinate[1]:
                    if coordinate[0] in page and page.index(p) < page.index(coordinate[0]):
                        flag = False
                        break
        if flag:
            middlePages.append(page[len(page) // 2])

    middlePages.remove("")
    return [int(x) for x in middlePages]

def part2():

    middlePages = 0

    for page in pages:
        copy = page.copy()
        for p in page:
            for rule in coordinates:
                if rule[0] == p and rule[1] in page:
                    page_idx = copy.index(rule[0])
                    dep_idx = copy.index(rule[1])
                    if page_idx > dep_idx:
                        copy.pop(page_idx)
                        copy.insert(dep_idx, p)
        if page != copy:
            middlePages += int(copy[len(copy) // 2])

    return middlePages


print(sum(part1()))
print(part2())
