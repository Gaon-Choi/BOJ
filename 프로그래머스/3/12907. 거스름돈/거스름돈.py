def solution(n, money):
    answer = 0
    
    MOD = 1000000007
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for coin in money:
        for total in range(coin, n + 1):
            dp[total] = (dp[total] + dp[total - coin]) % MOD
                
    answer = dp[n]
    
    return answer