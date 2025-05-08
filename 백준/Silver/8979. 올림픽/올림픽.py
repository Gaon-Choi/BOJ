import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x : (-x[1], -x[2], -x[3]))

rank = 0
prev = [0, 0, 0, 0]

for i in range(n):
    if prev != arr[i][1:]:
        rank = i
    
    prev = arr[i][1:]

    if k == arr[i][0]:
        print(rank + 1)
