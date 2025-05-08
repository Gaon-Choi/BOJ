def solution(chicken):
    answer = 0
    
    while chicken >= 10:
        reward = (chicken // 10)
        chicken = (chicken % 10) + reward
        answer += reward
        
    return answer
        
        