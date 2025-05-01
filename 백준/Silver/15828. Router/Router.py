import sys
input = sys.stdin.readline

from collections import deque

max_size = int(input())

q = deque()

while True:
    elem = int(input())
    
    if elem == -1:
        break

    if elem == 0:
        q.popleft()
    else:
        if len(q) < max_size:
            q.append(elem)

if q:
    print(*q)
else:
    print("empty")