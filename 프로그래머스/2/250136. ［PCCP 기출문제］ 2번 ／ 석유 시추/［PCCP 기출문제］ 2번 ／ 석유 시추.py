from collections import deque

def solution(land):
    def is_reachable(x, y):
        return 0 <= x < size_h and 0 <= y < size_w
    
    def dfs(x, y):
        stack = deque()
        stack.append((x, y))
        visited[x][y] = True
        width_set = set()
        
        cnt = 0
        
        while stack:
            x_, y_ = stack.pop()
            width_set.add(y_)
            cnt += 1
            
            for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                nx, ny = x_ + dx, y_ + dy
                
                if is_reachable(nx, ny) and (land[nx][ny] == 1) and (not visited[nx][ny]):
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                
        for width in width_set:
            arr[width] += cnt
                
        return cnt
        
    answer = 0
    
    size_h, size_w = len(land), len(land[0])
    visited = [[False] * size_w for _ in range(size_h)]
    arr = [0] * size_w
    
    for p in range(size_w):
        petroleum_cnt = 0
        
        for h in range(size_h):
            if (land[h][p] == 1) and (not visited[h][p]):
                dfs(h, p)
                
    answer = max(arr)
    
    return answer