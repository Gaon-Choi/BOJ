import heapq

def topological_sort():
    queue = []

    res = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(queue, i)

    while len(queue) > 0:
        x = heapq.heappop(queue)

        res.append(x)

        for v in graph[x]:
            indegree[v] -= 1

            if indegree[v] == 0:
                heapq.heappush(queue, v)

    return res

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    # a > b <=> a -> b
    a, b = map(int, input().split())

    graph[a].append(b)

    indegree[b] += 1

result = topological_sort()

for elem in result:
    print(elem, end = " ")