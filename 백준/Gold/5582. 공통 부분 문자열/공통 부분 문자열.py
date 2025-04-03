A = input()
B = input()
a, b = len(A), len(B)

max_cnt = 0

dp = [[0] * (b + 1) for _ in range(2)]

for i in range(1, a + 1):
    for j in range(1, b + 1):
        if A[i - 1] == B[j - 1]:
            dp[1][j] = dp[0][j - 1] + 1
            max_cnt = max(max_cnt, dp[1][j])
        else:
            dp[1][j] = 0
    
    dp.pop(0)
    dp.append([0] * (b + 1))

print(max_cnt)