import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

flag = True

for _ in range(n):
    x, y = map(int, input().split())
    
    if x == 1:
        cnt += y
    else:
        if y <= cnt:
            cnt -= y
        else:
            flag = False
            break

if flag:
    print("See you next month")
else:
    print("Adios")
