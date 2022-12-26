input = []

with open('4_input.txt', 'r') as file:
    for line in file:
        elves = line.rstrip().split(",")
        input.append([elf.split("-") for elf in elves])

total = 0

for pair in input:

    (elf1, elf2) = pair
    (a, b) = elf1
    (c, d) = elf2

    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    if (a <= c and b >= d) or (a >= c and b <= d):
        total += 1

print(total)