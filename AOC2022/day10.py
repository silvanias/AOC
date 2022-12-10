# Part 1
def noop(pc):
    pc[0] += 1

def addx(pc, amt, count):
    for x in range(2):
        pc[0] += 1
        if ((pc[0] + 20) % 40) == 0:
           count[0] += pc[1]*pc[0]
    pc[1] += amt


with(open("/Users/silasmaughan/CodingProjects/AOC/AOC2022/input.txt", "r") as txt):
    lines = txt.read().splitlines()
    count = [0]
    # pc[0] refers to how many cycles have been completed
    pc = [0,1]
    for line in lines:
        line = line.split()
        if line[0] == "noop":
            noop(pc)
            if ((pc[0] + 20) % 40) == 0:
                count[0] += pc[1]*pc[0]
        if line[0] == "addx":
            addx(pc, int(line[1]), count)
    print(count[0])

#Part 2
def noop(pc,crt):
    pc[0] += 1
    upCRT(pc,crt)

def addx(pc, amt, crt, row):
    for x in range(2):
        if pc[0] >= 40:
            row[0] += 1
            pc[0] = 0
        pc[0] += 1
        upCRT(pc,crt[row[0]])
    pc[1] += amt
    pass 

def upCRT(pc, crtLine):
    cpbd = pc[0] - 1
    spritePos = [pc[1] - 1, pc[1], pc[1] + 1]
    crtLine[pc[0]-1] = "."
    for x in range(len(spritePos)):
        if spritePos[x] == cpbd:
            if crtLine[spritePos[x]] == ".":
                crtLine[spritePos[x]] = "#"
    


with(open("/Users/silasmaughan/CodingProjects/AOC/AOC2022/input.txt", "r") as txt):
    lines = txt.read().splitlines()
    
    crt = [[],[],[],[],[],[]]
    for y in range(6):
        for x in range(40):
            crt[y].append("_")
    # pc[0] = amount cycles have been completed
    pc = [0,1]
    # Line of CRT drawing to
    row = [0]
    for line in lines:
        # Transition to next line
        if pc[0] >= 40:
            row[0] += 1
            pc[0] = 0
        line = line.split()
        if line[0] == "noop":
            noop(pc, crt[row[0]])
        if line[0] == "addx":
            addx(pc, int(line[1]), crt, row)
    for x in range(len(crt)):
        print("".join(crt[x]))