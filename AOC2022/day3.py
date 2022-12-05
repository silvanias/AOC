# Part one
lines = []
total = 0
with(open("input.txt", "r") as txt):
    for x in txt:
        if "\n" in x:
            x = x.replace("\n", "")
        half = int(len(x)/2)
        p1 = x[:half]
        p2 = x[half:]
        x = ''.join(set(p1).intersection(p2))
        lines.append(x)
    for y in lines:
        if y.isupper():
            number = (ord(y) - 64) + 26
        else:
            number = (ord(y) - 96)
        total += number
    print(total)

# Part two
import itertools
lines = []
total = 0
with(open("input.txt", "r") as txt):
    for p1,p2,p3 in itertools.zip_longest(*[txt]*3):
        x = ''.join((set(p1).intersection(p2)).intersection(p3))
        if "\n" in x:
           x = x.replace("\n", "")
        lines.append(x) 
    for y in lines:
        if y.isupper():
            number = (ord(y) - 64) + 26
        else:
            number = (ord(y) - 96)
        total += number
    print(total)