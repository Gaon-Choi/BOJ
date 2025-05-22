def solution(wallpaper):
    answer = []
    
    lux, luy, rdx, rdy = 100, 100, 0, 0
    
    matrix = []
    
    for w in wallpaper:
        matrix.append([1 if (elem == "#") else 0 for elem in list(w)])
        
    size_h, size_w = len(matrix), len(matrix[0])
    
    for x in range(size_h):
        for y in range(size_w):
            if matrix[x][y] == 1:
                lux, luy = min(lux, x), min(luy, y)
                rdx, rdy = max(rdx, x), max(rdy, y)
        
    answer.extend([lux, luy, rdx + 1, rdy + 1])
    
    return answer