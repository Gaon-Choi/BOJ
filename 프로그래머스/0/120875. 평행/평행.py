from itertools import combinations

def solution(dots):
    pair = list(combinations(range(4), 2))
    
    for i in range(len(pair)):
        for j in range(i + 1, len(pair)):
            p1, p2 = pair[i]
            p3, p4 = pair[j]
            
            if len({p1, p2, p3, p4}) != 4:
                continue
            
            x1, y1 = dots[p1]
            x2, y2 = dots[p2]
            x3, y3 = dots[p3]
            x4, y4 = dots[p4]
            
            if (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1):
                return 1
    
    return 0
