def is_reachable(n):
    return (0 <= n <= N) and arr[n] == -1
    
def bfs(n_: int):
    arr[n_] = 0
    queue = [n_]
    
    while len(queue) > 0:
        n = queue.pop(0)

        if is_reachable(n * 2):
            arr[n * 2] = arr[n]
            queue.append(n * 2)
        
        if is_reachable(n - 1):
            arr[n - 1] = arr[n] + 1
            queue.append(n - 1)
            
        if is_reachable(n + 1):
            arr[n + 1] = arr[n] + 1
            queue.append(n + 1)

            
n, k = map(int, input().split())

N = 100000

arr = [-1] * (N + 1)

bfs(n)

print(arr[k])