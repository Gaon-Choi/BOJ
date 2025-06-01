import sys
input = sys.stdin.readline

a, b = map(int, input().split())

print(abs(a - b) * "1" + min(a, b) * "2")

