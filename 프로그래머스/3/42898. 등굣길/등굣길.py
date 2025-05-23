def solution(m, n, puddles):
    MOD = 1000000007
    
    puddle_set = set()
    
    for puddle in puddles:
        y, x = puddle
        puddle_set.add((x, y))
        
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    dp[1][1] = 1
    puddle_set.add((1, 1))
        
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if (x, y) in puddle_set:
                continue
                
            dp[x][y] = (dp[x - 1][y] + dp[x][y - 1]) % MOD
            
    answer = dp[n][m]
    
    return answer