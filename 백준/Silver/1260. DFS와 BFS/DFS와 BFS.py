def DFS(G, V, N):
	global dfs_result
	global dfs_visited

	dfs_visited[V] = True
	dfs_result.append(V)

	for curr_v in sorted(G[V]):
	    if not dfs_visited[curr_v]:
	        DFS(G, curr_v, N)
			
def BFS(G, V, N):
    global bfs_result
    global bfs_visited
	
    bfs_visited[V] = True
    bfs_result.append(V)
	
    queue = [V]
	
    while queue:
	    curr_v = queue.pop(0)
	    for v in sorted(G[curr_v]):
	        if not bfs_visited[v]:
	            bfs_visited[v] = True
	            bfs_result.append(v)
	            queue.append(v)

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

dfs_result = []
dfs_visited = [False for _ in range(N + 1)]

DFS(graph, V, N)

bfs_result = []
bfs_visited = [False for _ in range(N + 1)]

BFS(graph, V, N)

print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))

