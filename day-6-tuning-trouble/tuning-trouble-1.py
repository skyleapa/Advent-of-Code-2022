f = open("input_test.txt", "r")

for line in f:
    potentialMarker = []
    quantity = 0
    for index, c in enumerate(line):
        # load in first 4 values
        if quantity < 4:
            if c not in potentialMarker:
                potentialMarker.append(c)
                quantity += 1
            else:
                for x in range(0, potentialMarker.index(c)):
                    potentialMarker.pop(0)
            print(potentialMarker)
        # else:
        #     print(potentialMarker)
        #     print(c)
        #     potentialMarker.pop(0)
            
        #     if c in potentialMarker:
        #         potentialMarker.append(c)
        #     else:
        #         print(index+1)
        #         break