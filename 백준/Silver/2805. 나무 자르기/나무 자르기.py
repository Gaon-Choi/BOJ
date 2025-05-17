import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

left, right = 0, max(arr)

ans = 0

while left <= right:
    mid = (left + right) // 2

    # parametric search
    total = sum(max(0, h - mid) for h in arr)

    # 더 높게 자를 수 있음 (total은 작아지는 방향)
    if total >= m:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
