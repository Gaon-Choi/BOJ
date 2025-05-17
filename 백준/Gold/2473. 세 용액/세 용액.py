import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

res = float('inf')
answer = []

# i : leftmost

for i in range(n - 2):
    left, right = i + 1, n - 1

    while left < right:
        total = arr[i] + arr[left] + arr[right]

        if abs(total) < res:
            res = abs(total)
            answer = [arr[i], arr[left], arr[right]]

        if total < 0:
            left += 1
        else:
            right -= 1

print(*answer)
