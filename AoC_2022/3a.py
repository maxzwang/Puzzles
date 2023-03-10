input = []

with open('3_input.txt', 'r') as file:
    for line in file:
        input.append(line.rstrip())

LETTERS = [letter for letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
VALUES = [value for value in range(1, 52+1)]

PRIORITY_DICT = {LETTERS[i]:VALUES[i] for i in range(52)}

total = 0

for sack in input:
    halfsize = int(len(sack) / 2)
    
    left = sack[:halfsize]
    right = sack[halfsize:]

    common_item = (set(left) & set(right)).pop()

    total += PRIORITY_DICT[common_item]

print(total)