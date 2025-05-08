def solution(a, b, n):
    answer = 0
    
    while n >= a:
        reward = (n // a) * b
        answer += reward
        n = (n % a) + reward
    
    return answer