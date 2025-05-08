import sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, +1))
    arr.append((end, -1))

arr.sort()

cnt = 0
max_cnt = 0

for _, incr in arr:
    cnt += incr
    max_cnt = max(max_cnt, cnt)

print(max_cnt)

