
path = '2022/03/input.txt'

with open(path, 'r') as file:
    input = file.read()

rucksacks = {rucksack[1]: rucksack[0] // 3 for rucksack in enumerate(input.split('\n')) if rucksack[1] != ''}

def sort_rucksack(rucksack):
    first_compartment, second_compartment = split_rucksack(rucksack)
    item = compare_compartments(first_compartment, second_compartment)[0]
    priority = get_priority(item)

    return priority


def split_rucksack(rucksack):
    first_output = rucksack[0: int(len(rucksack)/2)]
    second_output = rucksack[int(len(rucksack)/2):int(len(rucksack))]

    return first_output, second_output


def compare_compartments(first, second):
    return [item for item in first if item in second]


def get_priority(item):
    if item.upper() == item:
        output = ord(item) - 38
    elif item.lower() == item:
        output = ord(item) - 96
    
    return output


def get_group_priority(group):
    badge_item = list(find_badge_item(group))[0]

    return get_priority(badge_item)


def find_badge_item(group):
    return set(group[0]).intersection(set(group[1]), set(group[2]))


results = map(sort_rucksack, rucksacks)
print(sum([result for result in results]))

groups = set(list(rucksacks.values()))
group_priorities = [get_group_priority([rucksack for rucksack, v in rucksacks.items() if rucksacks[rucksack] == group]) for group in groups]

print(sum(group_priorities))
