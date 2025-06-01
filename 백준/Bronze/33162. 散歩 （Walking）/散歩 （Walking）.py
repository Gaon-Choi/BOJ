import sys
input = sys.stdin.readline

n = int(input())

left, right = n // 2, n // 2

if n % 2 == 1:
    left += 1

print(3 * left - 2 * right)
