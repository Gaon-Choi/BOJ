import sys
input = sys.stdin.readline

a, b = map(int, input().split())

ratio = b * 100 // a

ret = -1

left = 1; right = 1000000001

while left <= right:
    mid = (left + right) // 2

    if ((b + mid) * 100 // (a + mid) > ratio):
        ret = mid
        right = mid - 1
    else:
        left = mid + 1

print(ret)