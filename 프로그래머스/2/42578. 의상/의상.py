def solution(clothes):
    answer = 1
    
    clothes_hash = dict()
    
    for cloth in clothes:
        category = cloth[1]
        
        if category in clothes_hash:
            clothes_hash[category] += 1
        else:
            clothes_hash[category] = 1
            
    for k, v in clothes_hash.items():
        answer *= (v + 1)
        
    answer -= 1
    
    return answer