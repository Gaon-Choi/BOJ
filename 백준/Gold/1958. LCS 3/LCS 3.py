import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()
word3 = input().strip()

X, Y, Z = len(word1), len(word2), len(word3)

dp = [[[0] * (Z + 1) for _ in range(Y + 1)] for _ in range(X + 1)]


for x in range(1, X + 1):
    for y in range(1, Y + 1):
        for z in range(1, Z + 1):
            if word1[x - 1] == word2[y - 1] == word3[z - 1]:
                dp[x][y][z] = dp[x - 1][y - 1][z - 1] + 1
            else:
                dp[x][y][z] = max(
                    dp[x - 1][y][z],
                    dp[x][y - 1][z],
                    dp[x][y][z - 1]
                )

print(dp[X][Y][Z])