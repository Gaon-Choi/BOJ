def solution(n):
    answer = 0
    
    is_prime = [False, False] + [True] * (n - 1)
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    answer = is_prime.count(True)
    
    
    
    return answer