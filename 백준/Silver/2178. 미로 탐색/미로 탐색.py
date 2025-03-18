n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, list(str(input())))))
    
visited = [[[False, 0] for _ in range(m)] for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def is_reachable(x, y):
    return (0 <= x < n and 0 <= y < m) and (visited[x][y][0] is False) and (matrix[x][y] == 1)
    
def bfs(x_, y_):
    visited[x_][y_][0] = True
    
    queue = [[x_, y_]]
    
    while len(queue) > 0:
        x, y = queue.pop(0)
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if is_reachable(nx, ny):
                visited[nx][ny][0] = True
                visited[nx][ny][1] = visited[x][y][1] + 1
                queue.append([nx, ny])
                
bfs(0, 0)

print(visited[n-1][m-1][1] + 1)