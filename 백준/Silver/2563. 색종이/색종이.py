import sys

n = 101

paper = [[0] * (n + 1) for _ in range(n + 1)]

N = int(sys.stdin.readline())

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1
            
answer = 0

for i in range(n):
    for j in range(n):
        if paper[i][j] == 1:
            answer += 1
            
print(answer)