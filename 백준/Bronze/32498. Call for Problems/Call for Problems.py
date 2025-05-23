import sys
input = sys.stdin.readline

n = int(input())

cnt = 0

for _ in range(n):
    elem = int(input())
    if elem % 2 != 0:
        cnt += 1
        
print(cnt)