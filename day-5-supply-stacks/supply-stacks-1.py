import re

f = open("input_michelle.txt", "r")

stackHolder = [[], [], [], [], [], [], [], [], []]

stopper = 0

def getElements(line):
    return [int(s) for s in re.findall(r'\b\d+\b', line)]

# amount is 0 index
def stackMover(amount, startIndex, endIndex):
    for x in range(0, amount):
        # print(stackHolder[startIndex])
        # print(stackHolder[endIndex])
        # stackHolder[endIndex].insert(0, stackHolder[startIndex][0])
        # stackHolder[startIndex].pop(0)
        # print(stackHolder[startIndex])
        # print(stackHolder[endIndex])

        stackHolder[endIndex].insert(0, stackHolder[startIndex][0])
        stackHolder[startIndex].pop(0)

for line in f:
    # building stacks)
    index = 0
    if stopper < 8:
        # by column
        for x in range(1, 37, 4):
            if (line[x] != ' '):
                stackHolder[index].append(str(line[x]))
            index += 1
        stopper += 1
    # working with move-to-from instructions
    elif stopper == 10:
        elements = getElements(line)
        # print(elements)
        stackMover(elements[0], elements[1] - 1, elements[2] - 1)
    # so we can access the txt file after 2 lines
    else:
        stopper += 1

# print(stackHolder)
for x in range(0, 9):
    print(stackHolder[x][0])