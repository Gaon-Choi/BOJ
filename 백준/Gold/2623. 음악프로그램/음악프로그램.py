import sys
input = sys.stdin.readline

from collections import deque

def topological_sort(graph):
    size = len(graph)
    result = []

    indegree = [0] * size

    for u in range(size):
        for v in graph[u]:
            indegree[v] += 1

    q = deque()

    for v in range(1, size):
        if indegree[v] == 0:
            q.append(v)

    while q:
        v = q.popleft()

        result.append(v)

        for adj in graph[v]:
            indegree[adj] -= 1
            if (indegree[adj] == 0):
                q.append(adj)

    return result

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    arr = list(map(int, input().split()))

    for i in range(1, arr[0]):
        u, v = arr[i], arr[i + 1]
        graph[u].append(v)

res = topological_sort(graph)

if len(res) == n:
    for v in res:
        print(v)
else:
    print(0)