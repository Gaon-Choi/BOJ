import sys
input = sys.stdin.readline

k, n = map(int, input().split())

arr = []
for _ in range(k):
    arr.append(int(input()))

ans = 0

left, right = 1, max(arr)

while left <= right:
    mid = (left + right) // 2

    total_cnt = sum(line // mid for line in arr)

    # 이미 잘라서 만든 개수가 충분한 경우
    if total_cnt >= n:
        ans = max(ans, mid)
        left = mid + 1
        
    # 자르는 길이를 줄여야 함
    else:
        right = mid - 1

print(ans)
