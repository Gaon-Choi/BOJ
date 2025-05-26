import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

q = deque()

for _ in range(n):
    query = input().strip().split()

    if query[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)

    elif query[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
    
    elif query[0] == "empty":
        print(1 if not q else 0)

    elif query[0] == "size":
        print(len(q))

    elif query[0] == "pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif query[0] == "pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)

    else:
        val = int(query[1])

        if query[0] == "push_front":
            q.appendleft(val)
        
        elif query[0] == "push_back":
            q.append(val)

    