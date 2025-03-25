def DFS(graph, v):
    result = []
    visited = [False] * len(graph)

    stack = [v]

    while stack:
        vertex = stack.pop()
        
        if not visited[vertex]:
            visited[vertex] = True
            result.append(vertex)
            
            for curr_v in sorted(graph[vertex], reverse=True):
                if not visited[curr_v]:
                    stack.append(curr_v)
                    
    return result
			
def BFS(graph, v):
    result = []
    visited = [False] * len(graph)

    visited[v] = True
    queue = [v]
	
    while queue:
        vertex = queue.pop(0)
        result.append(vertex)

        for curr_v in sorted(graph[vertex]):
            if not visited[curr_v]:
                visited[curr_v] = True
                queue.append(curr_v)
                
    return result

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

dfs_result = DFS(graph, V)

bfs_result = BFS(graph, V)

print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))

