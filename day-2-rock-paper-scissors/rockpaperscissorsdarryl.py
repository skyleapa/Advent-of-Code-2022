f = open("input_michelle.txt", "r")

# elf: A - rock; B - paper; C - scissors
# player: X - rock; Y - paper; Z - scissors
# points: 1 - rock; 2 - paper; 3 - scissors; 0 - lose; 3 - draw; 6 - win
totalPts = 0

# your response as the key, the enemy's response as the value
data = {}

answers = {
    "X": "C", # rock beats scissors
    "Y": "A", # paper beats rock
    "Z": "B", # scissors beats paper
}

tie = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

# populate the hashmap with user data
for line in f:
    lineSplit = line.split() # Given "A Y" -> ["A", "Y"]
    data[lineSplit[1]] = lineSplit[0]

print(data)

for key, value in data.items():
    # calculate shape selected
    if key == "X":
        totalPts += 1
    elif key == "Y":
        totalPts += 2
    else:
        totalPts += 3

    # check if won
    if answers[key] == value:
        totalPts += 6
    elif tie[key] == value:
        totalPts += 3

print(totalPts) 
    