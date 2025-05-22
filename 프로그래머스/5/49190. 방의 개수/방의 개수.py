def solution(arrows):
    answer = 0
    
    dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]
    
    visited_nodes = set()
    visited_edges = set()
    
    curr_x, curr_y = 0, 0
    visited_nodes.add((0, 0))
    
    for move in arrows:
        # 대각선 방향 이동을 위해 두 번 이동
        for _ in range(2):
            nx, ny = curr_x + dxs[move], curr_y + dys[move]
            
            edge = ((nx, ny), (curr_x, curr_y))
            rev_edge = ((curr_x, curr_y), (nx, ny))
            
            if (nx, ny) in visited_nodes and (edge not in visited_edges):
                answer += 1
                
            visited_nodes.add((nx, ny))
            visited_edges.add(edge)
            visited_edges.add(rev_edge)
            
            curr_x += dxs[move]
            curr_y += dys[move]
    
    return answer