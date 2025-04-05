n, h = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

cnt = 0
flag = False

for i in range(n):
    h -= arr[i]
    cnt += 1

    if h <= 0:
        flag = True
        break

print(cnt if flag else -1)