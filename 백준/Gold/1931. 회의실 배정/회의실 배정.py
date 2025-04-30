import sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key = lambda x : (x[1], x[0]))

start, end = arr[0]
cnt = 1

for i in range(1, n):
    s, e = arr[i]

    if end <= arr[i][0]:
        cnt += 1
        start, end = arr[i]

print(cnt)