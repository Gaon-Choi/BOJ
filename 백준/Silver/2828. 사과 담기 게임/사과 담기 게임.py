import sys
input = sys.stdin.readline

n, m = map(int, input().split())

left, right = 0, m - 1

total_dist = 0

t = int(input())

for _ in range(t):
    loc = int(input()) - 1

    if right < loc:
        diff = (loc - right)
        total_dist += diff
        left += diff; right += diff
    elif loc < left:
        diff = (left - loc)
        total_dist += diff
        left -= diff; right -= diff

print(total_dist)