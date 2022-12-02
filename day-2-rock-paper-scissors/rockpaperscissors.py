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

# part 2
# --- Part Two ---
# The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y 
# means you need to end the round in a draw, and Z means you need to win. Good luck!"

# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

# In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
# Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

# Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

totalPts = 0

# part 2
for line in f:
    hmm = line.strip()

    elfinput = hmm[0]
    outcome = hmm[len(hmm)-1]

    # if elfinput == "A" and outcome == "X":
        # switch       
    
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