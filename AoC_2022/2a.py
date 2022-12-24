input = []

with open('2_input', 'r') as file:
    for line in file:
        input.append(line.rstrip())

total = 0

for round in input:
    if round == "A Y" or round == "B Z" or round == "C X":
        total += 6
    elif round == "A X" or round == "B Y" or round == "C Z":
        total += 3
    else:
        total += 0 # loss gets zero points lol, should I just write pass

    if "X" in round:
        total += 1
    elif "Y" in round:
        total += 2
    else:
        total += 3

print(total)