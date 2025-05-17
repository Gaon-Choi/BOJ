import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

def check_bipartile(graph):
    size = len(graph)

    visited = [-1] * size

    for start_point in range(1, size):
        if visited[start_point] == -1:

            queue = deque([start_point])
            visited[start_point] = 1

            while queue:
                x = queue.popleft()

                for adj in graph[x]:
                    if visited[adj] == -1:
                        visited[adj] = visited[x] ^ 1
                        queue.append(adj)

                    elif visited[adj] == visited[x]:
                        return False
            
    return True


for _ in range(T):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        start, end = map(int, input().split())

        graph[start].append(end)
        graph[end].append(start)

    res = check_bipartile(graph)

    print("YES" if res else "NO")