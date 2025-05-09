import sys
input = sys.stdin.readline

t, s = map(int, input().split())

if s == 1 or not (12 <= t <= 16):
    print(280)
else:
    print(320)