from collections import deque

def is_reachable(n):
    return (0 <= n <= size)# and (arr[n] == -1)
    
def bfs(n_: int):
    global cnt
    
    arr[n_] = 0
    queue = deque([n_])
    
    while len(queue) > 0:
        n = queue.popleft()
        
        if n == K:
            cnt += 1
            continue
        
        if is_reachable(n - 1) and (arr[n - 1] == -1 or arr[n - 1] == arr[n] + 1):
            arr[n - 1] = arr[n] + 1
            queue.append(n - 1)
            
        if is_reachable(n + 1) and (arr[n + 1] == -1 or arr[n + 1] == arr[n] + 1):
            arr[n + 1] = arr[n] + 1
            queue.append(n + 1)
            
        if is_reachable(n * 2) and (arr[2 * n] == -1 or arr[2 * n] == arr[n] + 1):
            arr[n * 2] = arr[n] + 1
            queue.append(n * 2)
            
N, K = map(int, input().split())

size = 100000

arr = [-1] * (size + 1)

cnt = 0

bfs(N)

print(arr[K])
print(cnt)