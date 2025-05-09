import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = input().strip()
    print(len(num))