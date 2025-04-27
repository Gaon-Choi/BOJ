n, m = map(int, input().split())

arr = list(map(int, input().split()))

accum_arr = []
accum_arr.append(0)

for elem in arr:
    accum_arr.append(accum_arr[-1] + elem)

left = 1
right = 1
cnt = 0

while (right <= n):
    s = accum_arr[right] - accum_arr[left - 1]

    if (s == m):
        cnt += 1

    if (s >= m):
        left += 1

    else:
        right += 1

print(cnt)