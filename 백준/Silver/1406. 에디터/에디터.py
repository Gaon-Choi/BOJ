import sys
input = sys.stdin.readline

from collections import deque

text = input().strip()

left = deque(list(text))
right = deque()

k = int(input())

for _ in range(k):
    q = input().split()

    mode = q[0]

    if mode == "D":
        if right:
            elem = right.popleft()
            left.append(elem)
    
    elif mode == "L":
        if left:
            elem = left.pop()
            right.appendleft(elem)
    
    elif mode == "B":
        if left:
            left.pop()

    elif mode == "P":
        c = q[1]

        left.append(c)

for c in left:
    print(c, end="")

for c in right:
    print(c, end="")