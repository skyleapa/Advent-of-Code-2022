f = open("input_michelle.txt", "r")

# part 1
# O(n)

for line in f:
    elementArray = []
    for index, c in enumerate(line):
        if len(elementArray) != 4:
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
