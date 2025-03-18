f, s, g, u, d = map(int, input().split())

arr = [-1] * (f + 1)

visited = [False] * (f + 1)

def is_reachable(x):
    return (0 < x <= f) and not visited[x]
    
def bfs(x):
    visited[x] = True
    arr[x] = 0
    
    queue = [x]
    
    while queue:
        x_ = queue.pop(0)
        
        if is_reachable(x_ + u):
            visited[x_ + u] = True
            arr[x_ + u] = arr[x_] + 1
            queue.append(x_ + u)
        
        if is_reachable(x_ - d):
            visited[x_ - d] = True
            arr[x_ - d] = arr[x_] + 1
            queue.append(x_ - d)
            
bfs(s)

ans = arr[g]

if ans == -1:
    print("use the stairs")
else:
    print(ans)