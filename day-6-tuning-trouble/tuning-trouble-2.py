f = open("input_michelle.txt", "r")

# part 2
# O(n)

for line in f:
    elementArray = []
    for index, c in enumerate(line):
        # changed 4 to 14 for part 2
        if len(elementArray) != 14:
            if c not in elementArray:
                elementArray.append(c)
            else:
                for x in range(0, elementArray.index(c) + 1):
                    elementArray.pop(0)
                elementArray.append(c)
        # once elementArray contains 4 valid non duplicate elements, produce the index
        else:
            print(elementArray)
            print(index)
            break
