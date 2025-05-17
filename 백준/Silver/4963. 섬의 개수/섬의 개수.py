import sys
input = sys.stdin.readline

from collections import deque

def is_reachable(x, y):
    return 0 <= x < h and 0 <= y < w

def bfs(x_, y_):
    global visited

    visited[x_][y_] = True

    queue = deque([(x_, y_)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip([-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]):
            nx, ny = x + dx, y + dy
            
            if is_reachable(nx, ny) and (matrix[nx][ny] == 1) and (not visited[nx][ny]):
                visited[nx][ny] = True
                queue.append((nx, ny))

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    matrix = []

    for _ in range(h):
        matrix.append(list(map(int, input().split())))

    visited = [[False] * w for _ in range(h)]

    cnt = 0

    for x in range(h):
        for y in range(w):
            if (matrix[x][y] == 1) and (not visited[x][y]):
                bfs(x, y)
                cnt += 1

    print(cnt)
