# Part 1 & 2 just change num of distinct
with(open("/Users/silasmaughan/CodingProjects/AOC/AOC2022/input.txt", "r") as txt):
    line = list(txt.read())
    distinct = 14
    for i in range(len(line)):
        if len(set(line[i:(distinct + i)])) == distinct:
            print(i + distinct)