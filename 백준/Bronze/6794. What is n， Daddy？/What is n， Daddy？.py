import sys
input = sys.stdin.readline

n = int(input())

left, right = min(n, 5), n - min(n, 5)

cnt = 0

while left >= right and right <= 5:
    left -= 1
    right += 1

    cnt += 1

print(cnt)