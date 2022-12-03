f = open("input_darryl.txt", "r")

prioritySum = 0

def priorityCalc(letter):
    priorityValue = ord(letter)

    # lowercase 97 - 122
    if (priorityValue > 96):
        priorityValue -= 96
        return priorityValue
    else:
    # uppercase 65 - 90
        priorityValue -= 64 - 26
        return priorityValue


# the logic: 
# line 1 - put all keys (the letter) into hashmap with value = 1
# line 2 - check if c appears in hashmap, if so, increment value++
# line 3 - check if c appears in hashmap, if so, check if value = 2, if so then add priorityCalc(c) to prioritySum

currLine = 1

hashmap = {}

for line in f:
    if currLine == 1:
        for c in line:  
            hashmap[c] = 1
        currLine += 1
    elif currLine == 2:
        for c in line:
            if c in hashmap:
                hashmap[c] = 2
        currLine += 1
    elif currLine == 3:
        for c in line:
            if hashmap.get(c) == 2:
                calc = priorityCalc(c)
                prioritySum += calc
                hashmap = {}
        currLine = 1
    
print(prioritySum)