f = open("input_michelle.txt", "r")

# O(n) solution

maxCalorie = 0
currCalorie = 0

first = 0
second = 0
third = 0

#first sol
for line in f:
    if line == '\n':
        if currCalorie > maxCalorie:
            maxCalorie = currCalorie
        currCalorie = 0
    else:
        currCalorie += int(line)
  
print(maxCalorie)

# second sol

# for line in f:
#     if (line.strip() == ""):
#         maxCalorie = max(currCalorie, maxCalorie)
#         currCalorie = 0
#         print("new max is " + str(maxCalorie))
#         continue
#     currCalorie += int(line)
#     print("The current calories " + str(currCalorie))

# print("The max calories is " + str(maxCalorie))