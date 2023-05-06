gamma = ''
epsi = ''
# Part 1 
with open('input.txt', 'r') as inp:
    inp = inp.read().splitlines()
    for x in range(len(inp[0])):
        count_1 = count_0 = 0
        for line in inp:            
            if line[x] == '1':
                count_1 += 1
            else:
                count_0 += 1
        if count_1>count_0:
            gamma += '1'
            epsi += '0'
        else:
            gamma += '0'
            epsi += '1'

print(int(gamma,2)*int(epsi,2))