def solution(brown, yellow):
    answer = []
    w = 1
    
    while True:
        for h in range(1, w + 1):
            if w * h - (w - 2) * (h - 2) == brown and (w - 2) * (h - 2) == yellow:
                return [w, h]
            
        w += 1
            
    
    return answer