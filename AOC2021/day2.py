depth = horiz = aim = 0
with open('input.txt', 'r') as txt:
    txt = txt.read().splitlines()
    for instruction in txt:
        inst = instruction.split(' ')
        if inst[0] == 'forward':
            horiz += int(inst[1])
            depth += int(inst[1]) * aim
        elif inst[0] == 'down':
            aim += int(inst[1])
        elif inst[0] == 'up':
            aim -= int(inst[1])
print(depth*horiz)