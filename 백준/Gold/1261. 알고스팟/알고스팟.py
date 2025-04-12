import heapq

INF = float('inf')

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < m

def dijkstra():
    dist = [[INF] * m for _ in range(n)]
    q = []
    heapq.heappush(q, (0, 0, 0))

    dist[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if is_reachable(nx, ny):
                new_cost = cost + matrix[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))

    return dist

m, n = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, list(input()))))

dist_result = dijkstra()

print(dist_result[n - 1][m - 1])