nums = [0] * 26

string = input()
string = string.upper()

for i in range(len(string)):
    nums[ord(string[i])-65] += 1
maxim = max(nums); count = 0
for elem in nums:
    if elem == maxim: count += 1
if count > 1: print("?")
else: print(chr(nums.index(maxim)+65))