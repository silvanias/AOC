with(open("/Users/silasmaughan/CodingProjects/AOC/AOC2022/input.txt", "r") as txt):
    maze = []
    sPos = []
    ePos = []
    lines = txt.read().splitlines()
    # Initialise the grid
    for i in range(len(lines)):
        maze.append([])
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                maze[i].append(0)
                sPos = [i,j] 
            elif lines[i][j] == 'E':
                maze[i].append(27)
                ePos = [i,j]
            else:
                maze[i].append(ord(lines[i][j]) - 96)
    print(maze)