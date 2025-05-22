def solution(x, y, n):
    answer = 0
    
    dp = [-1] * (y + 1)

    dp[x] = 0
    
    for num in range(x + 1, y + 1):
        a, b, c = None, None, None
        
        if num - n >= x:
            a = dp[num - n]
        if (num // 2 >= x) and (num % 2 == 0):
            b = dp[num // 2]
        if (num // 3 >= x) and (num % 3 == 0):
            c = dp[num // 3]
            
        candidates = [v for v in [a, b, c] if (v is not None) and (v != -1)]

        if candidates:
            dp[num] = min(candidates) + 1
        
    answer = dp[y]
    
    return answer