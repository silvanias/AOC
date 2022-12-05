with(open("input.txt", "r") as txt):
    temp = 0
    ls = []
    for x in txt:
        if "\n" in x:
            x = x.replace("\n", "")
        if x == "":
            ls.append(temp)
            temp = 0
        else:
            temp += int(x)
    ls.sort(reverse = True)
    # Part 1
    print(ls[0])
    # Part 2
    print(sum(ls[:3]))