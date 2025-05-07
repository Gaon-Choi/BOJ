import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))
    
min_coin = [1e9] * (k + 1)
min_coin[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        if min_coin[i - coin] != 1e9:
            min_coin[i] = min(min_coin[i], min_coin[i - coin] + 1)

print(min_coin[k] if min_coin[k] != 1e9 else -1)