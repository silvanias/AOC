end = 0
with open("input.txt", 'r') as f:
    data = list(map(int, f.read().splitlines()))

for num in range(len(data) - 3):
    comp = data[num] + data[num+1] + data[num+2]
    if comp < (data[num+1] + data[num+2] + data[num+3]):
        end += 1

print(end)