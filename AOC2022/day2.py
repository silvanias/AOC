# Part 1
with(open("input.txt", "r") as txt):    
    ls = []
    score = 0
    d = {'A':0, 'B':1, 'C':2, 'X':0, 'Y':1, 'Z':2}
    s = {0:3, 1:6, 2:0}
    for x in txt:
        ls = x.split()
        score += d[ls[1]] + 1
        score += s[((d[ls[1]]-d[ls[0]])%3)]
    print(score)


# Part 2
with(open("input.txt", "r") as txt):
    ls = []
    l = [1,2,3]
    score = 0
    for x in txt:
        ls = x.split()
        match ls[1]:
            case 'X':
                match ls[0]:
                    case 'A':
                        score += 3
                    case 'B':
                        score += 1
                    case 'C':
                        score += 2
            case 'Y':
                score += 3
                match ls[0]:
                    case 'A':
                        score += 1
                    case 'B':
                        score += 2
                    case 'C':
                        score += 3
            case 'Z':
                score += 6
                match ls[0]:
                    case 'A':
                        score += 2
                    case 'B':
                        score += 3
                    case 'C':
                        score += 1
    print(score)