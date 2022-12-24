def read_calories(file_name):
    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    return lines

def find_top_calories(lines, n):
    calories = []
    current_sum = 0
    for line in lines:
        if len(line) == 0:
            calories.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line)

    top_calories_sum = 0
    for i in range(n):
        top_calories_sum += calories.pop(calories.index(max(calories)))

    return top_calories_sum
        

if __name__ == '__main__':
    calorie_list = read_calories('1_input')
    print(find_top_calories(calorie_list, 3))