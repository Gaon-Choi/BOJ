import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

for _ in range(T):
    query = input().strip()
    n = int(input())
    temp = input().strip()
    
    arr = deque()

    num = ""

    for c in temp:
        if c.isdigit():
            num += c
        else:
            if len(num) > 0:
                arr.append(int(num))
                num = ""

    is_error = False

    rev = 0

    for q in query:
        if q == "R":
            rev += 1
        else:
            if arr:
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                is_error = True
                break

    if is_error:
        print("error")
    else:
        if rev % 2 == 1:
            arr.reverse()
            
        arr = list(map(str, arr))
        print("[" + ",".join(arr) + "]")
