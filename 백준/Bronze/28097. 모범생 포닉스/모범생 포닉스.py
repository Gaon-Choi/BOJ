import sys
input = sys.stdin.readline

n = int(input())

total = 0

arr = list(map(int, input().split()))

total += sum(arr)
total += 8 * (n - 1)

print(total // 24, total % 24)