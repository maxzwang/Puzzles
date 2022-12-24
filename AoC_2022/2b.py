input = []

with open('2_input.txt', 'r') as file:
    for line in file:
        input.append(line.rstrip())

total = 0

for round in input:
    if "A" in round:
        modulo = 1
    elif "B" in round:
        modulo = 2
    else:
        modulo = 3

    if "X" in round:
        modulo -= 1
    elif "Y" in round:
        total += 3
        # modulo unchanged
    else:
        total += 6
        modulo += 1
    
    modulo = modulo % 3
    if modulo == 0:
        modulo = 3
    
    total += modulo


print(total)