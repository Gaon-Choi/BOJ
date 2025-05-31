import sys
input = sys.stdin.readline

n = int(input())

result = 2024 * 12 + 8
x = result + 7 * (n - 1)

year, month = x // 12, x % 12

if month == 0:
    year -= 1
    month = 12

print(year, month)
