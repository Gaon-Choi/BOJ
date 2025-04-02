import sys
import heapq

input = sys.stdin.readline

def topological_sort():
    pq = []
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            dp[i] = vertices[i]
            heapq.heappush(pq, i)

    while pq:
        v = heapq.heappop(pq)

        for adj in graph[v]:
            indegree[adj] -= 1
            dp[adj] = max(dp[adj], dp[v] + vertices[adj])

            if indegree[adj] == 0:
                heapq.heappush(pq, adj)

    return dp[final]

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    vertices = [0] + list(map(int, input().split()))

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    final = int(input())

    print(topological_sort())

    