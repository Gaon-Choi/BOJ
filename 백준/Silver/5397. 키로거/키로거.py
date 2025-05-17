import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

for _ in range(N):
    text = input().strip()

    stk1 = deque([])
    stk2 = deque([])

    for c in text:
        if c == "<":
            if not stk1:
                continue
        
            elem = stk1.pop()
            stk2.appendleft(elem)
        elif c == ">":
            if not stk2:
                continue

            elem = stk2.popleft()
            stk1.append(elem)
        elif c == "-":
            if stk1:
                stk1.pop()
        else:
            stk1.append(c)

    print("".join(stk1) + "".join(stk2))