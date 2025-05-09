import sys
input = sys.stdin.readline

n, m = map(int, input().split())

print("Yes" if (100 * n >= m) else "No")