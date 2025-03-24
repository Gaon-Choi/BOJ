import sys
input = sys.stdin.readline

from collections import deque

def is_reachable(x, y):
    return (0 <= x < size) and (0 <= y < size)

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 0

    while queue:
        x_, y_ = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x_ + dx, y_ + dy

            if is_reachable(nx, ny) and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x_][y_] + 1
                queue.append([nx, ny])

dxs = [-1, -2, -2, -1, 1, 2, 2, 1]
dys = [-2, -1, 1, 2, 2, 1, -1, -2]

n = int(input())

result = []

for _ in range(n):
    size = int(input())

    visited = [[-1] * size for _ in range(size)]
    x, y = map(int, input().split())
    bfs(x, y)
    fx, fy = map(int, input().split())

    result.append(visited[fx][fy] if visited[fx][fy] >= 0 else 0)

for res in result:
    print(res)