import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    num = int(input())
    print("even" if num & 1 == 0 else "odd")