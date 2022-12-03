f = open("input_darryl.txt", "r")

# elf: A - rock; B - paper; C - scissors
# player: X - rock; Y - paper; Z - scissors
# points: 1 - rock; 2 - paper; 3 - scissors; 0 - lose; 3 - draw; 6 - win

# part 1

totalPts = 0
for line in f:
    hmm = line.strip()

    if hmm == 'A Y' or hmm == 'B Z' or hmm == 'C X': # win
        totalPts += 6
    if hmm == 'A X' or hmm == 'B Y' or hmm == 'C Z': # draw
        totalPts += 3

    if hmm[len(hmm)-1] == 'X':
        totalPts += 1
    elif hmm[len(hmm)-1] == 'Y':
        totalPts += 2
    elif hmm[len(hmm)-1] == 'Z':
        totalPts += 3

print(totalPts)

totalPts2 = 0

# part 2
for line in f:
    hmm = line.strip()

    elfinput = hmm[0]
    outcome = hmm[len(hmm)-1]

    # if elfinput == "A" and outcome == "X":
        # switch       
    
    if hmm == 'A Y' or hmm == 'B Z' or hmm == 'C X': # win
        totalPts2 += 6
    if hmm == 'A X' or hmm == 'B Y' or hmm == 'C Z': # draw
        totalPts2 += 3

    if hmm[len(hmm)-1] == 'X':
        totalPts2 += 1
    elif hmm[len(hmm)-1] == 'Y':
        totalPts2 += 2
    elif hmm[len(hmm)-1] == 'Z':
        totalPts2 += 3

print(totalPts2)