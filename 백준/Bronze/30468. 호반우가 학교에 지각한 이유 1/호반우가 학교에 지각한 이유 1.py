import sys
input = sys.stdin.readline

a, b, c, d, n = map(int, input().split())

print(max(0, 4 * n - (a + b + c + d)))
