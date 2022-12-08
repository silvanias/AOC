# Day 1
def isVisible (coord, map):
    visible = wVisible = nVisible = eVisible = sVisible = True
    height = map[coord[0]][coord[1]]
    yPos = coord[0]
    xPos = coord[1]

    # Is tree on border?
    if (xPos == 0) or (yPos == 0) or (xPos == len(map[0]) - 1) or (yPos == len(map) - 1):
        visible = True
        return visible 

    # North   
    while (yPos > 0):
        if map[(yPos - 1)][xPos] >= height:
            nVisible = False
            break   
        yPos -= 1
            
    # West
    yPos = coord[0]
    xPos = coord[1]
    while (xPos > 0):
        if map[(yPos)][xPos - 1] >= height:
            wVisible = False
            break   
        xPos -= 1

    # South
    yPos = coord[0]
    xPos = coord[1]
    while (yPos < (len(map) - 1)):
        if map[(yPos + 1)][xPos] >= height:
            sVisible = False
            break   
        yPos += 1

    # East
    yPos = coord[0]
    xPos = coord[1]
    while (xPos < (len(map[0]) - 1)):
        if map[(yPos)][xPos + 1] >= height:
            eVisible = False
            break   
        xPos += 1

    if (nVisible or eVisible or sVisible or wVisible):
        visible = True
    else:
        visible = False
    return visible

with(open("/Users/silasmaughan/CodingProjects/AOC/AOC2022/input.txt", "r") as txt):
    lines = txt.read().splitlines()
    map = []
    count = 0
    for line in lines:
        map.append([*line])
    for x in range(len(map[0])):
        for y in range(len(map)):
            if(isVisible([y, x], map)):
                count += 1
    print(count)

# Part 2
def scenicScore (coord, map):
    height = map[coord[0]][coord[1]]
    yPos = coord[0]
    xPos = coord[1]
    nDistance = eDistance = wDistance = sDistance = 0

    # North   
    while (yPos > 0):
        nDistance += 1
        if map[(yPos - 1)][xPos] >= height:
            break   
        yPos -= 1
            
    # West
    yPos = coord[0]
    xPos = coord[1]
    while (xPos > 0):
        wDistance += 1
        if map[(yPos)][xPos - 1] >= height:
            break   
        xPos -= 1

    # South
    yPos = coord[0]
    xPos = coord[1]
    while (yPos < (len(map) - 1)):
        sDistance += 1
        if map[(yPos + 1)][xPos] >= height:
            break   
        yPos += 1

    # East
    yPos = coord[0]
    xPos = coord[1]
    while (xPos < (len(map[0]) - 1)):
        eDistance += 1
        if map[(yPos)][xPos + 1] >= height:
            break   
        xPos += 1
    
    score = nDistance * eDistance * wDistance * sDistance 
    return score

with(open("/Users/silasmaughan/CodingProjects/AOC/AOC2022/input.txt", "r") as txt):
    lines = txt.read().splitlines()
    map = []
    m = []
    for line in lines:
        map.append([*line])
    for x in range(len(map[0])):
        for y in range(len(map)):
            m.append(scenicScore([y, x], map))
    print(max(m))