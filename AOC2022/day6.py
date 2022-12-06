# Part 1 & 2 just change num of distinct
import collections
with(open("/Users/silasmaughan/CodingProjects/AOC/AOC2022/input.txt", "r") as txt):
    line = list(txt.read())
    found = False
    i = 0
    distinct = 14
    while (found == False):
        temp = []
        for x in range(distinct):
            temp.append(line[i + x])
        temp = [item for item, count in collections.Counter(temp).items() if count > 1] 
        if len(temp) == 0:
            found = True
            print(i + distinct)
            break
        else:
            i += 1