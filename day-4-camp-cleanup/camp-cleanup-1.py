f = open("input_darryl.txt", "r")

# O(n) solution

# part 1

# logic: for example with 2-8,3-7, evaluate as a-b,c-d
# get the values a, b, c, d. 
# if a == c or b == d, pairsContained++
# if a<c, then if d<b, pairsContained++
# if a>c, then if d>b, pairsContained++

pairsContained = 0

for line in f:
    first_half = line.split(',')[0]
    second_half = line.split(',')[1]
    a = int(first_half.split("-")[0])
    b = int(first_half.split("-")[1])
    c = int(second_half.split("-")[0])
    d = int(second_half.split("-")[1])
    
    if a == c or b == d:
        pairsContained += 1
    elif a < c:
        if d < b:
            pairsContained += 1
    elif a > c:
        if d > b:
            pairsContained += 1

print(pairsContained)