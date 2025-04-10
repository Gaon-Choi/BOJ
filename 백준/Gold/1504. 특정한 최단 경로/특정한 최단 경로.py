import math
import heapq

def Dijkstra(graph, src):
    '''
    graph   : a graph with form of adjancy list (vertex, cost)
    src     : starting point (vertex)
    '''

    dist = [math.inf] * (len(graph) + 1)

    pq = []

    # 탐색을 시작할 정점에 대해 거리를 0으로 설정하고 힙에 삽입
    dist[src] = 0
    heapq.heappush(pq, (0, src))

    # 힙 내부가 비어있기 전까지 계속 반복
    while len(pq) > 0:
        curr_dist, u = heapq.heappop(pq)

        for v, cost in graph[u]:
            # 새로 갱신된 거리
            new_dist = curr_dist + cost

            # 새로 계산된 거리가 기존의 dist 배열에 저장된 거리 값보다 작은 경우 갱신
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(e):
    start, end, cost = map(int, input().split())

    graph[start].append((end, cost))
    graph[end].append((start, cost))

v1, v2 = map(int, input().split())

result1, result2 = 0, 0
# 1 -> v1 -> v2 -> n
dist = Dijkstra(graph, 1)
result1 += dist[v1]
dist = Dijkstra(graph, v1)
result1 += dist[v2]
dist = Dijkstra(graph, v2)
result1 += dist[n]

# 1 -> v2 -> v1 -> n
dist = Dijkstra(graph, 1)
result2 += dist[v2]
dist = Dijkstra(graph, v2)
result2 += dist[v1]
dist = Dijkstra(graph, v1)
result2 += dist[n]

res = min(result1, result2)

print(res if res != math.inf else -1)