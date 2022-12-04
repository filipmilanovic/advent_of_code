
path = '2022/04/input.txt'

with open(path, 'r') as file:
    input = file.read()


def get_overlaps(assignment, strategy):
    elf_1, elf_2 = get_elf_sections(assignment)
    overlaps = sorted(list(set(elf_1).intersection(set(elf_2))))

    if strategy == 1:
        return overlaps in [elf_1, elf_2]
    elif strategy == 2:
        return len(overlaps) > 0


def get_elf_sections(assignment):
    elf_1 = get_sections(assignment[0])
    elf_2 = get_sections(assignment[1])

    return elf_1, elf_2


def get_sections(elf):
    bounds = elf.split('-')

    return list(range(int(bounds[0]), int(bounds[1]) + 1))


assignments_1 = [get_overlaps(assignment.split(','), 1) for assignment in input.split('\n') if assignment != '']
assignments_2 = [get_overlaps(assignment.split(','), 2) for assignment in input.split('\n') if assignment != '']

print(sum(assignments_1))
print(sum(assignments_2))
