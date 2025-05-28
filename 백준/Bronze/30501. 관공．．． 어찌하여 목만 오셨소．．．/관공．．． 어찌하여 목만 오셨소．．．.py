import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    name = input().strip()

    if "S" in name:
        print(name)
        break
    