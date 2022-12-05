# Part one
stack = [[],[],[],[],[],[],[],[],[]]
with(open("input.txt", "r") as txt):
    lines = txt.read().splitlines()
    j = 0
    amtOfStacks = 9
    rev = True
    for line in lines:
        # Get everything   
        if (j<8):  
            line = line.replace(" ", "_")
            line = list(line)
            for x in range(1,amtOfStacks):
                i = (4 * x) - 1
                line[i] = '.'
            line = "".join(line)
            line = line.split('.')
            for x in range(amtOfStacks):
                if line[x] != '___':
                    stack[x].append(line[x])
            j += 1
            continue
        elif (rev):
            for k in range(amtOfStacks):
                stack[k].reverse()
            rev = False
            continue
        elif (line == ''):
            continue
        line = line.split()
        del line[0], line[1], line[2]
        for x in range(int(line[0])):
            stack[int(line[2]) - 1].append(stack[int(line[1]) - 1].pop())
    for x in range(amtOfStacks):
        print(stack[x].pop())

# Part 2
stack = [[],[],[],[],[],[],[],[],[]]
with(open("input.txt", "r") as txt):
    lines = txt.read().splitlines()
    j = 0
    amtOfStacks = 9
    rev = True
    for line in lines:
        # Get everything   
        if (j<8):  
            line = line.replace(" ", "_")
            line = list(line)
            for x in range(1,amtOfStacks):
                i = (4 * x) - 1
                line[i] = '.'
            line = "".join(line)
            line = line.split('.')
            for x in range(amtOfStacks):
                if line[x] != '___':
                    stack[x].append(line[x])
            j += 1
            continue
        elif (rev):
            for k in range(amtOfStacks):
                stack[k].reverse()
            rev = False
            continue
        elif (line == ''):
            continue

        line = line.split()
        del line[0], line[1], line[2]
        print(line)
        tstack = []
        for x in range(int(line[0])):
            tstack.append(stack[int(line[1]) - 1].pop())
        tstack.reverse()
        stack[int(line[2]) - 1].extend(tstack)
    for x in range(amtOfStacks):
        print(stack[x].pop())