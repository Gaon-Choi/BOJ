INF = float('inf')

def BellmanFord(graph, start):
    size = len(graph)
    dist = [INF] * (size)

    # 시작점에서의 비용은 0으로 설정
    dist[start] = 0

    # 정점의 개수만큼 반복
    for _ in range(size - 1):
        for u in range(1, size):
            for v, w in graph[u]:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    # 음수 사이클 탐지
    for u in range(1, size):
        for v, w in graph[u]:
            if dist[u] != INF and dist[u] + w < dist[v]:
                # 음수 가중치 사이클 발견되는 경우
                return None
            
    return dist[1:]


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

dist_result = BellmanFord(graph, 1)

if dist_result is not None:
    for i in range(1, len(dist_result)):
        print(dist_result[i] if dist_result[i] != INF else -1)
else:
    print(-1)