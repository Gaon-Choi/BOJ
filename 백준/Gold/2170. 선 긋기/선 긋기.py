import sys
input = sys.stdin.readline

n = int(input())

lines = []

for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

lines.sort(key = lambda x : x[0])

length = 0
start, end = lines[0]

for s, e in lines:
    if end <= s:
        length += (end - start)
        start, end = s, e

    else:
        end = max(end, e)

length += (end - start)

print(length)