def solution(maps):
    answer = 0
    
    height = len(maps)
    width = len(maps[0])
    
    visited = [[-1] * width for _ in range(height)]
    
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    
    def is_reachable(x, y):
        return 0 <= x < height and 0 <= y < width and visited[x][y] == -1 and maps[x][y] == 1
    
    def bfs(x, y):
        queue = [[x, y]]
        visited[x][y] = 1
        
        while len(queue) > 0:
            x_, y_ = queue.pop(0)
            
            for dx, dy in zip(dxs, dys):
                nx, ny = x_ + dx, y_ + dy
                
                if is_reachable(nx, ny):
                    visited[nx][ny] = visited[x_][y_] + 1
                    queue.append([nx, ny])
        
    bfs(0, 0)
        
    answer = visited[height - 1][width - 1]
    
    return answer