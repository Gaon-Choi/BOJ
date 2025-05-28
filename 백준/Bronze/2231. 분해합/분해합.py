import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n + 1):
    if i + sum(map(int, list(str(i)))) == n:
        print(i)
        exit(0)
else:
    print(0)
