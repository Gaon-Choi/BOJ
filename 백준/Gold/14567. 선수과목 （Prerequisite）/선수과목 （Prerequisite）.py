import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

result = [1] * (n + 1)
indegree = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    src, tgt = map(int, input().split())
    indegree[tgt] += 1
    graph[src].append(tgt)

queue = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()

    for nxt in graph[x]:
        indegree[nxt] -= 1

        result[nxt] = max(result[nxt], result[x] + 1)

        if indegree[nxt] == 0:
            queue.append(nxt)

print(*result[1:])
