import sys
input = sys.stdin.readline

n = int(input())
ans = 0

lines = []

for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

start, end = lines[0]

for s, e in lines[1:]:
    # 겹치지 않음
    if end < s:
        ans += (end - start)
        start, end = s, e
    # 겹침
    else:
        end = max(end, e)

ans += (end - start)

print(ans)
