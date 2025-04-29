n = int(input())

arr = list(map(int, input().split()))

ans = 1
cnt = 1
cnt2 = 1

for i in range(1, n):
    if arr[i] >= arr[i - 1]:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 1

    if arr[i] <= arr[i - 1]:
        cnt2 += 1
        ans = max(ans, cnt2)
    else:
        cnt2 = 1

print(ans)