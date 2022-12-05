# Part 1
counter = 0
with(open("input.txt", "r") as txt):
    for x in txt:
        if "\n" in x:
            x = x.replace("\n", "")
        x = x.split(",")
        p1 = [int(x) for x in x[0].split("-")]
        p2 = [int(x) for x in x[1].split("-")]
        if (p1[0] <= p2[0] and p1[1] >= p2[1]) or (p1[0] >= p2[0] and p1[1] <= p2[1]):
            counter += 1
print(counter)

# Part 2
counter = 0
with(open("input.txt", "r") as txt):
    for x in txt:
        if "\n" in x:
            x = x.replace("\n", "")
        x = x.split(",")
        p1 = [int(x) for x in x[0].split("-")]
        p2 = [int(x) for x in x[1].split("-")]
        if p2[1] >= p1[0] >= p2[0]:
            counter += 1
        elif p2[1] >= p1[1] >= p2[0]:
            counter += 1
        elif p1[1] >= p2[0] >= p1[0]:
            counter += 1
        elif p1[1] >= p2[1] >= p1[0]:
            counter += 1      
print(counter)