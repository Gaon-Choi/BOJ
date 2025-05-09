import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

arr = list(map(int, input().split()))

arr.sort()

left, right = 0, n - 1
cnt = 0

while left < right:
    s = arr[left] + arr[right]

    if s == k:
        cnt += 1
        left += 1
        right -= 1

    elif s < k:
        left += 1
    
    else:
        right -= 1

print(cnt)