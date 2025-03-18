n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, list(input()))))
    
visited = [[False] * n for _ in range(n)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def is_reachable(x, y):
    return (0 <= x < n and 0 <= y < n) and (not visited[x][y]) and (matrix[x][y] == 1)
    
def bfs(x_, y_):
    visited[x_][y_] = True
    
    cnt = 1
    queue = [[x_, y_]]
    
    while len(queue) > 0:
        x, y = queue.pop(0)
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if is_reachable(nx, ny):
                visited[nx][ny] = True
                cnt += 1
                queue.append([nx, ny])
                
    return cnt
    
result = []
    
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and (not visited[i][j]):
            result.append(bfs(i, j))
                
result.sort()

print(len(result))

for res in result:
    print(res)
                