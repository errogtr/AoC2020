from copy import copy


def parse_instruction(line):
    name, val = line.split()
    return name, int(val)


def execute(instructions):
    current = 0
    accumulator = 0
    executed = {current}
    while True:
        name, val = instructions[current]
        match name:
            case "acc":
                accumulator += val
                current += 1
            case "jmp":
                current += val if val else 1
            case "nop":
                current += 1
        completed = current == len(instructions)
        if (current in executed) or completed:
            break
        else:
            executed.add(current)
    return accumulator, completed


with open("data") as f:
    instructions = [parse_instruction(l) for l in f.read().splitlines()]

# ========= PART 1 ==========
accumulator, _ = execute(instructions)
print(accumulator)

# ========= PART 2 ==========
for i, (name, val) in enumerate(instructions):
    modified = copy(instructions)
    match name:
        case "acc":
            continue
        case "jmp":
            modified[i] = "nop", val
        case "nop":
            modified[i] = "jmp", val
    accumulator, completed = execute(modified)
    if completed:
        break
print(accumulator)
