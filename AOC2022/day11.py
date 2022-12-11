# Part 1
ops = {"+": (lambda i,j: i+j), "*": (lambda i,j: i*j)}
with(open("input.txt", "r") as txt):
    lines = txt.read().splitlines()
    monks = []
    monkInspec = []
    test = [0,0,0]
    oper = []
    # Set up inventory for all monkeys
    for x in lines:
        x = x.split()
        if x == []:
            continue
        match x[0][0]:
            case "S":
                monks.append([int(y.replace(",","")) for y in x[2:]])
                monkInspec.append(0) 

    rcount = 0
    while rcount < 20:
        currMonk = 0
        for x in lines:
            x = x.split()
            # If all strings are parsed
            if x == []:
                g = 0
                while g < len(monks[currMonk]):
                    if oper[1] == 'old':
                        monks[currMonk][g] = monks[currMonk][g] * monks[currMonk][g] 
                    else:
                        monks[currMonk][g] = ops[oper[0]](monks[currMonk][g],int(oper[1]))
                    monks[currMonk][g] = monks[currMonk][g] // 3
                    if monks[currMonk][g] % test[0] == 0:
                        tp = monks[currMonk].pop(0)
                        monks[test[1]].append(tp)                            
                    else:
                        tp = monks[currMonk].pop(0)
                        monks[test[2]].append(tp)
                    monkInspec[currMonk] += 1
                currMonk += 1
                continue
            match x[0][0]:
                case "O":
                    oper = x[4:]
                case "T":
                    test[0] = int(x[3])
                case "I":
                    if x[1] == "true:":
                        test[1] = int(x[5])
                    else:
                        test[2] = int(x[5])
        rcount += 1
    monkInspec.sort(reverse=True)
    print(monkInspec[0]*monkInspec[1])


# Part 2
ops = {"+": (lambda i,j: i+j), "*": (lambda i,j: i*j)}
with(open("input.txt", "r") as txt):
    lines = txt.read().splitlines()
    monks = []
    monkInspec = []
    test = [0,0,0]
    oper = []
    primeFactors = 1
    # Set up inventory for all monkeys
    for x in lines:
        x = x.split()
        if x == []:
            continue
        match x[0][0]:
            case "S":
                monks.append([int(y.replace(",","")) for y in x[2:]])
                monkInspec.append(0)
            case "T":
                primeFactors = primeFactors * int(x[3])

    rcount = 0
    while rcount < 10000:
        currMonk = 0
        for x in lines:
            x = x.split()
            # If all strings are parsed
            if x == []:
                g = 0
                while g < len(monks[currMonk]):
                    if monks[currMonk][g] > primeFactors:
                        monks[currMonk][g] = monks[currMonk][g] % primeFactors
                    if oper[1] == 'old':
                        monks[currMonk][g] = monks[currMonk][g] * monks[currMonk][g] 
                    else:
                        monks[currMonk][g] = ops[oper[0]](monks[currMonk][g],int(oper[1]))
                        pass
                    if monks[currMonk][g] % test[0] == 0:
                        tp = monks[currMonk].pop(0)
                        monks[test[1]].append(tp)                            
                    else:
                        tp = monks[currMonk].pop(0)
                        monks[test[2]].append(tp)
                    monkInspec[currMonk] += 1
                currMonk += 1
                continue
            match x[0][0]:
                case "O":
                    oper = x[4:]
                case "T":
                    test[0] = int(x[3])
                case "I":
                    if x[1] == "true:":
                        test[1] = int(x[5])
                    else:
                        test[2] = int(x[5])
        rcount += 1
    monkInspec.sort(reverse=True)
    print(monkInspec[0]*monkInspec[1])
        