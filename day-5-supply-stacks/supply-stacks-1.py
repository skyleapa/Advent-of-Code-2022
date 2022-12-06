import re

f = open("input_michelle.txt", "r")

stackHolder = [[], [], [], [], [], [], [], [], []]

stopper = 0

def getElements(line):
    return [int(s) for s in re.findall(r'\b\d+\b', line)]

def stackMover(amount, startIndex, endIndex):
    for x in range(0, amount):
        

for line in f:
    # building stacks
    index = 0
    if stopper < 8:
        # by column
        for x in range(1, 37, 4):
            if (line[x] != ' '):
                stackHolder[index].append(line[x])
                index += 1
        stopper += 1
    # working with move to from instructions
    elif stopper == 10:
        elements = getElements(line)
        stackMover(elements[0], elements[1], elements[2])
    # so we can access the txt file after 2 lines
    else:
        stopper += 1

