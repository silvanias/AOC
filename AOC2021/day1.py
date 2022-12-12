nums = []
count = 0
count2 = 0
# Take input into list
with open("input.txt", "r") as f:
    for x in f:
        nums.append(x.strip("\n"))

# Part 1
for y in range(len(nums)- 1):
    if int(nums[y]) < int(nums[y+1]): count += 1
print(count)

#Part 2 
for y in range(len(nums) - 3):
    fir = int(nums[y]) + int(nums[y+1]) + int(nums[y+2])
    sir = int(nums[y+1]) + int(nums[y+2]) + int(nums[y+3])
    if sir > fir: count2 += 1
print(count2)