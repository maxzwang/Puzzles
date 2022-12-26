import string

input = []

with open('3_input.txt', 'r') as file:
    for line in file:
        input.append(line.rstrip())

LETTERS = list(string.ascii_lowercase + string.ascii_uppercase)
VALUES = [value for value in range(1, 52+1)]

PRIORITY_DICT = {LETTERS[i]:VALUES[i] for i in range(52)}

total = 0

for i in range(int(len(input)/3)):
    sack1 = input[3*i]
    sack2 = input[3*i + 1]
    sack3 = input[3*i + 2]

    common_item = (set(sack1) & set(sack2) & set(sack3)).pop()

    total += PRIORITY_DICT[common_item]

print(total)