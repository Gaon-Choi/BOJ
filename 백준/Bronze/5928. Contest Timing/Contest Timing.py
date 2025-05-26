import sys
input = sys.stdin.readline

original = 11 * 24 * 60 + 11 * 60 + 11

D, H, M = map(int, input().split())

sum_ = D * 24 * 60 + H * 60 + M

if sum_ < original:
    print(-1)
else:
    print(sum_ - original)
