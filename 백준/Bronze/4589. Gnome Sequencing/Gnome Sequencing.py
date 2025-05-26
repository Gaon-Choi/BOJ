import sys
input = sys.stdin.readline

n = int(input())

print("Gnomes:")

for _ in range(n):
    a, b, c = map(int, input().split())

    if a <= b <= c or c <= b <= a:
        print("Ordered")
    else:
        print("Unordered")
