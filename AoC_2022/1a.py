def read_calories(file_name):
    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    return lines

def find_max_calories(lines):
    calories = []
    current_sum = 0
    for line in lines:
        if len(line) != 0:
            current_sum += int(line)
        else:
            calories.append(current_sum)
            current_sum = 0

    return max(calories)

if __name__ == '__main__':
    calorie_list = read_calories('1_input.txt')
    print(find_max_calories(calorie_list))