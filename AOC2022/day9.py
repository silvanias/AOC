"""
# Day 1
def connected(h,t):
    if (h in surr(t)):
        return True
    else:
        return False

def surr(knot):
    surround = []
    for i in range(-1,2):
        for j in range(-1,2):        
            surround.append([knot[0] + i, knot[1] + j])
    return surround

with(open("/Users/silasmaughan/CodingProjects/AOC/AOC2022/input.txt", "r") as txt):
    lines = txt.read().splitlines()
    h = [0,0]
    t = [0,0]
    tHistory = [[0,0]]
    for x in lines:
        x = x.split()
        amt = int(x[1])
        for a in range(amt):
            temp = h.copy()
            match x[0]:
                case 'R':
                    h[0] += 1
                case 'L':
                    h[0] -= 1
                case 'D':
                    h[1] -= 1
                case 'U':
                    h[1] += 1
            if (connected(h,t) == False):
                t = temp
                tHistory.append(t)
    tSquares = []
    for squares in tHistory:
        if squares not in tSquares:
            tSquares.append(squares)
    print(len(tSquares))
"""
# Day 2
def connected(h,t):
    if (h in surr(t)):
        return True
    else:
        return False

def surr(knot):
    surround = []
    for i in range(-1,2):
        for j in range(-1,2):        
            surround.append([knot[0] + i, knot[1] + j])
    return surround

def planeDiscon(h,t):
    minus = [h[0] - t[0],h[1] - t[1]]
    if minus[0] == 0 or minus[1] == 0:
        return True

with(open("/Users/silasmaughan/CodingProjects/AOC/AOC2022/input.txt", "r") as txt):
    lines = txt.read().splitlines()
    b = [0,0]
    b1 = [0,0]
    b2 = [0,0]
    b3 = [0,0]
    b4 = [0,0]
    b5 = [0,0]
    b6 = [0,0]
    b7 = [0,0]
    b8 = [0,0]
    b9 = [0,0]
    body = [b,b1,b2,b3,b4,b5,b6,b7,b8,b9]
    tHistory = []
    for x in lines:
        x = x.split()
        amt = int(x[1])
        for a in range(amt):
            # Current pos of head
            temp = body[0].copy()
            temp2 = body[1]
            match x[0]:
                case 'R':
                    body[0][0] += 1
                case 'L':
                    body[0][0] -= 1
                case 'D':
                    body[0][1] -= 1
                case 'U':
                    body[0][1] += 1
            
            # do for all body pieces
            for p in range(len(body) - 1):
                minus = [body[p][0] - body[p+1][0],body[p][1] - body[p+1][1]]       
                if (connected(body[p],body[p + 1]) == False):
                    # If on a plane from head
                    if(planeDiscon(body[p],body[p + 1]) == True):
                        if minus[0] > 0:
                            body[p + 1][0] += 1
                        elif minus[0] < 0:
                            body[p + 1][0] -= 1
                        elif minus[1] > 0:
                            body[p + 1][1] += 1
                        elif minus[1] < 0:
                            body[p + 1][1] -= 1   
                        continue

                    # If diagonal 
                    # NE
                    if minus[0] > 0 and minus[1] > 0:
                        body[p+1][0] += 1
                        body[p+1][1] += 1
                    # SE
                    elif minus[0] > 0 and minus[1] < 0:
                        body[p+1][0] += 1
                        body[p+1][1] -= 1
                    # SW
                    elif minus[0] < 0 and minus[1] < 0:
                        body[p+1][0] -= 1
                        body[p+1][1] -= 1
                    # NW 
                    elif minus[0] < 0 and minus[1] > 0:
                        body[p+1][0] -= 1
                        body[p+1][1] += 1
            toAppend = body[9].copy()
            tHistory.append(toAppend)
    
    tSquares = []
    for squares in tHistory:
        if squares not in tSquares:
            tSquares.append(squares)
    print(len(tSquares))
   