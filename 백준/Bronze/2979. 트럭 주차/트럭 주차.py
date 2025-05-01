import sys
input = sys.stdin.readline

time = [0] + list(map(int, input().split()))

arr = [0] * 101

for _ in range(3):
    start, end = map(int, input().split())
    
    for i in range(start, end):
        arr[i] += 1

ans = 0

for i in range(len(arr)):
    ans += time[arr[i]] * arr[i]

print(ans)