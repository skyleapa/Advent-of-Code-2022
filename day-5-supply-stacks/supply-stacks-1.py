# 8 rows denoting the max length of the stack

# stack one is col 1
# two is 5
# three is 9
# four is 13
# five is 17
# six is 21
# seven is 25
# eight is 29
# nine is 33

f = open("input_test.txt", "r") # -> CMZ

stackHolder = [[], [], [], [], [], [], [], [], []]
currCol = 1

for index, line in enumerate(f):
    # the row
    if index <= 3:
        # each character
        for i, c in enumerate(line):
            if i - 1 == currCol:
                if not c == ' ':
                    print(c)
                    stackHolder[index].append(line[currCol])
            currCol += 4
        currCol = 0

print(stackHolder)

