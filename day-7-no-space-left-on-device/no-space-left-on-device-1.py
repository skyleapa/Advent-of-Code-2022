f = open("input_darryl.txt", "r")

# logic
# cases: $ cd (cd .. and cd gmz), dir, $ ls, # -> code

# create the tree using 2d array 
# set up the commands
# build tree directory

directTree = []

for line in f:
    