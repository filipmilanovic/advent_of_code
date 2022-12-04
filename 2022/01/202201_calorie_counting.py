path = '2022/01/input.txt'


with open(path, 'r') as file:
    input = file.read()

elves = [elf.split('\n') for elf in input.split('\n\n')]
total_calories = [sum([int(item) for item in elf if item != '']) for elf in elves]

total_calories.sort(reverse=True)

print(total_calories[0])
print(sum(total_calories[0:3]))
