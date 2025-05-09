import sys
input = sys.stdin.readline

n = int(input())
ans = 0

word = input().strip()

for i in range(n):
    if word[i] in {"a", "e", "i", "o", "u"}:
        ans += 1

print(ans)