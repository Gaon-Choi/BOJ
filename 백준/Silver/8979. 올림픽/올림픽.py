import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x : (-x[1], -x[2], -x[3]))

rank = 1
prev = arr[0]

for i in range(n):
    if prev == arr[i]:
        continue
    else:
        rank = i
    
    prev = arr[i]

    if k == arr[i][0]:
        print(rank)