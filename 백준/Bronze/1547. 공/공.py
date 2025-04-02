n = int(input())

arr = [False, True, False, False]

for _ in range(n):
    a, b = map(int, input().split())

    arr[a], arr[b] = arr[b], arr[a]

idx = -1

for i in range(len(arr)):
    if arr[i]:
        idx = i

print(idx)