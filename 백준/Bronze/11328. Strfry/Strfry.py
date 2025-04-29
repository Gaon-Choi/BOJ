import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = input().split()
    a = list(a); b = list(b)

    a.sort(); b.sort()

    if ''.join(a) == ''.join(b):
        print("Possible")
    else:
        print("Impossible")
        