# f = open("input_test.txt", "r")

# rows, columns = 5, 5 #99

# array = []

# yCoord = 0
# visible = 0

# for line in f:
#     col = []
#     # builds array with input
#     for i, c in enumerate(line):
#         col.append(c)
#     array.append(col)


# print(array)
# print(visible)

import numpy as np

f = open('input_test.txt', 'r')
tree_line = f.readlines()
lines_list = []

# convert the input in a matrix
for line in tree_line:
    list_current_line = list(line)  # convert line into list
    list_current_line = list_current_line[:len(list_current_line) - 1]  # get rid of the \n at the end of each line
    lines_list.append(list_current_line)  # add new line to the list of lists

matrix = np.array(lines_list)  # convert the list of lists into a matrix array

n_row = len(matrix)
n_col = len(matrix[1, :])
print(n_row, n_col)

visible = 0
for i in range(1, n_row-1):
    for j in range(1, n_col-1):
        row = matrix[i, :]  #all the line
        col = matrix[:, j]
        height_tree = matrix[i, j]
        right = row[j+1:]
        left = row[:j]
        up = col[:i]
        down = col[i+1:]
        #print(i, j)
        #print(row, col, height_tree)
        #print(right, left, up, down)
        if right.size > 0 and height_tree > max(right):
            visible += 1
        elif left.size > 0 and height_tree > max(left):
            visible += 1
        elif up.size > 0 and height_tree > max(up):
            visible += 1
        elif down.size > 0 and height_tree > max(down):
            visible += 1

visible += n_row *2 + (n_col-2) *2  #add the margins because they are all seen
print(visible)