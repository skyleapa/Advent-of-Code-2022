f = open("input_michelle.txt", "r")

for line in f:
    for c in line:
        position = 0
        needSleep = 0
        wantRamen = []
        if needSleep < 4:
            if (line[needSleep] not in wantRamen):
                wantRamen.append(line[needSleep])
                needSleep += 1
            else:
                print()
        else:
            wantRamen = []
            needSleep = 0
