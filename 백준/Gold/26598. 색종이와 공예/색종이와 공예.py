import sys
input = sys.stdin.readline

from collections import deque

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x_, y_):
    origin = arr[x_][y_]
    min_x, max_x, min_y, max_y = x_, x_, y_, y_

    visited[x_][y_] = True

    queue = deque([(x_, y_)])

    while queue:
        x, y = queue.popleft()

        min_x = min(min_x, x); max_x = max(max_x, x)
        min_y = min(min_y, y); max_y = max(max_y, y)

        for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            nx, ny = x + dx, y + dy

            if is_reachable(nx, ny) and (not visited[nx][ny]) and (arr[nx][ny] == origin):
                visited[nx][ny] = True
                queue.append((nx, ny))

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (arr[x][y] != origin) or (not visited[x][y]):
                return False
    
    return True

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(input().strip())

visited = [[False] * m for _ in range(n)]

for x in range(n):
    for y in range(m):
        if not visited[x][y]:
            if not bfs(x, y):
                print("BaboBabo")
                exit(0)

print("dd")