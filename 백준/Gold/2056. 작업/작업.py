from collections import deque

def topological_sort():
    res = []

    queue = deque([])

    for i in range(1, n + 1):
        if indegree[i] == 0:
            dp[i] = cost[i]
            queue.append(i)

    while queue:
        v = queue.popleft()

        res.append(v)

        for adj in graph[v]:
            dp[adj] = max(dp[adj], dp[v] + cost[adj])

            indegree[adj] -= 1

            if indegree[adj] == 0:
                queue.append(adj)

    return res

if __name__ == "__main__":
    n = int(input())

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    cost = [0]
    dp = [0] * (n + 1)

    for start in range(1, n + 1):
        arr = list(map(int, input().split()))

        cost.append(arr[0])

        for end in arr[2:]:
            # end -> start
            graph[end].append(start)
            indegree[start] += 1

    sort_res = topological_sort()

    print(max(dp))