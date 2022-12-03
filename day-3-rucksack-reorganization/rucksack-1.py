f = open("input.txt", "r")

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

for line in f:
    first_half  = line[:len(line)//2]
    second_half = line[len(line)//2:]

    hashmap = {}

    # put every item in the first half into a hashmap
    for c in first_half:
        hashmap[c] = priorityCalc(c)
    
    for c in second_half:
        # if item exists in the hashmap, put into results, with its priority
        if c in hashmap:
            print(str(c) + " : " + str(hashmap[c]))
            prioritySum += hashmap[c]
            break
    
print(prioritySum)

