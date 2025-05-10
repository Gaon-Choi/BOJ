import sys
input = sys.stdin.readline

n = int(input())
arr = []

support = int(input())
arr.append(support)
arr.extend(list(map(int, input().split())))

arr.sort(reverse=True)

for rank in range(n):
    if arr[rank] == support:
        print(rank + 1)
        break
