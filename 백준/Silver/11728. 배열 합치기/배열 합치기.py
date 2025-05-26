import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

res = []

a = deque(list(map(int, input().split())))
b = deque(list(map(int, input().split())))

while a or b:
    if a and b:
        if a[0] < b[0]:
            res.append(a.popleft())
        else:
            res.append(b.popleft())
    elif a:
        res.append(a.popleft())
    else:
        res.append(b.popleft())

print(*res)
