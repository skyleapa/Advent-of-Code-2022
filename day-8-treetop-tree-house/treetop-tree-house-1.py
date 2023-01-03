f = open("input_test.txt", "r")

array = [[], []]

visible = 0
yCoord = 0

for line in f:
    # builds array with input
    for i, c in enumerate(line):
        array[i][yCoord].append(c)
    yCoord += 1
    
columns = array[0].length()
rows = yCoord - 1

print(column)
print(rows)
print(visible)