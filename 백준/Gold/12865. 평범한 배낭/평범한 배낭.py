n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]


for c in range(1, n + 1):
    w, v = map(int, input().split())

    for i in range(1, k + 1):
        # 물건을 넣을 수 없는 경우
        if i < w:
            dp[c][i] = dp[c-1][i]
        # 물건을 넣을 수 있는 경우
        else:
            # 물건을 넣지 않은 경우 / 현재 물건의 무게만큼을 제외하고 이 물건을 넣는 경우
            dp[c][i] = max(dp[c - 1][i], dp[c - 1][i - w] + v)

print(dp[n][k])