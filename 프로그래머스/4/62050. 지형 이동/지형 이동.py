from collections import deque

def solution(land, height):
    def find(x):
        if uf[x] == x:
            return x
        
        root_node = find(uf[x])
        uf[x] = root_node
        
        return root_node
    
    def union(x, y):
        x_, y_ = find(x), find(y)
        uf[y_] = x_
    
    def is_reachable(x, y):
        size = len(land)
        return 0 <= x < size and 0 <= y < size
    
    def bfs(x, y, land_color):
        nonlocal landscape
        
        landscape[x][y] = land_color
        queue = deque([(x, y)])
        
        while queue:
            x_, y_ = queue.popleft()
            
            for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                nx, ny = x_ + dx, y_ + dy
                
                if is_reachable(nx, ny) and (landscape[nx][ny] == -1):
                    if abs(land[nx][ny] - land[x_][y_]) <= height:
                        landscape[nx][ny] = land_color
                        queue.append((nx, ny))
    
    answer = 0
    
    land_idx = 1
    
    size = len(land)
    
    landscape = [[-1] * size for _ in range(size)]
    
    for x in range(size):
        for y in range(size):
            if landscape[x][y] == -1:
                bfs(x, y, land_idx)
                land_idx += 1
    
    # edge
    edges = dict()
    
    for x in range(size):
        for y in range(size):
            if x + 1 < size and landscape[x][y] != landscape[x + 1][y]:
                a, b = landscape[x][y], landscape[x + 1][y]
                diff = abs(land[x][y] - land[x + 1][y])
                
                if (frozenset([a, b])) not in edges:
                    edges[frozenset([a, b])] = diff
                else:
                    edges[frozenset([a, b])] = min(edges[frozenset([a, b])], diff)
                    
            if y + 1 < size and landscape[x][y] != landscape[x][y + 1]:
                a, b = landscape[x][y], landscape[x][y + 1]
                diff = abs(land[x][y] - land[x][y + 1])
                
                if (frozenset([a, b])) not in edges:
                    edges[frozenset([a, b])] = diff
                else:
                    edges[frozenset([a, b])] = min(edges[frozenset([a, b])], diff)
    
    edges = sorted([(cost, tuple(pair)) for pair, cost in edges.items()])
    
    uf = list(range(land_idx))
    
    for cost, [start, end] in edges:
        if find(start) != find(end):
            union(start, end)
            answer += cost
    
    return answer