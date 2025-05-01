import sys
input = sys.stdin.readline

m, n = map(int, input().split())

arr = [False] * (n + 1)
arr[1] = True    # 1은 소수도 아니고 합성수도 아님!

for i in range(2, n + 1):
    if arr[i]:
        continue

    for j in range(2 * i, n + 1, i):
        arr[j] = True

for i in range(m, n + 1):
    if not arr[i]:
        print(i)