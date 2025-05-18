import sys
input = sys.stdin.readline

INF = float('inf')

min_x, min_y, max_x, max_y = INF, INF, -INF, -INF

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    min_x, min_y, max_x, max_y = min(min_x, x), min(min_y, y), max(max_x, x), max(max_y, y)

print(abs((min_x - max_x) * (min_y - max_y)))

