arr = []

i = 1

for _ in range(8):
    arr.append((int(input()), i))
    i += 1
    
arr.sort(key = lambda x : -x[0])

total = 0
rank = []

for i in range(5):
    total += arr[i][0]
    rank.append(arr[i][1])
    
rank.sort()
    
print(total)
for elem in rank:
    print(elem, end=" ")