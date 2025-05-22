def solution(k, m, score):
    answer = 0
    
    score.sort()
    
    while score:
        basket = []
        
        while score:
            basket.append(score.pop())
            
            if len(basket) == m:
                break
        
        if len(basket) == m:
            answer += (len(basket) * min(basket))
    
    return answer