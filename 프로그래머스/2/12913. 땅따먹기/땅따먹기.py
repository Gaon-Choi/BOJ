def solution(land):
    answer = 0

    size = len(land)
    
    dp = [[0] * 4 for _ in range(size)]
    
    dp[0] = land[0][:]
    
    for i in range(1, size):
        for j in range(4):
            for k in range(4):
                if j == k:
                    continue
                    
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + land[i][j])
                
    answer = max(dp[size - 1])

    return answer