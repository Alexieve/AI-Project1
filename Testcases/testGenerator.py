from testcasesFunction import *
import random


def write(testcase, filename):
    W, m, weights, values, constraints = testcase
    with open(filename, 'w') as file:
        file.write(f"{W}\n")
        file.write(f"{m}\n")
        file.write(", ".join(str(i) for i in weights) + "\n")
        file.write(", ".join(str(i) for i in values) + "\n")
        file.write(", ".join(str(i) for i in constraints))

def main():
    numItems = 200
    numConstraints = 5
    weightRange = 50
    valueRange = 50
    i = 7

    testcase = normalCase(numItems, numConstraints, weightRange, valueRange)
    filename = f"./Testcases/Input/input{i}.txt"
    write(testcase, filename)
    print("Testcase generated!")

if __name__ == "__main__":
    main()
