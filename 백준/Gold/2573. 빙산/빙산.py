def check_if_all_melted():
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                return False
                
    return True

def get_cnt(x, y):
    cnt = 0
    
    if (0 <= x - 1 < n and 0 <= y < m) and matrix[x-1][y] == 0:
        cnt += 1
    if (0 <= x + 1 < n and 0 <= y < m) and matrix[x+1][y] == 0:
        cnt += 1
    if (0 <= x < n and 0 <= y + 1 < m) and matrix[x][y+1] == 0:
        cnt += 1
    if (0 <= x < n and 0 <= y - 1 < m) and matrix[x][y-1] == 0:
        cnt += 1

    return cnt

def heighten_iceberg():
    tmp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0:
                tmp[i][j] = max(matrix[i][j] - get_cnt(i, j), 0)
                
    return tmp

def is_reachable(x, y):
    return (0 <= x < n and 0 <= y < m) and (not visited[x][y]) and (matrix[x][y] != 0)
    
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
    
def bfs(x_, y_):
    visited[x_][y_] = True
    cnt = 1
    
    queue = [[x_, y_]]
    
    while queue:
        x, y = queue.pop(0)
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if is_reachable(nx, ny):
                visited[nx][ny] = True
                cnt += 1
                queue.append([nx, ny])
    
    return cnt
    
n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

t = 0

while True:
    visited = [[False] * m for _ in range(n)]
    
    tmp_result = []
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] >= 1 and (not visited[i][j]):
                tmp_result.append(bfs(i, j))
                
    if len(tmp_result) > 1:
        break
    
    matrix = heighten_iceberg()
    t += 1
    
    if check_if_all_melted():
        print(0)
        exit(0)

print(t)