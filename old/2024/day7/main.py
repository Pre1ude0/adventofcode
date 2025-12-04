def getTests():
    with open("input.txt") as f:
        return f.readlines()

tests = getTests()
results = [test.split(":")[0] for test in tests]
tests = [test.split(":")[1] for test in tests]
tests = [tests.split() for tests in tests]
tests = [[int(number) for number in test] for test in tests]

operators = "+", "*"


def part1():

    validCodes = 0

    for y in range(len(tests)):

        operatorSequences = []

        for i in range(2 ** (len(tests[y])-1)):
            operatorSequences.append(format(i, "b").zfill(len(tests[y])))
            print(operatorSequences[i])

        for operatorSequence in operatorSequences:
            result = str(tests[y][0])

            for j in range(1, len(operatorSequence)-1):
                result += eval(result + operatorSequence[j] + str(tests[y][j]))


            print(result, results[y])
            if int(eval(result)) == int(results[y]):
                validCodes += 1
                break

    return validCodes

print(part1())
