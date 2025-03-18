N = 100000

n, k = map(int, input().split())
visited = [[False, 0] for _ in range (N + 1)]
path = [-1] * (N + 1)

def f1(n):
    return n - 1

def f2(n):
    return n + 1
    
def f3(n):
    return n * 2
    
def is_reachable(n):
    return (0 <= n <= N) and not visited[n][0]
    
def bfs(n):
    queue = [n]
    visited[n][0] = True
    
    while len(queue) > 0:
        num = queue.pop(0)
        
        if num == k:
            return
        
        if is_reachable(f1(num)):
            visited[f1(num)][0] = True
            visited[f1(num)][1] = visited[num][1] + 1
            path[f1(num)] = num
            queue.append(f1(num))
            
        if is_reachable(f2(num)):
            visited[f2(num)][0] = True
            visited[f2(num)][1] = visited[num][1] + 1
            path[f2(num)] = num
            queue.append(f2(num))
            
        if is_reachable(f3(num)):
            visited[f3(num)][0] = True
            visited[f3(num)][1] = visited[num][1] + 1
            path[f3(num)] = num
            queue.append(f3(num))
            
def get_path(n):
    arr = []
    p = path[n]
    
    while True:
        if p == -1:
            break
      
        arr.append(p)
        p = path[p]
    
    return arr

bfs(n)
    
print(visited[k][1])

k_path = ([k] + get_path(k))[-1::-1]

print(" ".join(map(str, k_path)))